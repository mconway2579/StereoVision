import numpy as np
import cv2 as cv
import sys
if __name__ == "__main__":
    captures = []
    for i in range(10):
        cap = cv.VideoCapture(i)
        if cap.isOpened():
            captures.append((cap, i))
    while True:
        for cap, index in captures:
            # Capture frame-by-frame
            e1 = cv.getTickCount()
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # Display the resulting frame
            e2 = cv.getTickCount()
            time = (e2 - e1)/cv.getTickFrequency()
            frame = cv.putText(frame, str(time), (00, 185), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv.LINE_AA, False)
            cv.imshow(str(index), frame)
            print(f"device ({index}) shape: {frame.shape}")

            if cv.waitKey(1) == ord('q'):
                # When everything done, release the capture
                for c, i in captures:
                    c.release()
                cv.destroyAllWindows()
                exit()
