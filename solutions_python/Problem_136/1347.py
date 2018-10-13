def main():
    a = open('B-large.in', 'r')
    test = a.read()
    #test = raw_input()
    test2 = test.replace('\n', ',')
    allinfo = test2.split(',')
    testcase = int(allinfo[0])
    i = 1
    b = open('result2', 'w')
    while i <= testcase:
        testrow = allinfo[i]
        row = testrow.split(' ')
        speed = 2.0
        C = float(row[0])
        F = float(row[1])
        X = float(row[2])


        
        one_more = C/speed +X/(speed + F)
        no_more = X/speed
        total = 0.0
        while no_more > one_more:
            total += C/speed
            speed += F
            no_more = X/speed
            one_more = C/speed + X/(speed + F)

        result = total + no_more
        print ('Case #%d: %f' % (i, result))
        b.write('Case #%d: %f\n' % (i, result))
        
        i +=1
main()
