import sys
from sets import Set


def is_tidy(N):
    num_list = map(int, list(str(N)))
    return num_list == sorted(num_list)


def answer(N):
    k = N
    while k > 0:
        if is_tidy(k):
            return k
        else:
            k -= 1
    assert False

def answer2(N):
    k = N
    if is_tidy(N):
        return N
    while k % 10 != 9:
        if is_tidy(k):
            return k
        else:
            k -= 1

    return 10 * answer2(int(k/10)) + 9



if __name__ == "__main__":

    T = int(sys.stdin.next())
    queries = []
    for i in range(T):
        queries.append(int(sys.stdin.next()))
    for i, q in enumerate(queries):
        print "".join(["Case #", str(i+1), ": ", str(answer2(q))])

