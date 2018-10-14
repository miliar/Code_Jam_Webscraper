import sys

inputStr ='''4
4 11111
1 09
5 110011
0 1'''


class StandingOvation:
    def execute(self, inputStr):
        inputs = inputStr.split('\n')
        test_count = int(inputs[0])
        outputs = []
        for x in xrange(0,test_count):
            levels = inputs[x + 1].split(' ')[1]
            levels = [int(levels[i]) for i in range(0, len(levels))]
            outputs.append('Case #%s: ' % (x+1) + str(self.solve(levels)))
        return outputs

    def solve(self, solevels):
        ss = []
        for i,sl in enumerate(solevels):
            ss.append((0 if i==0 else ss[i-1]) + sl)
        ssm = [i + 1 - ss[i] for i in range(0, len(ss) - 1)]
        result = max(ssm) if ssm else 0
        return result if result > 0 else 0


'''
if s[k]: sum(s[0 ~ k-1]) >= k
ss[i+1] = ss[i] + s[i] => ss[k-1] >= k
max(ss[k-1]-k)
'''


if __name__ == '__main__':
    inputStr = file(sys.argv[1]).read()
    outputs = StandingOvation().execute(inputStr)
    print '\n'.join(outputs)