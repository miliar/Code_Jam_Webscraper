#!/usr/bin/env python3

import sys, io

def main(fname):
    with io.open(fname, "r") as f:
        t = int(f.readline())

        for i, line in enumerate(f.readlines()):
            args = line.strip().split(" ")
            state = args[0]
            k = int(args[1])
            print("Case #{}: {}".format(i + 1, num_flips(state, k)))

def num_flips(state, k):
    index = 0
    flips = 0
    while index <= len(state) - k:
        if state[index] == "-":
            if flip_possible(state, k, index):
                state = flip(state, k, index)
                flips += 1
            else:
                return "IMPOSSIBLE"
        index += 1

    if "-" not in state:
        return str(flips)
    else:
        return "IMPOSSIBLE"

def flip(state, k, index):
    result = state[:index]
    for i in range(k):
        result += "+" if state[index + i] == "-" else "-"
    result += state[index + k:]
    return result

def flip_possible(state, k, index):
    if len(state) - index >= k:
        return True
    else:
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: pancake_flipper.py input_file")
        exit(1)
    main(sys.argv[1])
