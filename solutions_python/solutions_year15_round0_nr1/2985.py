#/usr/bin/python3

import argparse
import time
import sys
import fileinput
import timeit

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', "--filename", type=str,
                        help="specify a file for input")
    parser.add_argument('-s', "--stdin", help="read input from stdin",
                        action="store_true")
    return parser.parse_args()

def read_from_file(file_object):
    while True:
        data = file_object.readline().strip("\n").split(" ")
        if not data or data[0] == '':
            break
        yield data

def read_from_stdin():
    while True:
        data = sys.stdin.readline().strip("\n").split(" ")
        if not data or data[0] == '':
            break
        yield data

def solver(data):
    smax = int(data[0])
    if len(data) == 1:
        return 0
    applauding = 0
    counter = 0
    propaganda_people = 0
    while applauding < smax:
        if counter <= applauding:
            applauding += int(data[1][counter])
        elif int(data[1][counter]) == 0:
            pass
        else:
            propaganda_people += counter - applauding
            applauding += counter - applauding + int(data[1][counter])
        counter += 1
    return propaganda_people

def main():
    args = parse_arguments()
    counter = 0
    if args.stdin:
        for line in read_from_stdin():
            if counter > 0:
                pass
                print("Case #{0}: {1}".format(counter, solver(line)))
            counter += 1
    else:
        f = open(args.filename)
        for line in read_from_file(f):
            if counter > 0:
                print("Case #{0}: {1} ".format(counter, solver(line)))
            counter += 1
        f.close()

if __name__ == '__main__':
    main()
