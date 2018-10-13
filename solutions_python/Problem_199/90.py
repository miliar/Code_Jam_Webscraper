tc = int(input())

for t in range(tc):
    pc, k = input().split()
    k = int(k)
    pc = list(pc)
    ans = 0

    for i in range(len(pc)-k+1):
        if pc[i] == '-':
            for x in range(k):
                if pc[i+x] == '-':
                    pc[i+x] = '+'
                elif pc[i+x] == '+':
                    pc[i+x] = '-'
            ans += 1
    if '-' in pc:
        print('Case #' + str(t+1) + ': IMPOSSIBLE')
    else:
        print('Case #' + str(t+1) + ': ' + str(ans))
