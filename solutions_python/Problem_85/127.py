#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
import numpy
import scipy.optimize
#import psyco

def readnumbers(f, dtype=int):
    return [dtype(x) for x in f.readline().strip().split()]

class Solution:
    def main(self, filename):
        self.dataset_stream = open(filename, 'r')
        line = self.dataset_stream.readline()
        self.cases_left = int(line)
        print "File contains %d testcases." % (self.cases_left)

        self.caseno = 1
        while self.cases_left > 0:
            self.cases_left -= 1
            self.readcase()
            self.printcase()
            self.solve()
            self.printsolution()
            self.caseno += 1

    def readcase(self):
        numbers = readnumbers(self.dataset_stream)
        self.L = numbers[0]
        self.t = numbers[1]
        self.N = numbers[2]
        self.C = numbers[3]
        self.a = numbers[4:]
    
    def printcase(self):
        print "stars(N) =", self.N, "  boosters(L) =", self.L
        print "booster_build(t) =", self.t
        #print "C=", self.C, "a=", self.a
    
    def solve(self):
        L, t, N, C, a = self.L, self.t, self.N, self.C, self.a
        distances = numpy.zeros(N)
        k = 0
        while 0 in distances:
            for i in xrange(len(a)):
                s1 = k*C+i
                #s2 = k*C+i+1
                if s1 < len(distances):
                    distances[s1] = a[i]
            k += 1
        #print repr(distances)

        self.answer = self.answer = sum(distances) * 2

        def travel_time(distances, boosters, t, N):
            tt = 0
            for pos in xrange(N):
                if boosters[pos] == 0:
                    tt += distances[pos]*2
                else:                    
                    if tt >= t:
                        tt += distances[pos]
                    else:
                        without = distances[pos]*2
                        if without <= (t - tt):
                            tt += without
                        else:
                            dist_without_booster = (t-tt)*0.5
                            dist_left = distances[pos] - dist_without_booster
                            tt = t + dist_left
            #print boosters, tt
            return tt

        di = []
        for i, d in enumerate(distances):
            di.append((d, i))
        def cmpf(a, b):
            if a[0] != b[0]:
                return -cmp(a[0], b[0])
            else:
                return -cmp(a[1], b[1])
        di.sort(cmpf)

        def place_booster(di, distances, boosters, t, N, m):
            time = m
            last_d = di[0][0]
            booster_location = 0
            for d, i in di:
                b = boosters.copy()
                if b[i] == 1:
                    continue
                b[i] = 1
                new_t = travel_time(distances, b, t, N)
                if new_t > time:
                    if d > (last_d - 10000):
                        break
                else:
                    #print "loc", i, new_t, time
                    booster_location = i
                    time = new_t
                last_d = d
            return booster_location, time

        if L == 0:
            return
        elif L == 1:
            boosters = numpy.zeros(N)
            pos, new_t = place_booster(di, distances, boosters, t, N, self.answer)
            self.answer = min(new_t, self.answer)
        elif L == 2:
            boosters = numpy.zeros(N)
            pos, new_t = place_booster(di, distances, boosters, t, N, self.answer)
            #print "booster1", pos, new_t, self.answer
            self.answer = min(new_t, self.answer)
            boosters[pos] = 1
            pos, new_t = place_booster(di, distances, boosters, t, N, self.answer)
            self.answer = min(new_t, self.answer)
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %d" % (self.caseno, self.answer)
        sys.stderr.flush()

if __name__ == '__main__':
    #psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
