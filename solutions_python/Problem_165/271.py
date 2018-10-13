T = int(raw_input())

for case in range(T):
    R,C,W = map(int,raw_input().split())
    if C % W == 0:
        answer = (C/W)*R+W-1
        print  "Case #{}: {}".format(case+1,answer)
    else:
        answer = (C/W)*R+W
        print "Case #{}: {}".format(case+1,answer)