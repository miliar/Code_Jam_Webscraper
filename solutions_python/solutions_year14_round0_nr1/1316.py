import sys

def solve(x, Ax, y, Ay):
    guess = set.intersection(set(Ax[x-1]), set(Ay[y-1]))
    if len(guess) == 1:
        return guess.pop()
    elif len(guess) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


def main():
    def read_matrix():
        A = []
        for i in range(4):
            A.append(map(int, sys.stdin.readline().split()))
        return A

    T = int(sys.stdin.readline())
    for k in xrange(T):
        x = int(sys.stdin.readline())
        Ax = read_matrix()
        y = int(sys.stdin.readline())
        Ay = read_matrix()
        answer = solve(x, Ax, y, Ay)
        print "Case #{0}: {1}".format(1 + k, answer)
        

if __name__ == '__main__':
    main()
