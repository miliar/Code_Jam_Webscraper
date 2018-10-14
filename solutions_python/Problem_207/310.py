# from collections import deque
#
# FORBIDDEN = {
#     'RR', 'RV', 'RO',
#     'VV', 'VR', 'VB',
#     'BB', 'BV', 'BG',
#     'GG', 'GB', 'GY',
#     'YY', 'YG', 'YO',
#     'OO', 'OY', 'OR',
# }
#
#
# def solve(N, R, O, Y, G, B, V):
#     # if any(N // 2 < x
#     queue = deque()
#     queue.append(('', R, O, Y, G, B, V))
#     while queue:
#         path, r, o, y, g, b, v = queue.pop()
#         if len(path) == N:
#             if path[0] + path[-1] not in FORBIDDEN:
#                 return path
#             continue
#
#         if 0 < r and (path == '' or path[-1] + 'R' not in FORBIDDEN):
#             queue.append((path + 'R', r - 1, o, y, g, b, v))
#         if 0 < o and (path == '' or path[-1] + 'O' not in FORBIDDEN):
#             queue.append((path + 'O', r, o - 1, y, g, b, v))
#         if 0 < y and (path == '' or path[-1] + 'Y' not in FORBIDDEN):
#             queue.append((path + 'Y', r, o, y - 1, g, b, v))
#         if 0 < g and (path == '' or path[-1] + 'G' not in FORBIDDEN):
#             queue.append((path + 'G', r, o, y, g - 1, b, v))
#         if 0 < b and (path == '' or path[-1] + 'B' not in FORBIDDEN):
#             queue.append((path + 'B', r, o, y, g, b - 1, v))
#         if 0 < v and (path == '' or path[-1] + 'V' not in FORBIDDEN):
#             queue.append((path + 'V', r, o, y, g, b, v - 1))
#     return 'IMPOSSIBLE'

from itertools import permutations


def solve(N, R, O, Y, G, B, V):
    def _solve(N, R, O, Y, G, B, V):
        conn = {
            'R': 'BGY',
            'O': 'GBV',
            'Y': 'BVR',
            'G': 'VRO',
            'B': 'ROY',
            'V': 'OYG',
        }
        path = []
        data.sort(key=lambda x: (x[0], x[2]), reverse=True)
        assert 0 < data[0][0]
        path.append(data[0][1])
        data[0][0] -= 1

        while len(path) < N:
            data.sort(key=lambda x: (x[0], x[2]), reverse=True)
            last = path[-1]
            for i, (n, c, _) in enumerate(data):
                if 0 < n and c in conn[last]:
                    data[i][0] -= 1
                    path.append(c)
                    break
            else:
                return None

        if path[0] in conn[path[-1]] and path[-1] in conn[path[0]]:
            return ''.join(path)

        c = path.pop()
        for i in range(N - 2):
            c1 = path[i]
            c2 = path[i + 1]
            if c in conn[c1] and c in conn[c2] and c1 in conn[c] and c2 in conn[c]:
                path.insert(i + 1, c)
                return ''.join(path)
        return None

    for r, o, y, g, b, v in permutations(range(6)):
        data = [
            [R, 'R', r],
            [O, 'O', o],
            [Y, 'Y', y],
            [G, 'G', g],
            [B, 'B', b],
            [V, 'V', v],
        ]
        res = _solve(N, R, O, Y, G, B, V)
        if res is not None:
            return res
    return 'IMPOSSIBLE'


T = int(input())
for tc in range(T):
    N, R, O, Y, G, B, V = map(int, input().split())
    print('Case #{}: {}'.format(tc + 1, solve(N, R, O, Y, G, B, V)))
