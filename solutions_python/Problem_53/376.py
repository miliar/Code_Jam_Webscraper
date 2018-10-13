#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from memoize import memoize

MAX_N = 30

if __name__ == "__main__":
    filename = sys.argv[1]
    input = open(filename)
    t = int(input.readline())

    needed = dict()   #  k -> set[n1,n2,..]    dla wszystkich żądań
    max_k = 0         # największe potrzebne k
    queries = []      # wszystkie pary (n,k) w kolejności wejścia

    for case_no in xrange(1,t+1):
        n, k = [ int(v) for v in input.readline().split() ]
        n -= 1   # przejście na indeksowanie od zera
        if not k in needed:
            needed[k] = set()
        needed[k].add(n)
        queries.append( (n,k) )
        if k > max_k:
            max_k = k

    solutions = dict()  # (n,k) -> True/False

    # Właściwe rozw.
    current_k = 0
    current_state = [ False for i in xrange(0,MAX_N+1) ]
    while current_k <= max_k:
        # Wyliczamy ile jest wiodących True:
        first_false = 0
        while first_false < len(current_state) and current_state[first_false]:
            first_false += 1
        #print "Stage", current_k, "State", current_state, "first_false", first_false
        # Zapisujemy rozwiązania
        if current_k in needed:
            for current_n in needed[current_k]:
                solutions[ (current_n, current_k) ] = (current_n < first_false)
        #print "Solut", solutions
        # Kolejna iteracja danych:
        for i in xrange(0, min(first_false+1, len(current_state))):
            current_state[i] = not current_state[i]
        current_k += 1

    # Wypis odpowiedzi
    for case_no in xrange(1,t+1):
        is_on = solutions[ queries[case_no-1] ]
        print "Case #%d: %s" % (case_no, is_on and "ON" or "OFF")
