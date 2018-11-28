oufile = open('out.txt', 'w')

with open('B-large.in') as infile:
    T = int(infile.readline())
    for i in range(0,T):
        C, F, X = (float(x) for x in infile.readline().split(' '))
        t = 0.0
        rate = 2.0
        while True:
            t_1 = X / rate
            t_2 = C / rate + X / (rate + F)
            if (t_2 < t_1):
                t += C / rate
                rate += F
            else:
                t += X / rate
                break
        oufile.write('Case #' + str(i+1) + ': ')
        oufile.write('%.7f' % t + '\n')