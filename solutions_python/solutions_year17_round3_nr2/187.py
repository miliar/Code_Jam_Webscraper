import heapq
import functools

@functools.total_ordering
class ReverseCompare(object):
    def __init__(self, obj):
        self.obj = obj
    def __eq__(self, other):
        return isinstance(other, ReverseCompare) and self.obj == other.obj
    def __le__(self, other):
        return isinstance(other, ReverseCompare) and self.obj >= other.obj
    def __str__(self):
        return str(self.obj)
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.obj)
    def __int__(self):
        return self.obj

T = int(raw_input())
for t in range(1, T+1):
    AC, AJ = map(int, raw_input().split())
    SC = []
    SJ = []
    S = []
    for i in range(AC):
        c, d = map(int, raw_input().split())
        SC.append((c,d))
        S.append((c,d, 0))
    for i in range(AJ):
        c, d = map(int, raw_input().split())
        SJ.append((c,d))
        S.append((c,d, 1))

    S = sorted(S, key=lambda x: x[0])
    T = [0, 0]
    C = [[], [], []]
    #print 'start', S
    if len(S) == 1:
        ans = 2
    else:
        last_u = None
        first_u = None
        first_c = None
        start_c = 0
        last_d = 0
        for c, d, u in S:
            if u == last_u:
                # keep seq
                # add free time
                C[u].append(c-last_d)
            else:
                # change user
                C[2].append(c-last_d)
                if last_u is not None:
                    #T[last_u].append((start_c, last_d))
                    T[last_u] += last_d-start_c
                else:
                    first_u = u
                    first_c = c
                start_c = c
            last_d = d
            last_u = u
        # deal with last seq:
        if last_u == first_u:
            C[last_u].append(first_c - last_d + 24*60)
            #T[u][0][0] = start_c
            #print "the same", T[last_u], first_c, start_c
            T[last_u] += first_c - start_c + 24*60
            #print "the same", T[last_u], first_c, start_c
            #print "the same", T[last_u]
        else:
            #change user
            C[2].append(first_c - last_d + 24*60)
            #T[last_u].append((start_c, last_d))
            #print "change", T[last_u]
            T[last_u] += last_d - start_c
            #print "change", T[last_u], start_c, last_d

        if first_c == start_c:
            ans = 0
        else:
            ans = 2
        H=[[], []]
        C[0] =  map(ReverseCompare, C[0])
        C[1] =  map(ReverseCompare, C[1])
        heapq.heapify(C[0])
        heapq.heapify(C[1])
        #print 'C: ', C
        #print 'T: ', T
        while not (T[0] <= 720 and T[1]  <= 720):
            if T[0] > 720:
                u = 0
                u2 = 1
            else:
                u = 1
                u2 = 0
            #print T, C, u, u2
            T[u] = T[u] - int(heapq.heappop(C[u]))
            #print T, C
            ans += 2
    print 'Case #{}: {}'.format(t, ans)


