#!/usr/bin/env python

def find_gt(array, x):
    'Find leftmost value greater than x'
    from bisect import bisect_right
    i = bisect_right(array, x)
    if i != len(array):
        return array[i]
    raise ValueError

def find_first_inferior(A, B):
    "find the first index i where A[i] < B[i]"
    for i in range(len(A)):
        if A[i] < B[i]:
            return i
    return None

def deceitful_optimal(sorted_naomi, sorted_ken):
    """
    Naomi's optimal strategy is ensuring that naomi's blocks dominates ken's
    so that sorted_naomi[i] > sorted_ken[i] for all i
    by pairing naomi's lightest block to ken's heaviest block by
    giving a false weight
    """
    index = find_first_inferior(sorted_naomi, sorted_ken)
    while index != None:
        "fool Ken into wasting his heaviest block"
        del sorted_naomi[0]
        del sorted_ken[-1]
        index = find_first_inferior(sorted_naomi, sorted_ken)
    return len(sorted_naomi)

def war_optimal(sorted_naomi, sorted_ken):
    """
    Naomi's optimal score in regular War game
    Ken's optimal strategy:
    * Given Naomi's block, pick the smallest block heavier than Naomi's
    * If no such block exists, throw the lightest as a scapegoat.
    """
    ken_optimal_score = 0
    for weight in sorted_naomi:
        try:
            next_weight = find_gt(sorted_ken, weight)
            ken_optimal_score = ken_optimal_score + 1
        except ValueError:
            next_weight = sorted_ken[0]
        sorted_ken.remove(next_weight)
    return len(sorted_naomi) - ken_optimal_score

if __name__ == "__main__":
    import sys
    from string import strip, split
    cases = int(sys.stdin.readline())
    for i in range(1, cases+1):
        num = int(sys.stdin.readline())
        naomi = map(lambda x: float(x), split(sys.stdin.readline()))
        ken   = map(lambda x: float(x), split(sys.stdin.readline()))
        print "Case #%d:" %(i),
        print deceitful_optimal(sorted(naomi), sorted(ken)),
        print war_optimal(sorted(naomi), sorted(ken))
