t = int(input())
outputlist = [0]*t
for i in range(t):
    inline = input()
    inline = inline.split()
    s = inline[0]
    k = int(inline[1])
    sbin = [0]*len(s)
    iteration = 0

    for j in range(len(s)):
        if s[j] == '-':
            sbin[j] = 1

    for j in range(len(s)-k+1):
        if sbin[j] == 1:
            iteration += 1
            for a in range(j,j+k):
                sbin[a] = (sbin[a] + 1)%2

    if 1 in sbin:
        outputlist[i] = 'Case #' + str(i+1) + ': IMPOSSIBLE'
    else:
        outputlist[i] = 'Case #' + str(i+1) + ': ' + str(iteration)

for i in range(t):
    print(outputlist[i])
