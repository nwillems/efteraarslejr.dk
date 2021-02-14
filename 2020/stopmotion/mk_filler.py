#!/bin/env python

import argparse
import random
import tempfile
import os
import ffmpeg

parser = argparse.ArgumentParser(description="Create an awesome video sequence")
parser.add_argument("images", nargs="+", help="The images which will form the video")

args = parser.parse_args()

temp_dir = tempfile.TemporaryDirectory()
converted = []
for image in args.images:
    output_filename = "{}.mov".format(image).replace("/", "_")
    output_path = os.path.join(temp_dir.name, output_filename)
    ffmpeg.input(image, r=2, f="image2").output(output_path, r=30).run()

    converted.append(output_path)

partitions = [random.sample(converted, 4) for i in range(len(converted))]
streams = [ffmpeg.input(image) for partition in partitions for image in partition]

s = ffmpeg.concat(*streams)
s = s.output("herp.mov", r=30)
print(s.get_args())
s.run()
