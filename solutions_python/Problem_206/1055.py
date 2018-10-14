class X():
    def __init__(self, horses, D):
        self.horses = horses
        self.D = D

    def run(self):
        t = -1
        pre_k = 0
        pre_s = 0
        for h in self.horses:
            if t == -1:
                t = (self.D - h[0]) / h[1]
                pre_k = h[0]
                pre_s = h[1]

            if t * (h[1] - pre_s) < pre_k - h[0]:
                t = (self.D - h[0]) / h[1]
                pre_k = h[0]
                pre_s = h[1]

        return self.D / t


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    D, N = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

    horses = []
    for j in range(N):
        pos, speed = [float(s) for s in input().split(" ")]
        horses.append((pos, speed))
        horses.sort(key=lambda x: x[0], reverse=True)

    g = X(horses, float(D))

    cc = g.run()
    print("Case #{}: {}".format(i, cc))
