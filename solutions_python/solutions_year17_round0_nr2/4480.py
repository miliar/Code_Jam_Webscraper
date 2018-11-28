
file = open("input2.txt" ,"r")
n = int(file.readline())
for a0 in range(n):
    print("Case #"+str(a0+1)+": ",end="")
    line = file.readline().strip()
    num = [int(line[i]) for i in range(len(line))]
    i = 1
    while i < len(num):
        if num[i-1] > num[i]:
            cur = i - 1
            num[cur] -= 1
            while i < len(num):
                num[i] = 9
                i += 1
            while cur > 0 and (num[cur]+1) == num[cur-1]:
                num[cur] = 9
                num[cur-1] -= 1
                cur -= 1

        else:
            i+=1
    if num[0] == 0:
        for i in range(1,len(num)):
            if num[i] == 0 :
                print(9,end="")
            else:
                print(num[i],end="")
    else:
        for i in range(len(num)):
            print(num[i],end="")
    print("")

