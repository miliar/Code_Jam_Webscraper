ctable={' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q','\n': '\n'}
r=open('C:/Users/SJ/Downloads/infile.in','r')
out=[]
n = int(r.readline())
for i in range(0,n):
    text=r.readline()
    ans="Case #"+str(i+1)+": "
    for j in text:
        if i!='\n':
            ans=ans+ctable[j]
    out.append(ans)
r=open('C:/Users/SJ/Downloads/jam1.out','w')
for i in out:
    r.write(i)



    

    
    




    
