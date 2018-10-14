#!/usr/bin/env python3


class Kuhn(object):
    def __init__(self, edges):
        self.row_edges = {}
        self.col2row = {}
        for r, c in edges:
            lst = self.row_edges.get(r, [])
            lst.append(c)
            self.row_edges[r] = lst

    def try_kuhn(self, u):
        if self.used[u]:
            return False
        self.used[u] = True
        for to in self.row_edges[u]:
            if to not in self.col2row or self.try_kuhn(self.col2row[to]):
                self.col2row[to] = u
                return True
        return False

    @property
    def edges(self):
        for r in self.row_edges.keys():
            self.used = {r: False for r in self.row_edges.keys()}
            self.try_kuhn(r)
        return [
            ((r + c) // 2, (c - r) // 2)
            for c, r in self.col2row.items()
        ]


class Board(object):
    def __init__(self, ind):
        self._ind = ind + 1;
        self.n, self.m = list(map(int, input().split()))
        self.hor = set(range(self.n))
        self.ver = set(range(self.n))
        self.good_diag = set(range(1 - self.n, self.n))
        self.bad_diag = set(range(2 * self.n - 1))
        self.lines = []
        self.diags = []
        for _ in range(self.m):
            c, i, j = input().split()
            i, j = int(i) - 1, int(j) - 1
            if c not in '.+':
                self.lines.append((i, j))
                self.hor.discard(i)
                self.ver.discard(j)
            if c not in '.x':
                self.diags.append((i, j))
                self.good_diag.discard(i - j)
                self.bad_diag.discard(i + j)


    def fill(self):
        self.board = [['.'] * self.n for i in range(self.n)]
        def update_board():
            line_conv = {'.': 'x', '+': 'o'}
            diag_conv = {'.': '+', 'x': 'o'}
            for i, j in self.lines:
                self.board[i][j] = line_conv[self.board[i][j]]
            for i, j in self.diags:
                self.board[i][j] = diag_conv[self.board[i][j]]

        update_board()
        self.lines = []
        self.diags = []
        for i, j in zip(self.hor, self.ver):
            self.lines.append((i, j))
        edges = []
        for i in range(self.n):
            for j in range(self.n):
                gd, bd = i - j, i + j
                if gd in self.good_diag and bd in self.bad_diag:
                    edges.append((gd, bd))
        self.diags.extend(Kuhn(edges).edges)
        update_board()
        return self

    def output(self):
        score = {'.': 0, '+': 1, 'x': 1, 'o': 2}
        score = sum(sum(score[pt] for pt in line) for line in self.board)
        points = [
            map(str, (self.board[i][j], i + 1, j + 1))
            for i, j in set(self.diags).union(set(self.lines))
        ]
        print('Case #{}: {:d} {:d}'.format(self._ind, score, len(points)))
        if points:
            print('\n'.join(' '.join(point) for point in points))
        # print('\n'.join(''.join(line) for line in self.board))


if __name__ == '__main__':
    for it in range(int(input())):
        Board(it).fill().output()
