cin = open("in.txt")
cout = open("out.txt" , "w")
TestCase = cin.readline()
for CaseNumber in range(1 , int(TestCase)+1):
    P = {}
    N = cin.readline()
    array = cin.readline().split()
    for i in range(1 , int(N)+1):
        P[i] = int(array[i-1])
    ans = 0
    for i in range(1 , int(N)+1):
        t , cnt = i , 0
        while t != 0:
            last = t
            t = P[t]
            P[last] = 0
            cnt += 1
        if cnt > 2:
            ans += cnt - 1  
    cout.write("Case #" + str(CaseNumber) + ": " + str(ans) + "\n")
cin.close()
cout.close()
