# Bioinformatics Project: Analysis Script
# Import necessary libraries (if needed)

def clean_sequence(sequence):
    """
    Cleans the sequence by removing unwanted characters like BOM, null bytes, and newlines.
    Ensures the sequence contains only valid DNA bases (A, T, C, G).
    """
    sequence = sequence.replace('\ufeff', '')  # Remove BOM marker
    sequence = sequence.replace('\x00', '')    # Remove null byte
    sequence = sequence.replace('\n', '')      # Remove newline characters
    sequence = ''.join([base.upper() for base in sequence if base.upper() in 'ATCG'])  # Keep only valid DNA bases
    return sequence

def read_sequence(file_name):
    """
    Reads the DNA sequence from the provided text file.
    """
    with open(file_name, 'r') as file:
        return file.read().strip()

def gc_content(sequence):
    """
    Calculates the GC content (percentage of G and C in the sequence).
    """
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

def reverse_complement(sequence):
    """
    Generates the reverse complement of the DNA sequence.
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in sequence[::-1])

def transcription(sequence):
    # This function transcribes the DNA sequence to mRNA (T -> U)
    return sequence.replace('T', 'U')

# Main function to perform analysis
if __name__ == "__main__":
    # Specify the file name containing the DNA sequence
    file_name = "sample_sequence.txt"
    
    # Read the DNA sequence from the file
    sequence = read_sequence(file_name)
    
    # Clean the sequence to remove unwanted characters
    sequence = clean_sequence(sequence)
    
    # Print the original (cleaned) sequence
    print("Original Sequence:", sequence)
    
    # Calculate and print the GC content
    print("GC Content: {:.2f}%".format(gc_content(sequence)))
    
    # Calculate and print the reverse complement of the sequence
    print("Reverse Complement:", reverse_complement(sequence))

     # Transcription (DNA to mRNA)
    mRNA = transcription(sequence)
    print("Transcribed mRNA:", mRNA)
