"""
Download the DermaMNIST dataset.
"""

from medmnist import INFO
from medmnist import DermaMNIST


# Dataset information
info = INFO["dermamnist"]

print("Dataset Information")
print("-------------------")
print(f"Description : {info['description']}")
print(f"Task        : {info['task']}")
print(f"Labels      : {info['label']}")
print(f"Number of classes : {len(info['label'])}")

# Download dataset
train_dataset = DermaMNIST(split="train", download=True)
val_dataset = DermaMNIST(split="val", download=True)
test_dataset = DermaMNIST(split="test", download=True)

print()
print("Dataset downloaded successfully!")

print(f"Training samples   : {len(train_dataset)}")
print(f"Validation samples : {len(val_dataset)}")
print(f"Testing samples    : {len(test_dataset)}")