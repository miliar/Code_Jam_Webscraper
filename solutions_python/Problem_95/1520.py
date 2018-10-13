#!/bin/env python
""" docstring """
import sys
import os
import argparse
import logging
import subprocess
_folder_path = os.path.split(os.path.abspath(__file__))[0]
sys.path.append(_folder_path)




def main():
    parser = argparse.ArgumentParser(description='docstring')
    parser.add_argument('infile')
    parser.add_argument('outfile')
    args = parser.parse_args()

    mapping = {}

    encoded_seqs = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
                    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                    "de kr kd eoya kw aej tysr re ujdr lkgc jv",
                    "z"]
    decoded_seqs = ["our language is impossible to understand",
                    "there are twenty six factorial possibilities",
                    "so it is okay if you want to just give up",
                    "q"]
    for i, eseq in enumerate(encoded_seqs):
        dseq = decoded_seqs[i]
        for j in range(len(eseq)):
            mapping[eseq[j]] = dseq[j]

    mapping["q"] = "z"

    for pair in sorted(mapping.items(), key=lambda x: x[0]):
        print pair


    with open(args.infile, "r") as inf:
        with open(args.outfile, "w") as outf:
            lines = inf.readlines()
            lines = lines[1:]
            for index, line in enumerate(lines):
                line = line.strip()
                decoded_line = "".join(map(lambda c: mapping[c], list(line)))
                write_line = "Case #%s: %s\n" % (index+1, decoded_line)
                print write_line
                outf.write(write_line)







if __name__ == '__main__':
    main()
