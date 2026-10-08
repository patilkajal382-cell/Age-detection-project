import os
import cv2

dataset_path = r"C:\Users\KAJAL\Downloads\archive (7)\utkface_aligned_cropped\UTKFace"

files = os.listdir(dataset_path)

print("Total images:", len(files))
print("First 5 files:", files[:5])


img = cv2.imread(os.path.join(dataset_path, files[0]))

print("Image shape:", img.shape)