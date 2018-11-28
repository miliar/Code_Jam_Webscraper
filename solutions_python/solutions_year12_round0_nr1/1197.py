import sys
with open(sys.argv[1]) as fp:
    T=int(fp.readline())
    mapping={'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd',
             'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z',
             'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a',
             'x': 'm', 'z': 'q',' ':' ','\n':'\n'}
    for i in range(1,T+1):
        sys.stdout.write("Case #{0}: {1}".format(i,"".join(mapping[e] for e in fp.readline())))
