import os

backend_dir = os.path.dirname(os.path.abspath(__file__))
model_path=os.path.join(backend_dir,"src","assets","resnet_feature_extractor_7class2.pth")
project_root = os.path.dirname(backend_dir)
frontend_path = os.path.join(project_root, "frontend", "index.html")
