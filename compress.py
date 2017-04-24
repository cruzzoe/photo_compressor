"""
Script to batch compress Jpegs in a specified folder to a predefined quality. 
Uses Pillow to manipulate images
Set the compression ratio, the input folder and the output folder to run.
Michael Robinson 2017
"""

import argparse
from PIL import Image
import os


COMPRESSION_RATIO = 60
INPUT_FOLDER = '/home/michael/PycharmProjects/photo_compress/input'


def walk_input_folder(input_folder):
    """Take the input folder and get a list of the jpeg files in the folder"""
    res = []
    for dir_name, sub_dir_list, file_list in os.walk(input_folder):
        for file_name in file_list:
            print('\t%s' % file_name)
            if '.jpg' in file_name.lower() or '.jpeg' in file_name.lower():
                path = os.path.join(dir_name, file_name)
                res.append(path)
    return res


def compress_image(compression, path):
    """Take a file path, compress it and save to the output folder"""
    try:
        base_name = os.path.basename(path)
        dir_name = os.path.dirname(path)
        output_folder = os.path.join(dir_name, 'output')
        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, base_name)
        im = Image.open(path)
        im.save(output_path, "JPEG", quality=compression)
        print('Successfully compressed image{} to: {}'.format(base_name,
                                                              output_path))
    except IOError:
        print("cannot create compressed image for", path)
        raise


def main():
    parser = argparse.ArgumentParser(description='Compress some pictures.')
    parser.add_argument("input_folder",
                        help="Supply the folder for inputting \n"
                             "the uncompressed pictures.",
                        type=str)
    parser.add_argument("compression", help="Supply the compression ratio.",
                        type=int)
    args = parser.parse_args()
    files = walk_input_folder(args.input_folder)
    [compress_image(args.compression, file_name) for file_name in files]

if __name__ == '__main__':
    main()
