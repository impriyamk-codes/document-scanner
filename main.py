import argparse
import cv2
import img2pdf

from scanner.scan import scan_document

print("Running scanner...")

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--output", default="output.pdf")

args = parser.parse_args()

image = cv2.imread(args.input)

if image is None:
    print("Error: Image not loaded")
    exit()

# Scan document
scanned = scan_document(image)

# Save temp image
temp_image = "temp.jpg"
cv2.imwrite(temp_image, scanned)

# Convert to PDF
with open(args.output, "wb") as f:
    f.write(img2pdf.convert(temp_image))

print(f"Saved scanned document as PDF: {args.output}")