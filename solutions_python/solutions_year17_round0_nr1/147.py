import sys
import bisect


def answer(text, K):
    errors = []
    if text[0] == '-':
        errors.append(0)
    for i, (before, after) in enumerate(zip(text[:-1], text[1:])):
        if before != after:
            errors.append(i+1)
    if text[-1] == '-':
        errors.append(len(text))

    steps = 0
    while True:
        if not errors:
            return steps
        last = errors[-1]
        del errors[-1]
        if not errors:
            return "IMPOSSIBLE"
        if last == errors[-1]:
            del errors[-1]
        else:
            if last < K:
                return "IMPOSSIBLE"
            else:
                steps += 1
                bisect.insort(errors, last-K)



if __name__ == "__main__":

    T = int(sys.stdin.next())
    queries = []
    for i in range(T):
        text, K = sys.stdin.next().split(' ')
        K = int(K)
        queries.append((text, K))
    for i, q in enumerate(queries):
        print "".join(["Case #", str(i+1), ": ", str(answer(*q))])

