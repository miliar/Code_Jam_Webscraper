input = open('B-small-attempt0.in', 'r')
output = open('B-small-attempt0.out', 'w')
t = int(input.readline().rstrip())
for test in range(t):
    output.write("Case #" + str(test + 1) + ": ")
    n, R, O, Y, G, B, V = map(int, input.readline().rstrip().split())
    ans = ""
    
    if O == G == V == 0:
        if R * 2 > n or Y * 2 > n or B * 2 > n:
            ans = "IMPOSSIBLE"
        else:
            col = [[R, "R"], [Y, "Y"], [B, "B"]]
            col.sort(reverse=True)
            ans += (col[0][1] + col[2][1]) * (col[0][0] - col[1][0])
            diff = col[0][0] - col[1][0]
            col[0][0] -= diff
            col[2][0] -= diff            
            ans += (col[0][1] + col[1][1] + col[2][1]) * col[2][0]
            col[0][0] -= col[2][0]
            col[1][0] -= col[2][0]
            col[2][0] -= col[2][0]
            ans += (col[0][1] + col[1][1]) * col[0][0]
    print(ans, file = output)

input.close()
output.close()