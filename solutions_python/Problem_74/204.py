from sys import stdin

num_cases = int(stdin.readline())
for case_index in xrange(1, num_cases+1):
    data = stdin.readline().split()
    data = [[data[2*k+1],data[2*k+2]] for k in xrange(len(data)/2)]
    O = [1,0]
    B = [1,0]
    for datum in data:
        bot = datum[0]
        button = int(datum[1])
        if datum[0] == 'O':
            O = [button, O[1] + abs(button - O[0]) + 1]
            if O[1] <= B[1]:
                O[1] = B[1] + 1
        else:
            B = [button, B[1] + abs(button - B[0]) + 1]
            if B[1] <= O[1]:
                B[1] = O[1] + 1
    print "Case #" + str(case_index) + ": " + str(max(B[1], O[1]))

