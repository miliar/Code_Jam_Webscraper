def try_candidate(start, end, candidate):
    if start > end or len(candidate) == 0:
        return 0
    if len(candidate) == 1:
        return end - start
    min_gold = -1
    for index in range(len(candidate)):
        prison = candidate[index]
        gold = end - start + try_candidate(start, prison - 1, candidate[:index]) + try_candidate(prison + 1, end, candidate[index + 1:])
        if min_gold == -1 or min_gold > gold:
            min_gold = gold
    return min_gold

def main():
    for case in range(input()):
        P, Q = map(int, raw_input().split())
        candidate = list(map(int, raw_input().split()))
        candidate.sort()
        min_gold = try_candidate(1, P, candidate)
        print "Case #%d: %d" % (case + 1, min_gold)
        
main()
