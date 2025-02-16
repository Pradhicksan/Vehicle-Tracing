from ultralytics import YOLO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import os

# loading the model
model = YOLO("yolov8l.pt")

# arguments to be used
video_path = r"E:\Abiotic Neuron\DS\DS Projects\Vehicle Tracing\2.mp4"
output_folder_path = r"E:\Abiotic Neuron\DS\DS Projects\Vehicle Tracing\video_output"

# using the model on the video
model.track(source=video_path, classes=[2], save=True, project=output_folder_path, line_width=3)


