num = int(raw_input())
output = [None]*num

for k in range(num):
        N, K = map(int, raw_input().strip().split(" "))
        spaces = {N:1}
        max_space = N
        for _ in range(K):
            l = (max_space-1)//2
            r = (max_space)//2
            try:
                spaces[l] += 1
            except KeyError:
                spaces[l] = 1
            try:
                spaces[r] += 1
            except KeyError:
                spaces[r] = 1
            spaces[max_space] -= 1
            if spaces[max_space]==0:
                del spaces[max_space]
                max_space = max(spaces.keys())
        output[k] = (r, l)

for i in range(num):
    print ("Case #%d: %d %d" % (i+1, output[i][0], output[i][1]))
