a = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
aa = "our language is impossible to understand"

b = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
bb = 'there are twenty six factorial possibilities'

c = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
cc = 'so it is okay if you want to just give up'

d = {}

for i in range(len(a)):
    d[a[i]] = aa[i]

for i in range(len(b)):
    d[b[i]] = bb[i]
   
for i in range(len(c)):
    d[c[i]] = cc[i]
    
    
d['q'] = 'z'
d['z'] = 'q'
#d['\n'] = '\n'

def trans(s):
    ret = ""
    
    for i in s:
        ret += d[i]

    return ret

if __name__ == '__main__':
    f = open("A-small-attempt1.in",'r')
    num = f.readline()
    
    t = open('output.txt','w')
    
    for i in range(int(num)):
        s = f.readline()
        t.write("Case #" + str(i+1) + ": " + trans(s.strip())+"\n")
        
    f.close()
    t.close()
        
    