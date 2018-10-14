def flip(c):
    if (c == "+"):
        return("-")
    else:
        return("+")
    
for case in range(1, int(input())+1):
        (si, ki ) = input().split()
        K = int(ki)
        S = list(si)
        result=0
        i=0
        s=len(S)
        while (i <= s-K):
            if (S[i] == "-"):
                result += 1
                for j in range(K):
                    S[i+j] = flip(S[i+j])
         #   print("".join(S))
            i += 1
        #print("".join(S[-K:]))
        if "".join(S[-K:]) == "+" * K:
            print ("Case #%d: %d" % (case,result))
        else:
            print ("Case #%d: IMPOSSIBLE" % (case))
