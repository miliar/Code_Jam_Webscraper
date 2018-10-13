def lower(n, i):
    l = len(n)
    nines = l-i-1
    if(int(n[i]) > 1):
        n = n[0:i]+str(int(n[i])-1);
    elif(n[i] == "1"):
        if(i == 0):
            n = ""
        else:
            n = n[0:i]+str(int(n[i])-1);
    else:
        n = n[0:i]+"9";
    return n+"9"*nines
    

numLines = int(input())
case = 0
for case in range(numLines):
    n = input()
    i = 0
    while(i < len(str(n))-1):
        if n[i] > n[i+1]:
            n = lower(n, i)
            i = 0
            continue
        i+=1
    print ("Case #"+str(case+1)+": "+str(n))
    