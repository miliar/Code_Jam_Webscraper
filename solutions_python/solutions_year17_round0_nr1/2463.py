for xa in range(1,int(input())+1):
    s,n = input().split(" ")
    n = int(n)
    count = 0
    if (s.count("-") > 0 and len(s) < n):
        print("IMPOSSIBLE")
    else:
        for i in range(len(s)-n+1):
            if(s[i] == "-"):
                count += 1
                for j in range(i,i+n):
                    if(s[j] == "-"):
                        lis = list(s)
                        lis[j] = "+"
                        s = ''.join(lis)
                    elif(s[j] == "+"):
                        lis = list(s)
                        lis[j] = "-"
                        s = ''.join(lis)
        if(s.count("-") == 0):
            print("Case "+ " #"+ str(xa) +": ",end = "")
            print(count)
        else:
            print("Case "+ " #"+ str(xa) +": ",end = "")
            print("IMPOSSIBLE")
