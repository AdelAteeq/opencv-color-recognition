import cv2
import numpy as np


def clean_mask(mask):
    """
    Remove small noise and fill small gaps inside detected objects.
    """
    kernel = np.ones((5, 5), np.uint8)

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        kernel
    )

    return mask


def detect_color(frame, mask, color_name, box_color):
    """
    Find colored objects and draw rectangles around them.
    """
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)

        # Ignore very small objects
        if area > 500:
            x, y, width, height = cv2.boundingRect(contour)

            cv2.rectangle(
                frame,
                (x, y),
                (x + width, y + height),
                box_color,
                2
            )

            cv2.putText(
                frame,
                color_name,
                (x, max(y - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                box_color,
                2
            )


def main():
    # Open the webcam
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not camera.isOpened():
        print("Error: Camera not found.")
        return

    print("Color Recognition started.")
    print("Press Q or ESC to exit.")

    while True:
        success, frame = camera.read()

        if not success:
            print("Error: Cannot read camera frame.")
            break

        # Flip the image horizontally like a mirror
        frame = cv2.flip(frame, 1)

        # Convert the image from BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # -----------------------------
        # Blue color range
        # -----------------------------
        lower_blue = np.array([100, 100, 50])
        upper_blue = np.array([140, 255, 255])

        blue_mask = cv2.inRange(
            hsv,
            lower_blue,
            upper_blue
        )

        # -----------------------------
        # Green color range
        # -----------------------------
        lower_green = np.array([40, 70, 50])
        upper_green = np.array([85, 255, 255])

        green_mask = cv2.inRange(
            hsv,
            lower_green,
            upper_green
        )

        # -----------------------------
        # Red color ranges
        # Red requires two HSV ranges
        # -----------------------------
        lower_red_1 = np.array([0, 100, 50])
        upper_red_1 = np.array([10, 255, 255])

        lower_red_2 = np.array([170, 100, 50])
        upper_red_2 = np.array([179, 255, 255])

        red_mask_1 = cv2.inRange(
            hsv,
            lower_red_1,
            upper_red_1
        )

        red_mask_2 = cv2.inRange(
            hsv,
            lower_red_2,
            upper_red_2
        )

        red_mask = cv2.bitwise_or(
            red_mask_1,
            red_mask_2
        )

        # Remove noise from masks
        blue_mask = clean_mask(blue_mask)
        green_mask = clean_mask(green_mask)
        red_mask = clean_mask(red_mask)

        # Detect colors and draw rectangles
        detect_color(
            frame,
            blue_mask,
            "Blue",
            (255, 0, 0)
        )

        detect_color(
            frame,
            green_mask,
            "Green",
            (0, 255, 0)
        )

        detect_color(
            frame,
            red_mask,
            "Red",
            (0, 0, 255)
        )

        # Add project title and exit instructions
        cv2.putText(
            frame,
            "Real-Time Color Recognition",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "Detecting: Red, Green, Blue",
            (10, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "Press Q or ESC to exit",
            (10, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        # Combine all color masks into one window
        combined_mask = cv2.bitwise_or(
            blue_mask,
            green_mask
        )

        combined_mask = cv2.bitwise_or(
            combined_mask,
            red_mask
        )

        # Display windows
        cv2.imshow(
            "Color Recognition",
            frame
        )

        cv2.imshow(
            "Detected Colors Mask",
            combined_mask
        )

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q") or key == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

    print("Program closed successfully.")


if __name__ == "__main__":
    main()
