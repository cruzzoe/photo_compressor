# photo_compressor
Take a folder containing JPGs and compresses them to a pre-defined ratio to reduce file size.

Instructions:

* Before starting the steps below, open a command line and navigate to the folder that contains the script compress.py.
* Enter: python compress.py -h to see the help

1. Add in arguments 'input folder'. This is where you copy the photos to.
2. Set your compression ratio. Higher compression = lower file size and lower quality.

e.g To run the script type at 50% compression: python compress.py '/home/my_input_folder' 50

After running, the output in the command line will show each picture that has been compressed.
The compressed images will go to a subfolder of the input folder called output.

Requirements:
* Pictures must be in jpeg or jpg format.
* Python 3 needs to be installed.
* pillow library is required.

Appendix
*Uses pillow (a derivation from PIL libray).