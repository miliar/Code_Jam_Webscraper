def maps(ip, op, dic):
    for i in range(len(ip)):
           if ip[i].isalpha():
               dic[ip[i]] =  op[i]
    return dic 

def translate(ip, dic):
    op = ''
    for i in range(len(ip)):
        if ip[i].isalpha():
            op = op + dic[ip[i]]
        else:
            op = op + ip[i]
    return op    

from sys import stdin
lines = open("A-small-attempt0.in").read().split('\n')
t=int(lines[0])
dic = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
for i in range(t):
    ip = lines[i+1]
    op = translate(ip, dic)
    print 'Case #%d: %s'%(i+1, op)


         
           
