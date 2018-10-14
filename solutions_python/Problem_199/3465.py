#!/usr/bin/env python3


def flip_substring(string):
    new_string = ""
    for char in string:
        if char == "+":
            new_string += "-"
        elif char == "-":
            new_string += "+"
    return new_string


def flip_first(string, size, count=0):
    while True:
        pos = string.find("-")
        if pos + size > len(string):
            return "IMPOSSIBLE"
        elif pos + size == len(string) and string[pos:pos+size] != "-" * size:
            return "IMPOSSIBLE"
        elif pos == -1:
            return count
        string = string[:pos] + flip_substring(string[pos:pos+size]) + string[pos+size:]
        count += 1


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        tstring, k = input().rstrip().split()
        print("Case #{0}: {1}".format(i, flip_first(tstring, int(k))))
