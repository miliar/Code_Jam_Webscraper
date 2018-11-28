t=int(input())
for i in range(1,t+1):
    # print (input().split(' '))
    inp = input().split(' ')
    s,k = list(inp[0]),int(inp[1])
    n=0
    for p in range(len(s)-k+1):
        if s[p]=='-':
            n+=1
            for q in range(p,k+p):
                if s[q]=='-':
                    s[q]='+'
                else:
                    s[q]='-'
            # print (''.join(s))
    if ''.join(s[-k:]) == '+'*k:
        print("Case #{}: {}".format(i, n))
    else:
        print("Case #{}: {}".format(i, 'IMPOSSIBLE'))