def run_case():
    engines = set()
    result = 0
    engine = None
    queries = []
    
    S = int(input())
    for _ in range(S):
        engines.add(input())

    Q = int(input())
    for _ in range(Q):
        queries.append(input())

    left = engines.copy()
    for q in queries:
        if q in left:
            left.discard(q)

        if not left:
#            print(q)
            result += 1
            left = engines.copy()
            left.discard(q)

#    print(left.pop())


    return result

def main():
    N = int(input())
    for i in range(N):
        r = run_case()
        print('Case #%d: %d' % (i+1, r))


main()
