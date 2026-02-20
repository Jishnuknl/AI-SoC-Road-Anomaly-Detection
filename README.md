# AI-SoC-Road-Anomaly-Detection
Bharat AI-SoC National Level Project – 2026

## About the Project
This project focuses on detecting potholes, manholes, and speed breakers in real time using YOLOv8.  
The system is deployed on Raspberry Pi 5 with a web camera module.

## Objective
- Real-time road defect detection
- To improve road safety using a low cost AI solution
- Deployment on Raspberry Pi
- To implement real time detection using camera input

## Model Details
Model: YOLOv8n  
Image Size: 640x640  
Classes:
- Pothole
- Manhole
- Speedbreaker

## Hardware Used
- Raspberry Pi 5
- Web camera
- SD Card
- Power Supply

# performance
- The model was tested on validation data and deployed on Raspberry Pi 5 for real-time detection.
- The system successfully detects potholes, manholes, and speed breakers under normal lighting conditions.
- Performance evaluation graphs and sample outputs are available in the results folder.

# Future scope
- Integrate LIDAR senor for depth based defect measurement.
- The system can be linked with digital maps to identify roads that have more defects.
- Add GPS module to upload pothole location to cloud.  
- Deploy on moving vehicles for smart city applications.

# Results
- The model was trained using YOLOv8 nano.
- Successfully detects potholes, manholes, and speed breakers in real-time.
- Works smoothly on Raspberry Pi 5 with live camera input.
  
## License
MIT License
