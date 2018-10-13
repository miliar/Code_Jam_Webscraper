from time import clock
import sys
# stderr isn't piped to a.out when we do  (py3 a.py < a.in) > a.out
print = lambda *s: sys.stderr.write(" ".join(str(m) for m in s)+"\n")

#---------------------------------------------

"""
lemma:
    in an ideal config every arrow has to point to another arrow
proof:
    if an arrow does not satisfy that, it would point to an edge
    and is an instant loss

in fact, this might be the only condition we have to satisfy.
    and because we cannot place/remove arrows, this would make
    the problem easy! (O(R*C))

well, per arrow we also have to search the corresponding row
    and column, so we have O(R+C) effort per cell,
    in total O((R*C)*(R+C))

we could do clever caching, but i think this suffices for the big case. :)

"""



def run(superdata):

    r,c,data = superdata
    cnt = 0

    for i in range(r):
        for j in range(c):

            # no arrow: nothing to do
            if data[i][j] == ".":
                continue

            # arrow pointing to arrow: nothing to do

            if data[i][j] == "^":
                if any([ data[y][j] != "." for y in range(i-1,-1,-1) ]):
                    continue

            if data[i][j] == "v":
                if any([ data[y][j] != "." for y in range(i+1,r) ]):
                    continue

            if data[i][j] == "<":
                if any([ data[i][x] != "." for x in range(j-1,-1,-1) ]):
                    continue

            if data[i][j] == ">":
                if any([ data[i][x] != "." for x in range(j+1,c) ]):
                    continue

            # arrow pointing to not arrow:
            #   find another arrow to point to
            #   if none found, ret IMPOSSIBLE

            if (any([ data[i][x] != "." for x in range(c) if j != x ])
                    or any([ data[y][j] != "." for y in range(r) if i != y ])):
                cnt += 1
                continue

            return "IMPOSSIBLE"

    return cnt

#---------------------------------------------

def read_case():

    r,c = [int(n) for n in input().split()]
    a = []
    for i in range(r):
        a.append(input())

    return (r, c, a)

for i in range(int(input())):
    outstr = "Case #"+str(i+1)+": "+str(run(read_case()))
    print(outstr+" @ t="+str(clock()))
    sys.stdout.write(outstr+"\n")
