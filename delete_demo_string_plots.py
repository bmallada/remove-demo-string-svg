import re
import sys
import os

def remove_demo_from_svg(input_filename):
    # Check if the input file exists
    if not os.path.isfile(input_filename):
        print(f"File '{input_filename}' does not exist.")
        return

    # Read the content of the input SVG file
    with open(input_filename, 'r') as f:
        svg_content = f.read()

    # Define the pattern to match the text 'demo' and the content around it
    pattern = re.compile(r'<[^>]*>[^<]*demo[^<]*</tspan></tspan></text>', re.IGNORECASE)

    # Remove the matched content from the SVG
    modified_svg_content = re.sub(pattern, '', svg_content)

    # Create an output filename based on the input filename
    output_filename = os.path.splitext(input_filename)[0] + '_no_demo.svg'

    # Write the modified content to the output SVG file
    with open(output_filename, 'w') as f:
        f.write(modified_svg_content)

    print(f"Content around 'demo' has been removed and saved to '{output_filename}'.")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python your_script.py <filename>")
        sys.exit(1)

    # Get the filename from the command-line argument
    input_filename = sys.argv[1]

    remove_demo_from_svg(input_filename)
