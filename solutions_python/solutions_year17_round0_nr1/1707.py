from collections import defaultdict


def mask(s, k):
    res = []
    for i in range(len(s) - k + 1):
        copys = list(s)
        for j in range(i, i + k):
            if copys[j] == "+":
                copys[j] = "-"
            else:
                copys[j] = "+"
        res.append(''.join(copys))
    return res

class Solution1(object):
    def solution(self, line):
        s, k = line.split(" ")
        k = int(k)
        self.k = k
        self.target = "+" * len(s)
        self.smap = {}
        self.smap[s] = 0

        def bfs(list, index):
            # visited
            if index >= len(list):
                return
            s = list[index]
            depth = self.smap[s] + 1
            for item in mask(s, self.k):
                if item not in self.smap or self.smap[item] > depth:
                    self.smap[item] = depth
                    list.append(item)
            if self.target in self.smap:
                return
            bfs(list, index + 1)
        bfs([s], 0)

        if self.target in self.smap:
            return str(self.smap[self.target])
        else:
            return "IMPOSSIBLE"


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, Solution1().solution(input())))
  # check out .format's specification for more formatting options