a = open('A-small-attempt0.in','r')
n = eval(a.readline().strip())

b = open('output.txt','w')

d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u',
     'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def fun(s):
    l = ''
    for i in s:
        l = l+d[i]
    return(l)

for i in range(1,n+1):
    s = a.readline().strip()
    b.write('Case #'+str(i)+': '+ fun(s)+'\n')


b.close()
a.close()
