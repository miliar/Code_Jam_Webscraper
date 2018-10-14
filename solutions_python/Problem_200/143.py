filename = "C:\\Users\\Andri_000\\Downloads\\python\\codejam2017\\Round Qualification\\B\\B-large"


fin = open(filename+".in")
fout = open(filename+".out","w")
trials = int(fin.readline())

for T in xrange(trials):
    s = fin.readline().strip()

    flag = False
    ans = []
    
    for c in s:
        ans = ans + [int(c)]
    s = ans[:]
    
    while not flag:
        i = 0
        while (i < len(s) - 1 and s[i] <= s[i+1]):
            i += 1
    
        #print i
    
        if (i < len(s)-1):
            ans[i] -= 1
            j = i
            while (j > 1 and ans[j] < 0):
                ans[j] = 9
                ans[j-1] -= 1
                j -= 1
            
            for j in range(i+1, len(s)):
                ans[j] = 9
        else:
            flag = True
        s = ans[:]
        #print ans
    
    if len(ans) > 1:
        while ans[0] == 0:
            ans = ans[1:]
    fout.write("Case #{0}: {1}\n".format(T+1,"".join(map(str, ans))))
                    
fin.close()
fout.close()