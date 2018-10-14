# Code Jam 2015
# Contestant: Rincewind
# Qualification Round A: Standing Ovation

def standing_ovation():
    t = input()
    f = open('output.txt','w')
    for z in xrange(t):
        a,b = raw_input().split()
        a = int(a); b = map(int,list(str(b)));
        s = 0; ans = 0
        for x in xrange(a+1):
            if s < x and b[x]:
                ans += (x-s)
                s += b[x] + (x-s)
            else:
                s += b[x]
        f.write("Case #%i: %i\n" % (z+1,ans))

standing_ovation()