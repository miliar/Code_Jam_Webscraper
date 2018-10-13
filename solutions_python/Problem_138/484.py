repeat = int(input())
for i in range(repeat):
    num = int(input())
    dec,war = 0,num;
    me = [float(a) for a in input().split(" ")]
    riv = [float(a) for a in input().split(" ")]
    me.sort()
    riv.sort()
    j = 0
    for a in riv:
        while j < num and me[j] < a:
            j += 1
        if j == num:
            break
        else:
            dec += 1
            j += 1
    j = 0
    for a in me:
        while j < num and riv[j] < a:
            j += 1
        if j == num:
            break
        else:
            war -= 1
            j += 1
    print("Case #"+str(i+1)+": "+str(dec)+" "+str(war))