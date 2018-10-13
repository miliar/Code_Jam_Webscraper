for case in range(1, int(input())+1):
        S = list(input())
        i = len(S) - 1
        sl = len(S)
        while (i > 0):
            if (S[i] < S[i-1]):
                for j in range(i,sl):
                    S[j] = "9"
                k = i - 1
                while ((k>0) and (S[k]=="0")):
                    S[k]="9"
                    k -= 1
                S[k] = chr(ord(S[k])-1)
            i -= 1
        if (S[0]=="0"):
            result="".join(S[1:])
        else:
            result="".join(S)
        print ("Case #%d: %s" % (case,result))
