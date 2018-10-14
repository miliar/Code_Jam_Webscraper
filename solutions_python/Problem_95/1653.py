table ={' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

incoming = open('A.in')
output = open('A.out','w')
a = int(incoming.readline())

for i in range(1,a+1):
    x = incoming.readline().rstrip()
    output.write("Case #%d: " % i)
    output.write(''.join(table[t] for t in x) + '\n')
    
incoming.close()
output.close()
