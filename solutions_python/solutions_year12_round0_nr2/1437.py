
def best(score):
    return min(10, score, int((score + 2) / 3.0))

def best_surprising(score):
    return min(10, score, int((score + 4) / 3.0))

def solve(S, p, scores):
    r = 0
    for score in scores:
        if best(score) >= p:
            r += 1
        elif best_surprising(score) >= p and S > 0:
            S -= 1
            r += 1
    return r

if __name__ == '__main__':
    n = input()
    for i in range(n):
        line = raw_input().split(' ')
        S = int(line[1])
        p = int(line[2])
        scores = map(int, line[3:])
        print 'Case #%s:' % (i+1), solve(S, p, scores)
        
