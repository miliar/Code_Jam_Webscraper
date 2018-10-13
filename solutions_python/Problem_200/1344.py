import sys

testnum = int(input().strip())

for k in range(testnum):
    num = input().strip()
    num_length = len(num)
    if num_length > 1:
        num = list(num)
        d = 0
        i = 0

        while i < num_length-1:
            if int(num[i]) > int(num[i+1]):
                num[i] = str(int(num[i]) - 1)
                break
            i = i+1

        for j in range(i+1, num_length, 1):
            num[j] = '9'

        while i > 0:
            if int(num[i]) >= int(num[i-1]):
                break
            else:
                num[i] = '9'
                num[i-1] = str(int(num[i-1]) -1)
                i = i-1

        #print("Case #"+str(k+1)+": "+str(int(''.join(str(e) for e in num))))
        print("Case #"+str(k+1)+": "+str(int(''.join(num))))
    else:
        print("Case #"+str(k+1)+": "+str(num))

