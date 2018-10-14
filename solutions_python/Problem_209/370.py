from math import pi

def score(stack):
    max_r = 0
    rh = 0.0
    for i in range(len(stack)):
        max_r = max(max_r, stack[i][0])
        rh += stack[i][0] * stack[i][1]
    return max_r * max_r * pi + 2 * pi * rh

class Pancakes(object):
    def __init__(self):
        self.Stack = []
        self.n = 0
        self.best_score = 0.0

    def into(self, x):
        self.Stack.append(x)
        self.n += 1

    def out(self):
        self.Stack.sort(key=lambda x: x[0]*x[1])
        score_0 = score(self.Stack[1:])
        score_1 = score(self.Stack[:1] + self.Stack[2:])
        # if score_0 >= score_1:
        #     self.best_score = max(self.best_score, score_0)
        #     self.Stack.pop(0)
        # else:
        #     self.best_score = max(self.best_score, score_1)
        #     self.Stack.pop(1)
        self.Stack.pop(0)
        self.best_score = max(self.best_score, score_0, score_1)
        self.n -= 1

    def score(self):
        self.best_score = max(self.best_score, score(self.Stack))
        return self.best_score

def solve(K, N, RH):
    Stack = []
    RH = sorted(RH, key=lambda x: x[0])
    pancakes = Pancakes()
    for i in range(K):
        pancakes.into(RH[i])
    pancakes.score()
    for i in range(K, N):
        pancakes.into(RH[i])
        pancakes.out()
    return pancakes.score()

T = input()
for t in range(1, T+1):
    N, K = map(int, raw_input().split())
    RH = []
    for n in range(N):
        RH.append(map(int, raw_input().split()))
    print 'Case #%d: %f'%(t, solve(K, N, RH))
