"""
Google Code Jam
2017 Qualification Round

Problem A. Oversized Pancake Flipper
    :author: yamaton
    :date: 2017-04-08
"""

import collections
import sys


def flip_at(s, i, n):
    res = s[:i] + flip(s[i:i + n]) + s[i + n:]
    return res


def flip(s):
    return s.translate(str.maketrans('-+', '+-'))


def next_states(s, n):
    states = [flip_at(s, i, n) for i in range(len(s) - n + 1)]
    return states


def is_goal(s):
    return set(s) == set('+')


def search(s, n):
    ini = [s]
    seen = set(s)
    queue = collections.deque([ini])
    while queue:
        hist = queue.popleft()
        q = hist[-1]
        # pp('q =', q)
        if is_goal(q):
            return hist

        qs_next = next_states(q, n)
        for q_ in qs_next:
            if q_ not in seen:
                seen.add(q_)
                queue.append(hist + [q_])

    return []


def solve__(s, n):
    traj = search(s, n)
    pp('traj:', traj)
    if traj:
        return len(traj) - 1
    else:
        return None


def solve(s, n):
    cnt = 0
    for i in range(len(s) - n + 1):
        if s[i] == '-':
            s = flip_at(s, i, n)
            cnt += 1
    if s[-n:] == '+' * n:
        return cnt

    return None


def pp(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    for _tc in range(1, int(input()) + 1):
        pp('\n--------- case #%d -------' % _tc)
        print("Case #%d: " % _tc, end='')
        s, tmp = input().split()
        n = int(tmp)

        result = solve(s, n)
        pp()
        pp('n =', n)
        pp('s =', s)
        pp('result =', result)
        if result is None:
            print('IMPOSSIBLE')
        else:
            print(result)




if __name__ == '__main__':
    main()
