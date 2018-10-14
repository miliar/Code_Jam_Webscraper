from parser import parse

def helper(test):
    rate = 2
    C = test[0]
    F = test[1]
    X = test[2]
    return toBuy(C, F, X, rate)


def toBuy(C, F, X, rate):
    counter = float(0)
    while True:
        if (float(X/rate) <= float(C/rate) + float(X/(rate+F))):
            counter += float(X/rate)
            return counter
        else:
            counter += float(C/rate)
            rate += F


# schema here
schema = [(), [lambda x: [float(z) for z in x.split()]]]

num_tests,tests = parse(schema)
for case,test in enumerate(tests):
	sol = helper(test)
	print 'Case #{}: {}'.format(case+1, sol)
