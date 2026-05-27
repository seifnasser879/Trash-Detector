import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from huggingface_hub import hf_hub_download
from config import model_path

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


resnet = models.resnet50(weights=None)

num_features = resnet.fc.in_features
resnet.fc = nn.Sequential(
    nn.Linear(num_features, 512),
    nn.ReLU(),
    nn.Dropout(0.3),
    nn.Linear(512, 7)
)

resnet = resnet.to(device)

if os.path.exists(model_path):
    resnet.load_state_dict(
        torch.load(model_path, map_location=device)
    )
else:
    repo_id = "seif-nasser/trash_detector"
    filename = "resnet_feature_extractor_7class2.pth"

    weights_path = hf_hub_download(
        repo_id=repo_id,
        filename=filename
    )

    resnet.load_state_dict(
        torch.load(weights_path, map_location=device)
    )
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    torch.save(resnet.state_dict(), model_path)

resnet.eval()

test_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225]
    )
])