f = open('r11.in','r')
f2 = open('ro.txt','w')
total = f.readline()

for t in range(1, int(total)+1):
    txt = f.readline().split()
    name = txt[0]
    n = int(txt[1])
    count = 0
    prev = 0
    for i in range(len(name)-n+1):
        subStr = name[ i : i + n]
        if(('a'  in subStr or 'e'  in subStr or 'i'  in subStr or 'o'  in subStr or 'u' in subStr) == False):
            #print i-prev+1
            #print len(name)-i-n+1
            count = count + (i-prev+1)*(len(name)-i-n+1)
            prev = i+1
    result = 'Case #'+str(t)+': '+ str(count)
    print result
    f2.write(result+'\n')
    steps = 0
f.close()
f2.close()
