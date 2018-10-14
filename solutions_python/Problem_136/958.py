in_f = open('B-large.in.txt', 'r')
out_f = open('output', 'w')

t = int(in_f.readline())
for t in range(1, t+1):
    print 'processing %d case' % t
    result = 0
    speed = 2
    line = in_f.readline().split(' ')
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])
    while True:
        if x/speed > c/speed+x/(speed+f):
            print c/speed
            result += c/speed
            speed += f
        else:
            print x/speed
            result += x/speed
            break
    out_f.write('Case #%d: %0.8f\n' % (t,result))
    print 
in_f.close()
out_f.close()
