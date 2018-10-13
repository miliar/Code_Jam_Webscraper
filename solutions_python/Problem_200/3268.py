count = 1
lengt = int(input())
for i in range(lengt):
    num = list(input())
    l = len(num)
    for i in range(len(num)):
        if (i == len(num) - 1):
            break
        if (num[l - i - 1] < num[l - i - 2]):
            for j in range(i+1):
                num[l - j - 1] = '9'
            if (num[l - i - 2] == '0'):
                num[l - i - 2] = '9'
            else:
                num[l - i - 2] = str(int(num[l - i - 2]) - 1)
            
        
    print("Case #" + str(count) + ": " + str(int(''.join(num))))
    count += 1


