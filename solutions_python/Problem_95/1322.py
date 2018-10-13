#!/usr/bin/python

translator = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm', 'y': 'a', 'z': 'q'}

def main():
    with open('A-small-attempt0.in', 'r') as f:
        inp = f.readlines()

    cnt = int(inp[0])
    for lineIx in range(1, cnt + 1):
        line = ''
        for charIx in range(len(inp[lineIx])):
            key = inp[lineIx][charIx]
            if key != ' ' and key != '\n':
                line += translator[key]
            else:
                line += key
        with open('A-small-attempt0.out', 'a') as f:
            f.write('Case #' + str(lineIx) + ': ' + line)

main()
