T = int(input())

for i in range(1, T+1):
        N = input()
        if len(N) == 1:
                print("Case #%d: %s" % (i, N))
                continue
        N = list(N)
        finished = False

        while(not finished):
                for l in range(len(N)-1):
                        if N[l+1] < N[l]:
                                N[l] = str(chr(ord(N[l]) - 1))
                                for k in range(l+1, len(N)):
                                        N[k] = "9"
                                break
                else:
                        finished = True
        print("Case #%d: %s" % (i,"".join(N).lstrip("0")))
 

        
