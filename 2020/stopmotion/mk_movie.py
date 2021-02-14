#!/bin/env python

import argparse
import random
import tempfile
import os
import ffmpeg

parser = argparse.ArgumentParser(description="Create an awesome video sequence")
parser.add_argument("glob", help="A glob for the image sequence")

args = parser.parse_args()

s = ffmpeg.input(args.glob, r=4, f="image2")
s = s.output("movie.mov", r=30)
print(s.get_args())
s.run()
