t = int(input())
for case in range(t):
    tmp = input()
    s = int(tmp[0]) + 1
    shy = tmp[2:]
    card = [int(shy[i]) for i in range(s)]
    prefix_sum = [0]*s
    prefix_sum[0] = card[0]
    for i in range(1, s):
        prefix_sum[i] = prefix_sum[i-1] + card[i]
    m = 0
    for i in range(1, s):
        m = max(m, i - prefix_sum[i-1])
    print('Case #' + str(case+1) + ": " + str(m))