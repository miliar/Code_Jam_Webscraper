i = open('test.txt', 'r')
o = open('result.txt', 'w')

tests = int(i.readline())

for t in xrange(tests):
    s = 2.0
    c, f, x = [float(v) for v in i.readline().split()]

    
    fact = [0]
    speed = [s]
    bestTime = fact[-1] + x / speed[-1]
    
    while True:
        fact.append(fact[-1] + c / speed[-1])
        speed.append(speed[-1] + f)
        
        time = fact[-1] + x / speed[-1]
        if time >= bestTime:
            break
        else:
            bestTime = time
     
    o.write('Case #{0}: {1}\n'.format(t + 1, bestTime))
