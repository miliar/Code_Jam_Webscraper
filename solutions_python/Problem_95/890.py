import sys

#code =  "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
#plain = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
#for i in xrange(len(code)):
#    d[code[i]] = plain[i]

N = int(sys.stdin.readline())

d = {' ': ' ', 'q': 'z', 'z': 'q', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}

for i in xrange(N):
    code = sys.stdin.readline().strip()
    solution = ""
    for letter in code:
        solution += d[letter]

    print "Case #%d: %s" % (i+1, solution)



