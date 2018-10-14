f = open('A-small-attempt5.in')
x = []
out = open('out','w')
z = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
count = 1
f.readline()
for i in f :
    s = 'Case #'+str(count) + ': '
    count += 1
    for j in i:
        if j != ' ' and j != '\n' and j != '\r' : s += z[j]
        else : s+= j
    out.write(s)


out.close()
    
