import fileinput
test = [line for line in fileinput.input()]
cases = int(test[0])
for i in range(cases):
    C,F,X = [float(num) for num in test[i+1].split(" ")]
    start,prod = 0,2
    best = X*3
    while (X/prod) + start < best:
        best = (X/prod) + start
        start += C/prod
        prod += F
    print "Case #%d: %.7f" % (i+1,best)