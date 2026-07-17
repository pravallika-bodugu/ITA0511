import cv2

# 1. Read the image directly from the folder
img = cv2.imread('image1.png')

# Check if the image loaded properly
if img is None:
    print("Error: Could not find 'image1.png'. Make sure it is pasted inside the folder!")
else:
    # 2. Convert the image to Grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Show both original and grayscale images on screen
    cv2.imshow('Original Color Image', img)
    cv2.imshow('Grayscale Output Image', gray_img)

    # 4. Save the grayscale image as a new file
    cv2.imwrite('gray_image.png', gray_img)

    # 5. Wait until you press any key, then close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
