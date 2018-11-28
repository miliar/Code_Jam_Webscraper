T = int(input())
for tc in range(T):
    inpt = input().split()
    s_max = int(inpt[0])
    s_in = inpt[1]
    s = 0
    friends = 0
    for i in range(len(s_in)):
        ppl = int(s_in[i])
        if friends < i - s:
            friends = i - s
        s += ppl
    print('Case #' + str(tc+1) + ":", friends)