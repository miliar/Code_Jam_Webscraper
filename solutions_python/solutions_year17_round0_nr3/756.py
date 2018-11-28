import Queue
import sys


#cin = open('input.txt', 'r')
#cin = open('C-small-2-attempt0.in', 'r')
cin = open('C-large.in', 'r')
#cin = sys.stdin
cout = open('output.txt', 'w')
#cout = sys.stdout

current_str_iter = None


def next_token():
    global current_str_iter

    while True:
        if current_str_iter is not None:
            token = next(current_str_iter, None)
            if token is not None:
                return token

        current_str_iter = iter(cin.readline().split())


def next_int():
    return int(next_token())


def solve(n, k):
    queue = Queue.PriorityQueue()
    queue.put((-n, 1))

    while True:
        i, nmbr = queue.get()

        while not queue.empty():
            j, nmbr2 = queue.get()
            if i != j:
                queue.put((j, nmbr2))
                break
            nmbr += nmbr2

        i = (-i) - 1

        if k <= nmbr:
            return "%i %i" % (i / 2 + i % 2, i / 2)

        k -= nmbr
        queue.put((- (i / 2 + i % 2), nmbr))
        queue.put((- (i / 2), nmbr))



def main():
    testcases = next_int()

    for tc in range(1, testcases + 1):
        n = next_int()
        k = next_int()

        result = solve(n, k)

        cout.write('Case #%i: %s\n' % (tc, str(result)))


if __name__ == '__main__':
    main()