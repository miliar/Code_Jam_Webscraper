import math
from itertools import starmap
import heapq

def preprocess(ingr_size, pack_size):
    # returns a tuple of possible sizes
    overall = []
    for ingr_i, line in enumerate(pack_size):
        tmp = []
        for indiv_pack in line:
            tmp.append(set(range(
                int(math.ceil(indiv_pack/(ingr_size[ingr_i]*1.1))),
                int(math.floor(indiv_pack/(ingr_size[ingr_i]*0.9)))+1
            )))
        overall.append(tmp)
    return overall

def custom_min(iterable):
    try:
        return min(iterable)
    except ValueError:
        return -1

def solver(possibles, N, P):
    idxs = [0 for i in xrange(N)]
    firsts = [(custom_min(poss[0]), ingr_idx, poss[0]) 
              for ingr_idx, poss in enumerate(possibles)]
    heapq.heapify(firsts)
    total_count = 0
    while all(map(lambda x: x<P, idxs)):
        for idx, t_set in enumerate(firsts):
            if idx == 0:
                coco = t_set[2]
            else:
                coco &= t_set[2]
        if len(coco) == 0:
            _, ingr_idx, _ = heapq.heappop(firsts)
            idxs[ingr_idx] += 1
            if idxs[ingr_idx] == P: break
            new_stuff = possibles[ingr_idx][idxs[ingr_idx]]
            heapq.heappush(
                firsts,
                (custom_min(new_stuff), ingr_idx, new_stuff)
            )
        else:
            total_count += 1
            for ingr_idx in xrange(N):
                idxs[ingr_idx] += 1
                if idxs[ingr_idx] == P: break
                firsts = [(custom_min(poss[idxs[ingr_idx]]), 
                           ingr_idx, poss[idxs[ingr_idx]])
                          for ingr_idx, poss in enumerate(possibles)]
                heapq.heapify(firsts)
    return total_count

def main():
    t_val = input('')
    for c_idx in xrange(t_val):
        N, P = map(int, raw_input('').split())
        IGR_SIZE = map(int, raw_input('').split())
        pack_size = []
        for igr_i in xrange(N):
            pack_size.append(sorted(map(int, raw_input('').split())))
        possibs = preprocess(IGR_SIZE, pack_size)
        answ = solver(possibs, N, P)
        print 'Case #%d: %d' % (c_idx+1, answ)

main()