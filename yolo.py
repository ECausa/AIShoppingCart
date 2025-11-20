from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")
class_names = model.names
# print("List of labels (class names):")
# print(class_names)

# Open camera (1 = default webcam for Sams MacBook)
cap = cv2.VideoCapture(0)

# load lables to filter results
filterLables = []
with open('labels.txt','r') as f:
    content = f.read()
    filterLables = content.splitlines()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection
    results = model(frame, stream=True)  # stream=True yields results in real-time

    # Loop through results and draw boxes
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            cls = int(box.cls[0])
            conf = box.conf[0]
            label = r.names[cls]
            
            # check for macthing items
            if label in filterLables:
                if "apple" in label:
                    print("apple price $0.75/lb")
                if "banana" in label:
                    print("banana price $0.54/lb")
                if "orange" in label:
                    print("orange price $1.33/lb")
                if "bread" in label:
                    print("bread price is $2.80")
                if "donut" in label:
                    print("donut price is $2.00")
                if "cake" in label:
                    print("cake price is $15.00")
                if "carrot" in label:
                    print("carrot price is $2.50")
                if "broccoli" in label:
                    print("broccoli price is $1.90")
                if "pizza" in label:
                    print("pizza price is $9.00")
                if "hot dog" in label:
                    print("hot dog price is $5.00")


            # Draw rectangle + label
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    cv2.imshow("YOLO Live Detection", frame)
    if cv2.waitKey(1) == 27:  # ESC key to stop
        break

cap.release()
cv2.destroyAllWindows()
