__author__ = 'artiom'

def solve(first_guess, A, second_guess, B):
    result = set(A[first_guess - 1]) & set(B[second_guess - 1])
    if len(result) == 0:
        return 'Volunteer cheated!'
    if len(result) > 1:
        return 'Bad magician!'
    return list(result)[0]

def parse_input(filename='A.in'):
    f = open(filename)
    ncases = int(f.readline())

    for ncase in range(ncases):
        first_guess = int(f.readline())

        A = [[] for i in range(4)]
        for i in range(4):
            A[i] = map(int, f.readline().split())

        second_guess = int(f.readline())

        B = [[] for i in range(4)]
        for i in range(4):
            B[i] = map(int, f.readline().split())

        print 'Case #' + str(ncase + 1) + ': ' + str(solve(first_guess, A, second_guess, B))

    f.close()

if __name__ == "__main__":
    parse_input('A-small-attempt0.in')