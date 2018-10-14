di = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', ' ': ' '}

i = int(raw_input())
for x in range(1, i+1):
    s = raw_input()
    #print s
    fin = ''
    for t in s:
        fin = fin + di[t] 
    print 'Case #{0}: {1}'.format(x, fin)
    

