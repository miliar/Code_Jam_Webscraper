def subtract(num, idx):
    if num[idx] != 0:
        num[idx] -=1
        return num
    else:
        num[idx] = 9
        return subtract(num, idx-1)

t = int(raw_input())

for case in range(1, t+1):

    num = map(int,list(raw_input()))

    for i in range(len(num)-1, 0, -1):
        if num[i] < max(num[:i]):
            num[i:] = [9 for j in range(len(num) - i)]
            num = subtract(num, i-1)

    num=int(''.join(map(str,num)))        
    print "Case #%s: %s" % (case, num)
