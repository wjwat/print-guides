#!/usr/bin/env python3

import os
import sys
import subprocess
import glob


vars = {
    'density': '300',
    'background': 'rgba(0,0,0,0)',
    'foreground': 'Black',
    'fontsize': '16',
    'font': 'themes/fonts/IBMPlexMono-Regular.ttf',
    'linespacing': '-20'
}


convert_command = (
    "magick "
    "convert "
    f"-density {vars['density']} "
    f"-background {vars['background']} "
    #f"-transparent white "
    f"-fill {vars['foreground']} "
    f"-pointsize {vars['fontsize']} "
    f"-font {vars['font']} "
    f"-interline-spacing {vars['linespacing']} "
    "label:@- "
    f"-bordercolor {vars['background']} "
    "-border 10x10"
)


if len(sys.argv) == 1:
    x = glob.glob("*.ascii")
else:
    x = sys.argv[1:]


for i in x:
    convert_command = convert_command.split()
    convert_command.append(i+".png")

    with open(i) as in_file:
        proc = subprocess.run(
                convert_command,
                stdin=in_file,
                shell=True,
                check=True
        )

