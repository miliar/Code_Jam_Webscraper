import os, sys


#T Test Cases
#10 lines, for two card arrangements each preceded by answer

#output:
#    "Case #x: y"
# where x is test case [1..]
# y is
#    if only one card could have been chosen, answer
#    else "Bad Magician!"
#    if no cards "Volunteer cheated!"

def magic(cases, data):
    output = []
    for t in xrange(cases):
        output.append("")
        case = data[t * 10:(t + 1) * 10]
        r1 = case[case[0]]
        r2 = case[case[5]+5]
        match = [x for x in r1 if x in r2]
        if len(match) != 1:
            if len(match) == 0:
                output[t] = 'Volunteer cheated!'
            else:
                output[t] = 'Bad magician!'
        else:
            output[t] = match[0]
    return output


if __name__=='__main__':
    if len(sys.argv) < 2:
        sys.exit()
    with open(sys.argv[1], 'r') as f:
        y = [l.rstrip() for l in f]
        t = int(y[0])
        x = y[1:]
        for i in xrange(10 * t):
            if i % 10 in [0, 5]:
                x[i] = int(x[i])
            else:
                x[i] = [int(n) for n in x[i].split()]
        ans = magic(t, x)
        with open("{}_output".format(sys.argv[1]), 'w') as o:
            for a in xrange(t):
                o.write("Case #{}: {}\n".format(a+1, ans[a]))