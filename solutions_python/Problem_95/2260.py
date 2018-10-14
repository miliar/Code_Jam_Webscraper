import sys
mapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
f = open(sys.argv[1]).read().split('\n')[1:]
g = open('out.txt','w')
n = 1
out_str = ''
for line in f:
   out_str += "Case #"+str(n)+": "+(''.join(mapping[x] for x in line))+"\n"
   n += 1
g.write(out_str.strip())
g.close()
