f = open('A input.in','r')
a = f.read()
f.close()
b = a.split('\n')
del(b[-1])

def key():
    d = {}
    #d[' '] = ' '
    d['z'] = 'q'
    d['q'] = 'z'
    for i in range(len(plain)):
        #if plain[i] == ' ':
        #    continue
        d[plain[i]] = cipher[i]        
    return d

def solve(x):
    d = key()
    s = ''
    for i in range(len(x)):
        for j in d.keys():
            if d[j] == x[i]:
                s = s + j
            
    return s    
    

plain1 = 'our language is impossible to understand'
plain2 = 'there are twenty six factorial possibilities'
plain3 = 'so it is okay if you want to just give up'

cipher1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
cipher2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
cipher3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

plain = plain1 + plain2 + plain3
cipher = cipher1 + cipher2 + cipher3


g = open('A Out.txt','w')
N = int(b[0])
for i in range(1,N+1):
    x = solve(b[i])
    s = "Case #"+str(i) + ': '+ x + '\n'
    g.write(s)

g.close()
