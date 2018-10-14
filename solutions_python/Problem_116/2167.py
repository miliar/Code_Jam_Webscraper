def find_result(strip,result):
    if '.' in strip:
        result = 'Game has not completed'
    elif strip['X'] >= 3 and strip['O'] == 0:
        return 'X won', True
    elif strip['O'] >= 3 and strip['X'] == 0:
        return 'O won', True
    return result, False

from collections import Counter

test_in = [[0 for i in range(4)] for j in range(4)]

with open('A-large.in','r') as reading,open('Solution A_very small.txt','w') as writing:
    no_of_testcase = int(reading.readline())

    for i in range(1,no_of_testcase+1):
        for row in range(4):
            test_in[row][:] = reading.readline()[:4]

        decision = False
        result = 'Draw'
        for row in range(4):
            result, decision = find_result(Counter(test_in[row]),result)
            if decision:
                writing.write('Case #%d: %s\n'%(i,result))
                break

        if not decision:
            for col in range(4):
                result, decision = find_result(Counter(zip(*test_in)[col]),result)
                if decision:
                    writing.write('Case #%d: %s\n'%(i,result))
                    break

        if not decision:
            result, decision = find_result(Counter([test_in[0][0], test_in[1][1], test_in[2][2], test_in[3][3]]),result)
            if decision:
                writing.write('Case #%d: %s\n'%(i,result))

        if not decision:
            result, decision = find_result(Counter([test_in[0][3], test_in[1][2], test_in[2][1], test_in[3][0]]),result)
            writing.write('Case #%d: %s\n'%(i,result))

        reading.readline()