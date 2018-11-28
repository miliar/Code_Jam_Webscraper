
def Check(num):
    lst = list(str(num))
    flag = 1
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            flag = 0
            break
    if flag == 0 :
        return 0
    else:
        return num
text_file = open("B-small-attempt4.in", "r")
lines = text_file.read().split('\n')
tc = int(lines[0])
for i in range(1,tc+1):
    n = int(lines[i])
    while True:
        res = Check(n)
        if res == 0:
            n = n-1
        else:
            break
    with open('new.in', 'a') as f1:
        result = "Case #"+str(i)+": "+str(res)
        f1.write(result+"\n")