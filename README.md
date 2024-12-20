# Bioinformatics Project: DNA Analysis Script

## Overview
This project is a DNA analysis tool implemented in Python. It provides several functions for processing and analyzing DNA sequences. The main features include:
- Cleaning the sequence to remove unwanted characters.
- Calculating the GC content (percentage of G and C bases).
- Generating the reverse complement of the DNA sequence.
- Transcribing the DNA sequence into mRNA.

The project is designed to work with DNA sequence data stored in text files.

## Features
- **Clean Sequence**: Removes invalid characters like BOM markers, null bytes, and newline characters.
- **GC Content**: Calculates the GC content, which is the percentage of Guanine (G) and Cytosine (C) bases in the sequence.
- **Reverse Complement**: Generates the reverse complement of the DNA sequence, which is important for various bioinformatics applications.
- **Transcription**: Converts the DNA sequence into its corresponding mRNA sequence by replacing Thymine (T) with Uracil (U).

## Prerequisites
- Python 3.x
- No external dependencies are required for this basic version of the project. However, you may need additional libraries like `numpy` or `biopython` if you plan to extend functionality.

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Pritika-10/Bioinformatics-Projects.git
   ```
   
2. **Navigate to the project directory**:
   ```bash
   cd Bioinformatics-Projects
   ```

3. **Create a Python virtual environment (optional)**:
   If you want to use a virtual environment, create one using:
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

## Running the Script
1. Ensure that you have a text file (`sample_sequence.txt`) containing a DNA sequence in the same directory as the script.
   
2. Run the Python script:
   ```bash
   python dna_analysis.py sample_sequence.txt
   ```

3. **Expected Output**:
   - The script will output the cleaned DNA sequence.
   - It will calculate and print the GC content (as a percentage).
   - It will generate and print the reverse complement of the DNA sequence.
   - It will transcribe the DNA sequence into mRNA.

### Example:
   ```bash
   Original Sequence: ATGCGTACGTAGCTAGCGT
   GC Content: 50.00%
   Reverse Complement: TACGCATGCATCGATCGCA
   Transcribed mRNA: AUGCGUACGUAGCUAGCGU
   ```

## File Structure
The repository contains the following files:
- `dna_analysis.py`: The Python script for DNA analysis.
- `sample_sequence.txt`: A sample text file containing a DNA sequence (modify as needed for your input).
- `README.md`: Documentation for the project.

## License
This project is open-source and available under the MIT License.

