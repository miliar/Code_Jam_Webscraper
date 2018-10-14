import collections
import logging

logging.basicConfig(level=logging.WARN)

FLIP = {'+': '-', '-': '+'}


def happy(row):
    logging.debug('happy({})'.format(row))
    ans = '-' not in row
    logging.info(ans)
    return ans


def flip(row):
    logging.debug('flip({})'.format(row))
    ans = ''.join([FLIP[x] for x in row])
    logging.info(ans)
    return ans


def flips(row, k):
    logging.debug('flips({},{})'.format(row, k))
    left, right = 0, k
    while right <= len(row):
        ans = row[:left] + flip(row[left:right]) + row[right:]
        logging.info(ans)
        yield ans
        left += 1
        right += 1


def count_flips(pancakes, k):
    seen = set()
    q = collections.deque()
    q.append((pancakes, 0))
    seen.add(pancakes)
    while q:
        row, cost = q.popleft()
        if happy(row):
            return cost
        for flip in flips(row, k):
            if flip in seen:
                continue
            q.append((flip, cost+1))
            seen.add(flip)

    return 'IMPOSSIBLE'


T = int(input())
for case in range(1, T+1):
    S, K = input().split()
    K = int(K)
    print('Case #{}: {}'.format(case, count_flips(S, K)))
