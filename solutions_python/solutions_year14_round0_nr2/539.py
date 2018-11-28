__author__ = 'Antariksh Bothale'
import sys, math

if __name__ == '__main__':
    total = map(lambda x: x.strip(), sys.stdin.readlines())
    case_num = 0
    for line in total[1:]:
        C, F, X = tuple(map(float, line.split()))
        #print C, F, X
        N = int(math.ceil((F * (X - C) - 2 * C) / (F*C) ))
        #print N
        N = max(0, N)
        sum_acc = 0
        for i in range(0, N):
            sum_acc += C / (2 + i * F)
        sum_acc += X / (2 + N * F)
        case_num += 1
        print ('Case #{0}: {1:15.7f}'.format(case_num, sum_acc))
