from datastructs import Queue


class solver:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.solutions = {}

        q = Queue()

        p = "+" * n
        self.solutions[p] = 0
        #print(p, self.solutions[p])
        q.enqueue(p)

        while(not q.isEmpty()):
            p = q.dequeue()

            for i in range(0, n-k+1):
                p1 = p
                for j in range(i, i+k):
                    p1 = p1[:j] + ('+' if p1[j] == '-' else '-') + (p1[j+1:] if j < n-1 else '')
                if p1 not in self.solutions:
                    self.solutions[p1] = self.solutions[p] + 1
                    q.enqueue(p1)
                    #print(p1, self.solutions[p1])
                else:
                    if (self.solutions[p1] > self.solutions[p] + 1):
                        self.solutions[p1] = self.solutions[p] + 1
                        q.enqueue(p1)
                        #print(p1, self.solutions[p1], "replace")

    def solve(self, p):
        return self.solutions[p] if p in self.solutions else "IMPOSSIBLE"


T = int(input())

for i in range(1, T+1):
    # n = int(input())
    p, k = [s for s in input().split(" ")]
    k = int(k)
    # s = input()

    #print(p, k)

    s = solver(len(p), k)
    x = s.solve(p)

    print("Case #{}: {}".format(i, x))
