#!/bin/python3

from datetime import datetime

import click
import hashlib
import os
import shutil

def md5(input):
    return hashlib.md5(input.encode()).hexdigest()

def file_ending(input):
    return input.split(".")[-1]

def now_replaced():
    return datetime.now().isoformat().replace(":", "-")[:19]

def new_filename(input):
    ending = file_ending(input)
    return f"{now_replaced()}-{md5(input)}.{ending}"

def transform_folder_content(input_path):
    files = [
        os.path.join(input_path, f) for f in os.listdir(input_path) if 
        os.path.isfile(os.path.join(input_path, f)) and
        file_ending(f) in ["jpg", "png", "gif", "jpeg"]
    ]
    return files

@click.command()
@click.option("--input", required = True, help="Folder/File for input")
@click.option("--output", required = False, default="content/posts/gallery/images", help="Output folder")
def main(input, output):
    input_path = os.path.abspath(input)
    output_path = os.path.abspath(output)

    input_files = []
    if os.path.isfile(input_path):
        input_files = [input_path]
    elif os.path.isdir(input_path):
        input_files = transform_folder_content(input_path)
    else:
        print("The provided input path does not exist.")
        exit(1)
    
    print(f"Files found: {input_files}")

    if not os.path.isdir(output):
        print("Provided value for output is no directory")
        exit(1)

    for f in input_files:
        shutil.copy(f, os.path.join(output, new_filename(f)))


if __name__ == "__main__":
    main()