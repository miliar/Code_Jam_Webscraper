from DomainModel.TestCase import TestCase


class R1B:
    def Solve(self):
        from collections import defaultdict
        from itertools import permutations
        import math
        import networkx as nx

        def hasInt(a,b):
            if int(a)!=int(b):
                return True
            if int(a)==a or int(b)==b:
                return True
            return False

        def overlap(a1,b1,a2,b2):
            if a2<=b1 and b2>=a1:
                return hasInt(a1,b1) and hasInt(a2,b2)
            return False

        tests = int(input())
        for test in range(tests):
            n, p = list(map(int, input().split()))
            r = list(map(int, input().split()))
            minr = [0.9 * x for x in r]
            maxr = [1.1 * x for x in r]
            q = []
            qq1=[]
            qq2 = []
            for i in range(n):
                a = list(map(int, input().split()))
                q.append(a)
                qq1.append([x / maxr[i] for x in a])
                qq2.append([x / minr[i] for x in a])
            cnt = 0
            if n == 1:
                for i in range(p):
                    if hasInt(qq1[0][i],qq2[0][i]):
                        cnt+=1
            # elif n == 2:
            #     for perm in permutations(range(p)):
            #         sc=0
            #         for i in range(p):
            #             if overlap(qq1[0][i],qq2[0][i],qq1[1][perm[i]],qq2[1][perm[i]]):
            #                 sc+=1
            #         cnt = max(cnt,sc)
            else:
                g = nx.DiGraph()
                for j in range(p):
                    g.add_edge('x', '{}-{}'.format(0,j), capacity=1.0)
                    g.add_edge('{}-{}'.format(n-1, j), 'y', capacity=1.0)

                for i in range(n-1):
                    for j in range(p):
                        for k in range(p):
                            if overlap(qq1[i][j], qq2[i][j], qq1[i+1][k], qq2[i+1][k]):
                                g.add_edge('{}-{}'.format(i, j), '{}-{}'.format(i+1, k), capacity=1.0)

                flow_value, flow_dict = nx.maximum_flow(g, 'x', 'y')
                cnt=int(flow_value)

            print("Case #{}: {}".format(test + 1, cnt))

    def Tests(self):
        yield TestCase("""6
2 1
500 300
900
660
2 1
500 300
1500
809
2 2
50 100
450 449
1100 1101
2 1
500 300
300
500
1 8
10
11 13 17 11 16 14 12 18
3 3
70 80 90
1260 1500 700
800 1440 1600
1700 1620 900""", """Case #1: 1
Case #2: 0
Case #3: 1
Case #4: 0
Case #5: 3
Case #6: 3
        """)
