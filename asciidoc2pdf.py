#!/usr/bin/env python3

import os
import sys
import subprocess
import glob


guide_dir = os.path.dirname(os.path.realpath(__file__))


args = {
    "out": "out",
    "pdf-font-dir": f"pdf-fontsdir={guide_dir}/themes/fonts",
    "pdf-theme": f"pdf-theme={guide_dir}/themes/guides.yml",
}


command = [
    "asciidoctor",
    "--trace",
    "--destination-dir", args["out"],
    "--attribute", args["pdf-font-dir"],
    "--attribute", "allow-uri-read",
    "--attribute", args["pdf-theme"],
    "--require", "asciidoctor-pdf",
    "--backend", "pdf"
]


if len(sys.argv) == 1:
    x = glob.glob("*.adoc")
else:
    x = sys.argv[1:]


for i in x:
    command.append(i)

    subprocess.run(
        command,
        shell=True,
        check=True
    )


