import numpy as np
import fileinput
import collections

def preprocess(board):
    """max ones square size from each top-left corner"""
    M, N = board.shape
    to_right = np.zeros(board.shape, np.int16)
    to_right[:,-1] = board[:,-1]
    for n in reversed(range(N-1)):
        to_right[:,n] = board[:,n] * (to_right[:,n+1] + 1)

    sizes = np.zeros(board.shape, np.int16)
    for n in range(N):
        for m in range(M):
            max_width = min(to_right[m,n], M - m)
            k = 0
            while True:
                max_width = min(max_width, to_right[m+k,n])
                if k >= max_width:
                    break
                k += 1
                if k >= max_width:
                    break
            sizes[m,n] = k
    return sizes

def solve(board):
    M, N = board.shape
    Y, X = np.indices(board.shape)
    chess = (X ^ Y) & 1
    sizes = np.max([preprocess(board ^ chess),
                    preprocess((~board) ^ chess)],
                   axis=0)
##    print sizes
    sizecounts = collections.defaultdict(int)
    while True:
        top,left = np.unravel_index(np.argmax(sizes), sizes.shape)
        s = sizes[top,left]
        if s == 0:
            break
        sizes[top:top+s, left:left+s] = 0
        for m in range(max(top - s, 0), top):
            for n in range(max(left - s, 0), left):
                sizes[m,n] = min(sizes[m,n], max(top - m, left - n))
        for m in range(top, top + s):
            for n in range(max(left - s, 0), left):
                sizes[m,n] = min(sizes[m,n], left - n)
        for m in range(max(top - s, 0), top):
            for n in range(left, left + s):
                sizes[m,n] = min(sizes[m,n], top - m)
##        print sizes
##        print 
        sizecounts[s] += 1
##    print '>', sum((k**2*v) for k,v in sizecounts.items()), N * M
    return sorted(sizecounts.items(), reverse=True)

it = fileinput.input()
T = int(next(it))
for case in range(1, T + 1):
    M, N = (int(w) for w in next(it).split())
    board = np.zeros(shape=(M,N), dtype=np.bool8)
    for i in range(M):
        for j, h in enumerate(next(it).strip()):
            four = np.array([int(h, 16)], dtype=np.uint8)
            board[i,j*4:(j+1)*4] = np.unpackbits(four)[-4:]
    res = list(solve(board))
    print 'Case #{0}: {1}'.format(case, len(res))
    for (size, count) in res:
        print size, count
