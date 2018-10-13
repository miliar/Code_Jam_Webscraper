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
        list = [s]

        while len(list) >0 :
            s = list.pop(0)
            depth = self.smap[s] + 1
            for item in mask(s, self.k):
                if item not in self.smap or self.smap[item] > depth:
                    self.smap[item] = depth
                    list.append(item)
            if self.target in self.smap:
                break

        if self.target in self.smap:
            return str(self.smap[self.target])
        else:
            return "IMPOSSIBLE"

class Solution2(object):
    def solution(self, line):
        k = len(line)
        listline = [int(s) for s in list(line)]
        def istidy(listline) :
            for i in range(1, len(listline)):
                if listline[i] < listline[i-1]:
                    return False
            return True
        if istidy(listline):
            return int(line)
        maxn = []
        for i in range(1, k):
            maxn.append(int(line[:i]) * (10 ** (k- i)) -1)
        return max([num for num in maxn if istidy(list(str(num)))])

def getn(line, i):
    return int(line[:i]) * (10 ** (len(line) - i)) -1

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, Solution2().solution(input())))
    # check out .format's specification for more formatting options