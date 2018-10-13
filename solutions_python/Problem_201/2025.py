#!env python
import math

def main(input_file='input.txt', output_file='output.txt'):
    fd = open(input_file)
    cases = int(fd.readline())
    output = open(output_file, 'w')

    for i in range(cases):
        N, K = map(lambda x: int(x), fd.readline().split())

        gaps = [(0, N - 1)]
        gaps = ocupe_stalls(gaps, K - 1)
        _, L, R = ocupe_stall(gaps)

        response = "%d %d" % (max(L, R), min(L, R))
        line = 'Case #%d: %s' % (i + 1, response)
        print line
        output.writelines([line, '\n'])

def ocupe_stalls(gaps, people):
    for i in range(people):
        gaps, _, _ = ocupe_stall(gaps)
    return gaps

def ocupe_stall(gaps):
    best_gap_index = 0
    best_gap = gaps[best_gap_index]

    bestL, bestR = count_LR(best_gap)
    best_min_LR = min(bestL, bestR)
    best_max_LR = max(bestL, bestR)

    # find the best gap
    for i, gap in enumerate(gaps[1:]):
        L, R = count_LR(gap)
        min_LR = min(L, R)
        #print 'best_gap', best_gap
        #print 'L: %d, R: %d, best L: %d, bestR: %d' % (L, R, bestL, bestR)
        #print 'minLR > best_min_LR %d %d %r' % (min_LR, best_min_LR, min_LR > best_min_LR)
        if (min_LR > best_min_LR):
            best_gap_index = i + 1
            best_gap = gap
            bestL, bestR = L, R
            best_min_LR = min_LR
            best_max_LR = max(bestL, bestR)
            continue

        if (min_LR == best_min_LR):
            max_LR = max(L, R)
            #print 'maxLR > best_max_LR %d %d %r' % (max_LR, best_max_LR, max_LR > best_max_LR)
            if (max_LR > best_max_LR):
                best_gap_index = i + 1
                best_gap = gap
                bestL, bestR = L, R
                best_min_LR = min_LR
                best_max_LR = max_LR
                continue

    #print 'best_gap', best_gap, bestL, bestR
    gaps = gaps[:best_gap_index] + \
           [ (best_gap[0], best_gap[0] + (bestL - 1)),
             (best_gap[0] + (bestL + 1), best_gap[1]) ] + \
           gaps[best_gap_index + 1:]

    #print '<<', gaps
    return gaps, bestL, bestR

def count_LR(gap):
    L = int(math.ceil((gap[1] - gap[0]) / 2.0))
    R = gap[1] - (gap[0] + L)
    return L, R

if __name__ == '__main__':
    #main()
    main(input_file='inputs/C-small-1-attempt0.in', output_file='outputs/C-small-1-attempt0.out')
