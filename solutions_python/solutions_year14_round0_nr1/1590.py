
def solve():
    r1 = input()
    m1 = list()
    for i in xrange(4):
        m1.append(set(raw_input().strip().split()))
    r2 = input()
    m2 = list()
    for i in xrange(4):
        m2.append(set(raw_input().strip().split()))
    number = m1[r1-1].intersection(m2[r2-1])
    if len(number) == 1:
        print list(number)[0]
    elif len(number) > 1:
        print "Bad magician!"
    else:
        print "Volunteer cheated!"

def main():
    n = input()
    for i in xrange(n):
        print "Case #%s: " %(i+1), 
        solve()

if __name__=='__main__':
    main()
