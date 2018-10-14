import math

def prep_file(fileName):
    f = open(fileName, 'r');
    return f.readlines();

def solve_case(line):
    val = line.replace('\n', '').split(' ')
    timeSpent = 0.0
    cookieRate = 2.0
    c = float(val[0])
    f = float(val[1])
    x = float(val[2])

    print 'c: ', c, ' f: ', f, ' x: ', x

    timeFactory = c / cookieRate
    timeFinish = x / cookieRate

    if x / cookieRate <= c / cookieRate: # case no factory needed
	return x / cookieRate
    else:
        while (timeFactory + (x / (cookieRate + f))) < timeFinish:
	    timeSpent = timeSpent + timeFactory
	    cookieRate = cookieRate + f
	    timeFinish = x / cookieRate
	    timeFactory = c / cookieRate

    return timeSpent + timeFinish


def main(fileName, outputName):

    f = prep_file(fileName)
    cases = f.pop(0)

    output = ''
    counter = 1

    for i in range(int(cases)):
	r = solve_case(f[i])
        output = output + 'Case #' + str(counter) + ': ' + format(r, '.7f') + '\n';
	counter = counter + 1
    f = open(outputName, 'w+');
    f.write(output[:-1]);

main("blarge.in", "output4.txt")
#main("demoInput.txt", "demoOutput.txt")
