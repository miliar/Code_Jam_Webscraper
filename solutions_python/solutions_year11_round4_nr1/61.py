
def compare(a,b):
    (b1,e1,w1) = a
    (b2,e2,w2) = b
    return cmp(w1,w2)

def solve(xxx):
    (x,s,r,t,n) = map(float,raw_input().split())
    wa = []
    last_e=0.0
    for i in range(int(n)):
        (b,e,w) = map(float,raw_input().split())
        wa.append((last_e,b,0))
        wa.append((b,e,w))
        last_e = e
    wa.append((last_e, x, 0))
    wa.sort(compare)

    used_time = 0.0
    t_rem = t
    for (b,e,w) in wa:
        l = e - b

        drt = l/(w+r)
        if (drt < t_rem):
            # run all range
            t_rem = t_rem - drt
            used_time = used_time + drt
        else:
            # run as long as i can
            l_run = (w+r)*t_rem
            dwt = (l-l_run)/(s+w)
            used_time = used_time + dwt + t_rem
            t_rem = 0
        
    print "Case #%s: %s"% (xxx, used_time)



def main():
    t = int(raw_input())
    for i in range(t):
        solve(i+1)

main()
