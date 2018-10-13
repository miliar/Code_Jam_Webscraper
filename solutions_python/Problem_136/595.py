import sys

f = open(sys.argv[1])
lines = f.readlines()
f.close()

cases = int(lines[0].strip())

case_no = 0
line = 1
while(case_no != cases):
    case_no += 1

    prob = lines[line].split(" ")
    C = float(prob[0].strip())
    F = float(prob[1].strip())
    X = float(prob[2].strip())

    line += 1
    
    rate = 2;
    cost = 0;
    while(True):
        if (cost + X/rate <= cost + C/rate + X/(rate+F)):
            cost += X/rate;
            break;
        else:
            cost += C/rate;
            rate += F;
    print "Case #" + str(case_no) + ": " + str(cost)

