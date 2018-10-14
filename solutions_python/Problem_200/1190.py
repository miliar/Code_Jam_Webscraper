data = open('B-large.in','r')
d = open('B-large.out','w')

cases = int(data.readline())
for j in range(cases):
    num = [int(x) for x in str(int(data.readline()))]
    for i in range(len(num) -1):
        if num[i] > num[i+1] and num[i] == 1:
            num = [ 9 for x in range(len(num))];num[0] = 0
        elif num[i] > num[i+1]:
            for k in range(len(num)):
                if num[k] == num[i]:
                    num[k] -= 1;num[k+1:] = [ 9 for x in range(k+1,len(num))]
                    break
    ans = int("".join(str(x) for x in num))
    print >>d,('Case #' + str(j+1) + ': ' + str(ans))
d.close()
