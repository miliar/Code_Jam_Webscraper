import argparse

def preprocess_data(data_str):
    n, k = [int(x) for x in data_str.split(' ')]
    return n, k

def tdiff(tup):
    return tup[1]-tup[0]

def simulate_stalls_exp(n, k):
    stalls = [True] + [False]*n + [True]
    for k_ix in xrange(k):
        scores = []
        for ix in xrange(n+2):
            if not stalls[ix]:
                left, right = 0, 0
                left_ix = ix-1
                while left_ix > 0:
                    if stalls[left_ix]:
                        break
                    left += 1
                    left_ix -= 1

                right_ix = ix+1
                while right_ix < (n+1):
                    if stalls[right_ix]:
                        break
                    right += 1
                    right_ix += 1
                scores.append((ix, (left, right)))

        # print 'computed scores:', scores
        # find min(L, R)
        min_lr = max([min(x[1][0], x[1][1]) for x in scores])
        scores_min_f = [x for x in scores if min(x[1][0], x[1][1]) == min_lr]
        # print 'min_lr:', min_lr, 'filtered min:', scores_min_f

        # find max(L, R)
        max_lr = max([max(x[1][0], x[1][1]) for x in scores_min_f])
        scores_max_f = [x for x in scores_min_f if max(x[1][0], x[1][1]) == max_lr]
        # print 'max_lr:', max_lr, 'filtered max:', scores_max_f
        # print max_lr, scores_max_f

        # find leftmost
        chosen = min(scores_max_f, key=lambda x: x[0])
        chosen_ix = chosen[0]
        chosen_lr = chosen[1]
        # print 'chosen idx:', chosen_ix
        stalls[chosen_ix] = True

        if k_ix == k-1:
            return chosen_lr[1], chosen_lr[0]
            


def simulate_stalls(n, k):
    ix_queue = [(0, n+1)]
    
    print 'Start:', n
    for _ in xrange(k-1):
        start, stop = ix_queue.pop(0)
        mid = (stop + start) / 2
        left, right = (start, mid), (mid, stop)
        fst, snd = (right, left) if tdiff(left) < tdiff(right) else (left, right)

        if tdiff(fst) >= 2:
            ix_queue.append(fst)

        if tdiff(snd) >= 2:
            ix_queue.append(snd)
        # print 'Start:', start, 'Stop:', stop
        # print 'Left:', left, 'Right:', right
        # print 'Queue:', ix_queue
    start, stop = ix_queue.pop(0)
    mid = (stop + start) / 2
    print 'Final Start:', start, 'Stop:', stop
    L = mid-start-1
    R = stop-mid-1
    # print 'y:', max(L, R), 'z:', min(L, R)

    return max(L, R), min(L, R) 

if __name__ == '__main__':
    # parse input args
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--input', required=True, help='Path to input file')
    ap.add_argument('-o', '--output', required=True, help='Path to output file')
    args = vars(ap.parse_args())

    input_path = args['input']
    output_path = args['output']

    with open(input_path) as fd:
        num_cases = int(fd.readline().strip())
        cases = [preprocess_data(line.strip()) for line in fd]
    print cases

    output = []
    for ix, (n, k) in enumerate(cases):
        print 'n_ix:', ix
        y, z = simulate_stalls_exp(n, k)
        output.append((str(y), str(z)))

    print 'Output:', output
    with open(output_path, 'w') as fd:
        for ix, (y, z) in enumerate(output):
            fd.write('Case #%d: %s %s\n' % (ix+1, y, z))
