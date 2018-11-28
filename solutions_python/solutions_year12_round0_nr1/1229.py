import sys
decrypt_map = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def build_decrypt_map(encrypted, decrypted):
    for e, d in zip(encrypted, decrypted):
        if e not in decrypt_map:
            decrypt_map[e] = d
    print len(decrypt_map)
    print decrypt_map

def decrypt(encrypted):
    dec = ""
    for e in encrypted:
        dec += decrypt_map[e]
    return dec

n = int(sys.stdin.readline())
for i in xrange(1, n+1):
    print "Case #" + str(i) + ": " + decrypt(sys.stdin.readline().strip())
