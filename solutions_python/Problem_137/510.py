import numpy as np


def load_data():
    with open("a-small.txt") as f:
        with open("answer.txt", 'w') as ans:
            T = int(f.readline().split()[0])
            for case in range(T):
                R, C, M = [int(i) for i in f.readline().split()]
                ans.write("Case #{}:\n{}".format(case + 1, solve_one(R, C, M)))
                #print "RCM", R, C, M
                #print "Case #{}:\n{}\n".format(case + 1, solve_one(R, C, M))


def solve_one(R, C, M):
    (res, sol) = rec_solve(R, C, M, [(0, 0)], add_neighbours((0, 0), {(0, 0)}, R, C))
    #print sol
    if not res:
            return "Impossible\n"
    return Mines(sol, R, C).__str__()


def is_inside(i, j, R, C):
    return 0 <= i < R and 0 <= j < C


def add_neighbours((i, j), deja_test, R, C):
    """ add the neighbours of n to deja_test """
    for ii in range(i - 1, i + 2):
        for jj in range(j - 1, j + 2):
            if is_inside(ii, jj, R, C) and (ii != i or jj != j):
                    deja_test.add((ii, jj))
    return deja_test


def neighbours((i, j), l, R, C):
    """ return the neighbours, not in l """
    res = []
    for ii in range(i - 1, i + 2):
        for jj in range(j - 1, j + 2):
            if is_inside(ii, jj, R, C) and (ii != i or jj != j):
                if (ii, jj) not in l:
                    res.append((ii, jj))
    return res


def rec_solve(R, C, M, l, deja_test):
    #print l, deja_test
    #raw_input()
    n = R * C - len(deja_test)
    if len(l) == 1 and R * C - 1 == M:
        return(True, {(0, 0)})
    if n == M:
        return (True, deja_test)
    elif n < M:
        return (False, None)
    else:
        for n in neighbours(l[-1], l, R, C):
            deja_test_temp = set(deja_test)
            l_temp = list(l)
            l_temp.append(n)
            add_neighbours(n, deja_test_temp, R, C)
            (res, sol) = rec_solve(R, C, M, l_temp, deja_test_temp)
            if res:
                return (res, sol)
        return(False, None)


class Mines():
    def __init__(self, deja_test, R, C):
        self.mat = np.zeros((R, C), dtype="uint8")
        for (i, j) in deja_test:
            self.mat[i, j] = 1

    def __str__(self):
        res = ""
        for i, r in enumerate(self.mat):
            ligne = ""
            for j, l in enumerate(r):
                if i == 0 and j == 0:
                    ligne += 'c'
                else:
                    if self.mat[i, j] == 0:
                        ligne += '*'
                    else:
                        ligne += '.'
            res += ligne + "\n"
        return res
        


def main():
    load_data()

if __name__ == "__main__":
    main()
