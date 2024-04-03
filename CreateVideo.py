import os
import cv2

path = "Images"

Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    
    if ext.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        file_name = os.path.join(path, file)
        
        Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])
height, width, channels = frame.shape

size = (width, height)
print("Image Size:", size)

video_name = "Project.avi"

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fps = 0.8


out = cv2.VideoWriter(video_name, fourcc, fps, size)

for i in range(count):
    img = cv2.imread(Images[i])
    
    out.write(img)

out.release()

print("Done")
