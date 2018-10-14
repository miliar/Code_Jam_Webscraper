data = {
    'y': 'a',
    'n': 'b',
    'f': 'c',
    'i': 'd',
    'c': 'e',
    'w': 'f',
    'l': 'g',
    'b': 'h',
    'k': 'i',
    'u': 'j',
    'o': 'k',
    'm': 'l',
    'x': 'm',
    's': 'n',
    'e': 'o',
    'v': 'p',
    'z': 'q',
    'p': 'r',
    'd': 's',
    'r': 't',
    'j': 'u',
    'g': 'v',
    't': 'w',
    'h': 'x',
    'a': 'y',
    'q': 'z',
    ' ': ' ',
    '\n': '' 
    }
f = open('A-small-attempt0.in')
n = int(f.readline())
l = []

for i in range(n):
    l.append(f.readline())

p = open('output_small.txt', 'w')
p.close()

for i in range(n):
    l[i] = [data[s] for s in l[i]]
    p = open('output_small_attemp0.txt', 'a')
    print >> p, "Case #"+str(i+1)+": "+''.join(l[i])
    print "Case #"+str(i+1)+": "+''.join(l[i])
    p.close()
