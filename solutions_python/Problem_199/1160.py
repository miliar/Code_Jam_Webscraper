data = open('A-large.in','r')
d = open('A-large.out','w')
tc = int(data.readline())
for t in range(tc):
    count = 0
    pan, numb = data.readline().split()
    pan = list(pan)
    numb = int(numb)
    for i in range(len(pan)):        
        if pan[i] == '-':
            count += 1
            if i + numb > len(pan):
                count = "IMPOSSIBLE"
                break
            else:
                for j in range(numb):
                    if pan[i+j] == '-': pan[i+j] = '+'
                    else: pan[i+j] = '-'
    print >>d,("Case #" +str(t+1) + ": " + str(count))
d.close()
