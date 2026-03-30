# Document Scanner (OpenCV + Python)

A command-line and web-based document scanner that converts images into clean, perspective-corrected PDF documents using Computer Vision techniques.

## Features

-  Detects document edges automatically  
-  Applies perspective transformation (top-down scan)  
-  Converts scanned output into PDF  
-  CLI-based execution (as required)  
-  Optional Streamlit web interface  

## Tech Stack

- Python  
- OpenCV  
- NumPy  
- Streamlit  
- img2pdf  


## Project Structure

```

document-scanner/
│
├── scanner/
│   └── scan.py           # Core scanning logic
│
├── webapp/
│   └── streamlit_app.py  # Web interface
│
├── outputs/              # Generated outputs
├── main.py               # CLI entry point
├── requirements.txt
└── README.md

````


## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/document-scanner.git
cd document-scanner
````

Install dependencies:

```bash
pip install -r requirements.txt
```


## Usage (CLI - IMPORTANT)

Run the scanner from terminal:

```bash
py main.py --input test.jpg --output result.pdf
```

### Arguments:

* `--input` → Path to input image
* `--output` → Output PDF file


## Usage (Streamlit UI - Optional)

```bash
streamlit run webapp/streamlit_app.py
```

## How It Works

1. Convert image to grayscale
2. Apply edge detection (Canny)
3. Find contours and detect largest quadrilateral
4. Apply perspective transform
5. Enhance and save as scanned output


## Limitations

* Requires clear document boundaries
* Performance decreases with cluttered backgrounds
* Handwritten text is not optimized


## Future Improvements

* OCR integration for text extraction
* Multi-page PDF generation
* Automatic edge enhancement
* Mobile-friendly interface


## Conclusion

This project demonstrates the application of Computer Vision techniques to solve a real-world problem of document digitization. It integrates image processing, transformation, and file generation into a complete working pipeline.


## Author

Priyam Kundu
B.Tech CSE (AIML)

