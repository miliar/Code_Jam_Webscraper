fp = open('out.txt',"w")
for i in range(input()):
    num = raw_input()
    l = [int(j) for j in num]
    length = len(l)
    if length > 1:
        j = 1;k=0
        while(j < length):
            if l[k] > l[j]:
                l[k] -= 1
                k += 1
                num = str(int(''.join(map(str,l[:k])) + '9'*(length - k)))
                break 
            elif l[k] != l[j]:
                k = j
            j += 1
    print ('Case #{}: '+num+'\n').format(i+1)
    fp.write (('Case #{}: '+num+'\n').format(i+1))
fp.close()