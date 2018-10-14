a = {' ': ' ', 'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

t = input()
def maph(f):
    r = ""
    for i in f:
        r += a[i]
    return r

for i in range(1,t+1):
    s = str(raw_input())
    print "Case #" + str(i) + ": " + maph(s)
    
    
