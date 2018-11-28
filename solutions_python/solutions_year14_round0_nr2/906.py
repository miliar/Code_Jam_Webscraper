def ans(C,F,X):
        ps = 2
        t=0
        while True:
                if X/ps <= C/ps +X/(ps+F):
                        return t + X/ps
                else:
                        t+=C/ps
                        ps+=F
		

T = int(raw_input())
for case in range(1, T + 1):
        C,F,X = map(float, raw_input().split())
        print "Case #%d: " % (case), ans(C,F,X)
