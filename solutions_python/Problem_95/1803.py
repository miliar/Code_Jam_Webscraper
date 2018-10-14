a = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

f = input()
n = int(f)

for i in range(n):
    f = input()
    s = ''
    l = len(f)
    for j in range(l):
        if f[j] == ' ':
            s += ' '
        else:
            s += a[f[j]]
    print('Case #{0}: '.format(i+1) + s)
    


