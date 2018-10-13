t = int(input())
f = open("out.txt", "w")
for case in range(t):
    tmp = input().split(' ')
    x = int(tmp[0])
    r = int(tmp[1])
    c = int(tmp[2])
    f.write('Case #' + str(case+1) + ": ")
    m = min(r, c)
    if (x == 4 and r ==2 and c == 4) or (x == 4 and r == 4 and c == 2):
        f.write('RICHARD\n')
    elif (r*c) % x != 0 or x >= 7 or (2*m+1) <= x or (x > r and x > c):
        f.write('RICHARD\n')
    else:
        f.write('GABRIEL\n')
f.flush()
f.close()