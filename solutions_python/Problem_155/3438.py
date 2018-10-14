j = open('A-small-attempt2.out' , 'w')
with open('A-small-attempt2.in') as f:
    content = f.readlines()
    content.pop(0)
    a=0
    for c in content:
        a+=1
        z=0
        x = c[0]
        e = list(c)
        ##e = [int(i) for i in a]
        w=0
        y=0
        for r in e[2:-1]:
            p = int(r)
            if p==0:
                w+=1
            else:
                
                if y>=w:
                    w+=1
                else:
                    b=w-y
                    w+=1
                    z+= b
                    y+= b
            y+=int(r)
        
        j.write('Case #'+ str(a) + ': ' + str(z))
        j.write('\n')
j.close()
        


