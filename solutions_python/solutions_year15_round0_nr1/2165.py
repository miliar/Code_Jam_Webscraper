def ovation(tc, smax, audi):
    """This function takes in the smax and audi"""
    count = 0
    sum = 0
    if smax == 0:
        print "Case #%s: 0" % tc
    else:
        for i in range(smax):
            sum = sum + int(audi[i])
            if int(audi[i]) < 1 and sum <= i:
                count = count + 1
                sum = sum + 1
        print "Case #%s: %s" % (tc, count)

    
if __name__ == '__main__':
    with open('Codejam_qual 2015_in.txt', 'r') as fp:
        testcases = int(fp.readline())
        for i in range(testcases):
            [smax, audi] = fp.readline().split()
            ovation(i+1, int(smax), audi)
