"""Script to batch compress jpgs in a specified folder to a predefined quality. 
Uses Pillow to manipulate images
Set the compression ratio, the input folder and the output folder to run.
Michael Robinson 2017"""


from PIL import Image
import os


COMPRESSION_RATIO = 60
INPUT_FOLDER = '/home/michael/PycharmProjects/photo_compress/input'
OUTPUT_FOLDER = '/home/michael/PycharmProjects/photo_compress/output'


def walk_input_folder():
    """Take the input folder and get a list of all the jpeg files in the folder"""
    res = []
    for dir_name, sub_dir_list, file_list in os.walk(INPUT_FOLDER):
        for file_name in file_list:
            print('\t%s' % file_name)
            if '.jpg' in file_name or '.jpeg' in file_name.lower():
                path = os.path.join(dir_name,file_name)
                res.append(path)
    return res


def compress_image(path):
    """Take a file path, compress it and save to the output folder"""
    try:
        base_name = os.path.basename(path)
        print(path)
        output_name = 'compressed_' + base_name
        output_path = os.path.join(OUTPUT_FOLDER, base_name)
        im = Image.open(path)
        im.save(output_path, "JPEG", quality=COMPRESSION_RATIO)
        print('Sucessfully Compressed Image{} to path: {}'.format(base_name, output_path))
    except IOError:
        print("cannot create compressed image for", path)
        raise


def main():
    files = walk_input_folder()
    [compress_image(file_name) for file_name in files]

if __name__ == '__main__':
    main()