dic={' ':' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
print len(dic)
f=open('result.txt','w')
i=0
for line in open('A-small-attempt1.in','r'):
    i+=1
    b=[]
    for letter in line.strip():
        b.append(dic[letter])
    f.write('Case #'+str(i)+': '+''.join(b)+'\n')
    b=[]
print 'OK, finished!'
            
    
