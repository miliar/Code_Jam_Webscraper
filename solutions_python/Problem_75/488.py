T = input()
for cas in range(1, T+1):
    create = {}
    repel = []
    args = raw_input()
    arglist = args.split(" ")
    C = int(arglist[0])
    #print "C=", C
    if C>0:
        for i in range(1, C+1):
            s = arglist[i]
            create[(s[0],s[1])] = s[2]
            create[(s[1],s[0])] = s[2]
    D = int(arglist[C+1])
    #print "D=", D
    if D>0:
        for i in range(C+1+1, C+1+D+1):
            s = arglist[i]
            repel.append((s[0],s[1]))
            repel.append((s[1],s[0]))

    N = int(arglist[C+1+D+1])
    mag = arglist[C+1+D+1+1]
    #print create, repel, mag
    stack = []
    for x in mag:
        if len(stack) == 0:
            stack.append(x)
            continue

        ch = stack.pop()
        if (ch, x) in create:
            stack.append(create[(ch, x)])
            continue
        elif (x, ch) in create:
            stack.append(create[(x, ch)])
            continue
        else:
            pass
        
        flag = 0
        stack.append(ch)
        for ch in stack:
            if (ch, x) in repel or (x, ch) in repel:
                #print (ch, x)
                stack = []
                flag = 1
                break
            else:
                pass
        if flag == 0:
            stack.append(x)
    
    if len(stack) == 0:
        print "Case #"+str(cas)+": []"
    else:
        ans = "Case #"+str(cas)+": ["
        ch = 0
        for ch in range(len(stack)-1):
            ans += str(stack[ch])+", "
        if (len(stack)==1):
            ch=0 
        else:
            ch+=1
        ans += str(stack[ch])+"]"
        print ans

