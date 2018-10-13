import sys

lang = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q':'z', 'z':'q'}
a = raw_input()
input = dict()

for i in range(int(a)):
    input[i] = raw_input()

for i in input:
    sys.stdout.write("Case #")
    j = str(i + 1)
    sys.stdout.write(j)
    sys.stdout.write(": ")
    [sys.stdout.write(lang[ch]) for ch in input[i]]
    print
