inp = open('B-large.in', 'r')
out = open('out.txt', 'w')

num = int(inp.readline())


for i in range(1, num+1):
    [C, F, X] = [float(j) for j in inp.readline().split()]

    speed = 2
    best = X / speed 
    
    pref = 0
    now = 0 

    while 1:
        pref += C / speed

        speed += F

        now = pref + X / speed

        if now <= best:
            best = now
        else:
            break

    out.write('Case #' + str(i) + ': ' + str(best) + '\n')