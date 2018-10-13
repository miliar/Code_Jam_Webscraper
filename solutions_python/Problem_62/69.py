#!/usr/bin/env python



if __name__ == '__main__':
    test_cases = int(raw_input())
    for case in xrange(1, test_cases+1):
        n = int(raw_input())
        points = []
        for i in range(n):
            points.append(tuple(map(int, raw_input().split(' '))))
        intersections = 0
        for index1 in xrange(0, n):
            for index2 in xrange(index1+1, n):
                if points[index1][0] < points[index2][0] and points[index1][1] > points[index2][1]:
                    intersections +=1
                elif points[index1][0] > points[index2][0] and points[index1][1] < points[index2][1]:
                    intersections += 1
        
        print "Case #%d: %d" % (case, intersections)
        