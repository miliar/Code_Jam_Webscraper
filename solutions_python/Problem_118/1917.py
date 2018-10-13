import math

f = open('third.txt')
datas = f.read().split('\n')
f.close()

nb = int(datas[0])

final = ''



for k in range(nb):
    #print('----------')
    count = 0
    count2 = 0

    x = int(datas[k + 1].split()[0])
    y = int(datas[k + 1].split()[1])

    #y = 10**100

    start = ''
    tmp = 0
    if x > 100:
        if (int(math.sqrt(x)) - 1) > 10:
            tmp = int(str(int(math.sqrt(x)) - 1)[:int(len(str(int(math.sqrt(x))))/2)]) - 1
    tmp = max(1, tmp)
    #print('TMP',tmp)
    other = 1
    while True:
        if other == 1:
            if len(str(tmp)) == 1:
                start = tmp
            else:
                start = int(str(tmp)+(str(tmp)[::-1][int(len(str(tmp))/2):]))
        elif other == 2:
            start = int(str(tmp)+(str(tmp)[::-1]))
        if other == 2:
            tmp += 1
            other = 1
        else:
            other += 1
        sq = start ** 2
        if sq < x:
            continue
        if sq > y and other == 2:
            #print('END', start, sq)
            break
        elif sq > y:
            continue
        ch = str(sq)
        if ch == ch[::-1]:
            count += 1
            #print(sq, start)

    final += 'Case #'+str(k+1)+': '+str(count)+'\n'

    
 #   for n in range(x, y+1):
#        if str(n) == str(n)[::-1]:
#            sqrt = int(math.sqrt(n))
#            if sqrt**2 == n and str(sqrt) == str(sqrt)[::-1]:
                #print(n, sqrt)
#                count2 +=1

    #print(count2)
    #if count != count2:
#        print('ERROR', count, count2, k)
#        break


print(final[:-1])
f = open('thirdr.txt', 'w')
f.write(final)
f.close()
