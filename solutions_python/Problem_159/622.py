t = int(input())

for i in range(t):

    n = int(input())
    m = input().split()

    m = [int(k) for k in m]

    ans1 = 0
    ans2 = 0
    rate = 0
    
    for q in range(1, len(m)):
        if m[q - 1] > m[q]:
            diff = m[q - 1] - m[q]
            ans1 += diff

            if(diff > rate):
                rate = diff
    
    for q in range(len(m) - 1):
        diff = m[q] - rate

        if diff >= 0:
            ans2 += rate
        else:
            ans2 += m[q]

    print("Case #" + str(i+1) + ": " + str(ans1) + " " + str(ans2))
    
