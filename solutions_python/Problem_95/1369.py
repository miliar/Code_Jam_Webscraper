d = {' ': ' ', 'y': 'a', 'n': 'b', 'f': 'c', 'i': 'd', 'c': 'e', 'w': 'f', 'l': 'g', 'b': 'h', 'k': 'i', 'u': 'j', 'o': 'k', 'm': 'l', 'x': 'm', 's': 'n', 'e': 'o', 'v': 'p', 'z': 'q', 'p': 'r', 'd': 's', 'r': 't', 'j': 'u', 'g': 'v', 't': 'w', 'h': 'x', 'a': 'y', 'q': 'z'}

n = int(raw_input(''))
for i in range(1, n+1):
    s = raw_input()
    o = ''
    for c in s:
        
        o += d[c]

    print 'Case #' + str(i) + ': ' + o
