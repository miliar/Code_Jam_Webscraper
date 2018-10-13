f = open('A-small-attempt1.in','r')
inp = f.read().split('\n')
fi = open('1.txt','w')
for i in xrange(int(inp[0])):
    c = inp[1+10*i:1+10*(i+1)][int(inp[1+10*i])]
    d = inp[1+10*i:1+10*(i+1)][int(inp[6+10*i])+5]
    count = 0
    for e in c.split(' '):
        if e in d.split(' '):
            count += 1
            val = e
    if count == 0:
        fi.write('Case #'+str(i+1)+': '+ 'Volunteer cheated!')
    elif count ==1:
        fi.write('Case #'+str(i+1)+': '+ val)
    else:
        fi.write('Case #'+str(i+1)+': '+ 'Bad magician!')
    if i!=99:
        fi.write('\n')
fi.close()
