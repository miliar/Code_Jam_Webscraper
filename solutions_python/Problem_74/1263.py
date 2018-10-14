#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback
import re


def process(args):
    try:
        count = int(args.input.readline())
        for index, line in enumerate(args.input, 1):
            sep = re.compile(r"([OB]) (\d+)")
            m = re.findall(sep, line)
            O=[1,]
            B=[1,]
            omoves = 0
            bmoves = 0
            for i in m:
                if i[0] == 'O':
                    omoves+=abs(int(i[1])-O[-1])+1
                    if omoves <= bmoves:
                        omoves = bmoves+1
                    O.append(int(i[1]))
                else:
                    bmoves+=abs(int(i[1])-B[-1])+1
                    if bmoves <= omoves:
                        bmoves = omoves+1
                    B.append(int(i[1]))
            tempmoves = max(omoves,bmoves)
            print "Case #%d: %d" %( index , tempmoves)
    except Exception:
        traceback.print_exc()
        return 2
    except BaseException:
        traceback.print_exc()
        return 1


def main(args):
    sys.exit(process(args))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=argparse.FileType('r'))
    main(parser.parse_args())
