import sys
for C in range(1, int(sys.stdin.readline())+1):
    answer = 0
    N = sys.stdin.readline().strip()
    n = long(N)
    l = [int(c) for c in N]
    for j in reversed(range(len(N))):
        if j == 0:
            if l[j] < 1:
                answer = "9" * (len(N)-1)
            else:
                answer = "".join(map(str, l))
        else:
            if l[j] < 1 or l[j] < l[j-1]:
                for m in range(j, len(N)):
                    l[m] = 9
                l[j-1] = l[j-1] - 1
    print "Case #%s: %s" % (C, answer)

"""
999
899
889
888
799
789
788
779
778
777
699
689
688
679
678
677
669
668
667
666


1
2
3
4
5
6
7
8
9
11
12
13
14
15
16
17
18
19
22
23
24
25
26
27
28
29
33
34
35
36
37
38
39
44

"""