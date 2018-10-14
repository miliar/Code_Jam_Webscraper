import sys

dict = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q' : 'z', 'z' : 'q'}

f = open(sys.path[0] + "//A-small-attempt0.in").readlines()
N = int(f.pop(0))

for i in range(N):
    line = f[i].strip()
    rez = ""
    for j in line:
        rez += dict[j]
    print "Case #" + str(i+1) + ": " + rez