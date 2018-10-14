ofile = open('Boutfile.txt','w')
TC = int(input())
for t in range(TC) :
    x = input().strip()
    if len(x) == 1 :
        #print(x)
        ofile.write("Case #" + str(t+1) + ": " + x+"\n")
    else :
        lst = []
        old = []
        for i in x :
            lst.append(int(i))
            old.append(int(i))
        for i in range(len(lst) - 1, 0, -1) :
            if(lst[i] < lst[i-1]) :
                lst[i] = 9
                lst[i-1] -= 1
        ans = ""
        for i in range(len(lst)) :
            if i == 0 and lst[i] != old[i] :
                if lst[i] != 0 :
                    ans += str(lst[i])
                for j in range(len(lst) - 1) :
                    ans += str(9)
                break
            else :
                ans += str(lst[i])
        #print(ans)
        ofile.write("Case #" + str(t+1) + ": " + ans+"\n")
ofile.close()
    
