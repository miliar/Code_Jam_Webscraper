import copy

def main():
    filename = 'D-large'
    
    inf = open(filename + '.in', 'r')
    outf = open(filename + '.out', 'w')
    for i, line in enumerate(inf):
        values = line.split()
        if i == 0:
            T = int(values[0]) # number of test cases
            print 'T: %d' % T
            continue
        if i % 2 == 1:
            N = int(values[0])
            continue
        else:
            C = [int(j) for j in values]
        
        print N, C
        
        
        
        cnt = 0
        
#        cnt = test(C)
        cpy = copy.deepcopy(C)
        cpy.sort()
        wrong = 0
        for j in range(N):
            if cpy[j] != C[j]:
                wrong += 1

        
#        mask = 0
#        # already fixed
#        for j in range(N):
#            if j+1 == C[j]:
#                mask ^= 1 << j
#        print bin(mask), C
#        
#        # choose candidates to swap
#        for j in range(N):
#            if mask & (1 << j) == 0:
#                try:
#                    idx = C.index(j+1)
#                    C[idx] = C[j]
#                    C[j] = j+1
#                    cnt += 2
#                    mask ^= 1 << j
#                    if idx == j+1:
#                        mask ^= 1 << idx
#                    print bin(mask), C
#                    
#                except ValueError, e:
#                    pass
        
#        buf = 'Case #%d: %.6f\n' % (int(i / 2), cnt*2)
        buf = 'Case #%d: %.6f\n' % (int(i / 2), wrong)
        print buf,
        outf.write(buf)
    inf.close()

def test(seq, depth=-1):
    depth += 1
    finished = True
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            if estimate(seq, i, j) > 0:
                finished = False
                return test(swap(seq, i, j), depth)
    print depth, seq
    if finished:
        return depth

def estimate(seq, i, j):
    before = 0
    after = 0
    before += 1 if seq[i] == i+1 else 0
    before += 1 if seq[j] == j+1 else 0
    
    after += 1 if seq[i] == j+1 else 0
    after += 1 if seq[j] == i+1 else 0
    
    return after - before

def swap(seq, i, j):
    ret = copy.deepcopy(seq)
    tmp = ret[i]
    ret[i] = ret[j]
    ret[j] = tmp
    return ret

def quicksort(seq):
    if len(seq) <= 1:
        return seq
    
    left = []
    right = []
    pivot = seq[0]
    for i in range(1, len(seq)):
        if seq[i] <= pivot:
            left.append(seq[i])
        else:
            right.append(seq[i])
    print seq, left, pivot, right
    
    return quicksort(left) + [pivot] + quicksort(right)


if __name__ == '__main__':
    main()
    
