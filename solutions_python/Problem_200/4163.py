import math
inp = open('C:/Users/rahulr/Downloads/B-large.in', 'r')
outp = open('C:/Users/rahulr/Downloads/B-large-solution.in', 'w')
lines = inp.readlines()
count = 1
for line in lines[1:]:
    X = line.strip()
    N = int(X)
    nn = X[0]
    # import pdb
    # pdb.set_trace()
    if N > 9:
        for j in xrange(len(X) - 1):
            number = int(X[j+1])
            if number >= int(nn[-1]):
                nn += X[j+1]
            else:
                if int(nn[-1]) > 1:
                    first_occur = nn.find(nn[-1])
                    nn = nn[:first_occur] + str(int(nn[-1]) - 1) + '9'*(j - first_occur)
                else:
                    nn = (len(nn)-1)*'9'
                nn += '9' * (len(X) - j - 1)
                break

    outp.write('Case #' + str(count) + ': ' + nn + '\n')
    count += 1

outp.flush()
outp.close()
