mapping = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm', 'y': 'a', 'z': 'q', ' ': ' '}

def Googlerese(G):
    S = ''
    for i in range(0, len(G)):
        S = "%s%s" % (S, mapping[G[i]])
    return S

T = input()
for i in range(0, T):
    G = raw_input()
    print "Case #%s: %s" % (i + 1, Googlerese(G))
