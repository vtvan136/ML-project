# Dùng để load data
from torchvision import datasets, models, transforms
from torchvision.datasets import ImageFolder
data_dir = "data/processed"
train_dir = data_dir + "/train"
valid_dir = data_dir + "/valid"
train = ImageFolder(train_dir, transform=transforms.ToTensor())
valid = ImageFolder(valid_dir, transform=transforms.ToTensor())