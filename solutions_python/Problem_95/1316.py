__author__ = 'Daria'
#creating the dictionary
d = {}
d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
d['q'] = 'z'
d['z'] = 'q'

#translating
res =  []
input = open ('/Users/Daria/PycharmProjects/CodeJam/input.txt','r')
N = int(input.readline())
k = 0
l = input.readlines()
input.close()
lines = []
for line in l:
    lines.append(line.strip())

output = open ('/Users/Daria/PycharmProjects/CodeJam/output.txt','w')
for line in lines:
    k += 1
    output.write('Case #%i: '%k)
    for s in line:
        output.write(d[s])
    output.write("\n")

output.close()