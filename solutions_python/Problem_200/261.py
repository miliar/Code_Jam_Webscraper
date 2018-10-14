def solve(num):
    jj = -1
    for i in range (len(num)):
        for j in range(i):
            if int(num[j]) > int(num[i]):
                jj = j
        if jj != -1:
            j = jj
            new_num = int(num[:j+1])-1
            if new_num <= 0:
                new_num = ""
            else:
                new_num = str(new_num)
            new_num += ('9' * (len(num)-j-1))
            return False,new_num
    return True,num




f = open("C:\\Users\\TocarIP\\Google Drive\\Downloads\\B-large.in")
lines = f.readlines()
numcases = int(lines[0])
i = 1
while i <= numcases:
    num = lines[i].strip()
    res = "Case #" + str(i) + ": "
    while True:
        ok,new_num = solve(num)
        num = new_num
        if ok:
            break
    print (res + num)
    i = i+ 1