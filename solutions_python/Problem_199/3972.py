import sys
from itertools import permutations

class Pancake:

    order = []
    k = 0
    solution = []
    solutions = []

    def __init__(self, order, k):
        self.order = order
        self.k = k
        self.solution = [True for x in xrange(0, len(order))]

    def isCorrect(self, data):
        return data == self.solution

    def flip(self, pos, order):
        for i in xrange(pos, pos + self.k):
            order[i] = not order[i]
        return order

    def applyPermutation(self, combo):
        temp = self.order[:]
        if self.isCorrect(temp):
            return 0
        count = 1
        for t in combo:
            temp = self.flip(t, temp)
            if self.isCorrect(temp):
                return count
            count = count + 1
        return -1


    def solve(self):
        pos = len(self.order) - self.k + 1
        indexes = []
        solutions = []
        for i in xrange(0, pos):
            indexes.append(i)
        for combo in permutations(indexes):
            test = self.applyPermutation(combo)
            if test >= 0:
                solutions.append(test)
        if len(solutions) > 0:
            return str(min(solutions))
        else:
            return "IMPOSSIBLE"

def main():
    f = open(sys.argv[1], 'r')
    f2 = open('output.txt', 'w')
    lines = f.readlines()
    f.close()
    counter = 1
    for line in lines:
        if counter == 1:
            counter = counter + 1
            continue
        parts = line.split(' ')
        orderString = list(parts[0])
        order = [x == '+' for x in orderString]
        k = int(parts[1])
        p = Pancake(order, k)
        result = p.solve()
        f2.write("Case #{0}: {1}\n".format(str(counter - 1), result))
        counter = counter + 1
    f2.close()


if __name__ == "__main__":
    main()
