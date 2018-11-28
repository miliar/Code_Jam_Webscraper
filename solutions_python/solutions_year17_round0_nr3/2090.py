def main():
  T = int(raw_input())
  for i in range(T):
      N, K = raw_input().split(' ')
      N, K = int(N), int(K)

      result = run_case(N, K)
      print 'Case #{}: {} {}'.format(i+1, result[0], result[1])


def run_case(n, k):
    S = [False] * (n + 2)
    S[0] = True ; S[-1] = True

    for p in range(k):
        y, z = take_a_stall(S)

    return y, z


def take_a_stall(s):
    def _done(cs):
        s[cs] = True
        return max(*C[cs]), min(*C[cs])

    # iterate over empty stalls by index
    C = {}
    open_spots = [i for i, o in enumerate(s) if o is False]
    for es in open_spots:
        L = es - next_occupied(s, es, go_left=True) - 1
        R = next_occupied(s, es, go_left=False) - es - 1
        C[es] = (L, R)

    # find the set of stalls where min(L, R) is maximal
    max_min = max(min(*x) for x in C.values())
    select = [i for i, x in C.iteritems() if min(*x) == max_min]
    if len(select) == 1:
        return _done(select[0])
    assert len(select) > 0

    max_max = max(max(*C[i]) for i in select)
    select_max = [i for i in select if max(*C[i]) == max_max]
    if len(select_max) == 1:
        return _done(select_max[0])
    assert len(select_max) > 0

    # take leftmost
    return _done(min(select_max))


def next_occupied(s, i, go_left):
    step = -1 if go_left else 1
    i = i + step
    while not s[i]:
        i = i + step
    return i


if __name__ == '__main__':
    main()
    #pass
