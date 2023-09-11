import easyocr
import cv2

image = cv2.imread("dokumen.jpg")
images = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
reader = easyocr.Reader(['en'])

results = reader.readtext(image,width_ths=20.0,height_ths=20.0, slope_ths=2.0)

for (bbox, text, prob) in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    
    # Gambar bounding box dan teks pada gambar
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(image, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    print(text)

# Tampilkan gambar hasilnya
cv2.imshow('Hasil OCR', image)
cv2.waitKey(0)

    
