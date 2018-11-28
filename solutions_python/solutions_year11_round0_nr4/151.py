def cyclical_groups(z):
    groups = []
    for i in range(len(z)):
        x = z[i]
        if x < 0:
            continue
        z[i] = -1
        k = [i]
        while x != i:
            k.append(x)
#            print z, x
            y = z[x]
            z[x] = -1
            x = y
        groups.append(k)
    return groups
        
def gorosort(z):
    return sum(map(lambda x:len(x)*(len(x)>1), cyclical_groups(z)))
        
def main():
    cases = int(raw_input())
    for case in range(cases):
        n = raw_input()
        z = map(lambda x: int(x)-1, raw_input().split(" "))
        print "Case #%d: %.6f" % (case+1, gorosort(z))

main()
