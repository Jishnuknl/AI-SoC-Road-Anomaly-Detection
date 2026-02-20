from ultralytics import YOLO
import cv2

def main():
    # Load trained YOLOv8 model
    model = YOLO("best.pt") 

    # Open webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Camera not accessible")
        return

    print("Press 'q' to exit...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Run inference
        results = model(frame)

        # Annotate frame
        annotated_frame = results[0].plot()

        cv2.imshow("AI-SoC Road Anomaly Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
