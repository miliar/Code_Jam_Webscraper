data = open('A-large.in','r')
d = open('A-large.out','w')

cases = int(data.readline());count = 1

while (count <= cases):
    pan,flips = data.readline().split();flips = int(flips);pank = []
    for x in range(len(pan)):
        if pan[x] == '-': pank.append(-1)
        else: pank.append(+1)
    ans,count_1 = 0,0
    while((count_1 + flips) <= len(pank)):
        if pank[count_1] == -1 :
          pank[count_1:count_1+flips] = [ pank[x]*(-1) for x in range(count_1,(count_1+flips))]
          ans += 1
        count_1 += 1
    if sum(pank) == len(pank): print >>d,('Case #' + str( count) + ': ' + str(ans))
    else: print >>d,('Case #' + str( count) + ': ' + 'IMPOSSIBLE')
    count += 1
d.close()
