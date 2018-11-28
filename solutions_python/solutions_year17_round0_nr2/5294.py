t = int(input())
#print(t)
for i in range(t):
    tidy = False
    s = input()
    #print(s)
    a = ['2','3','4','5','6','7','8','9']
    for j in range(int(s),0,-1):
        if "10" in str(j) and not(any(x in s for x in a)):
            print("Case #" + str(i+1) + ":", '9'*(len(str(j)) - 1) )
            break
        if len(str(j)) > 1:
            for k in range(len(str(j))-1):
                if (str(j)[k] <= str(j)[k + 1]):
                    tidy = True
                else:
                    tidy = False
                    break
        else:
            tidy = True

        if(tidy):
            print("Case #" + str(i+1) + ":", str(j))
            break
