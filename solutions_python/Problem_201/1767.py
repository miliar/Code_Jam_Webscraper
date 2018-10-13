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


class Solution3(object):
    def solution(self, line):
        s, k = [int(i) for i in line.split(" ")]
        listn = [s]
        while listn[0] > 1 and k > 1:
            n = listn[0]
            i = 1
            while len(listn) > i and k > i + 1 and listn[i] == n:
                i += 1
            listn = listn[i:]
            k -= i
            m = int((n-1)/2)
            if n % 2 == 0:
                listn.extend([m+1] * i)
                listn.extend([m] * i)
            else:
                listn.extend([m] * i *2)
            # print(listn)

        if listn[0] == 1:
            return (0, 0)
        if k == 1:
            n = listn[0]
            m = int((listn[0] - 1) / 2)
            if n % 2 == 0:
                return (m + 1, m)
            else:
                return (m, m)


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    res = Solution3().solution(input())
    print("Case #{}: {} {}".format(i, res[0], res[1]))
    # check out .format's specification for more formatting options