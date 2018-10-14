def foo(p,q):
    r = 0
    for i in range(1,42):
       p *= 2
       if p/q >= 1 and r == 0:
           r = i
           p -= q
           p *= 2
       elif p/q >= 1:
           p -= q
           p *= 2

       if p%q == 0:
           break

    if i == 41:
       r = "impossible"

    return r


def main():
    for c in range(1,input()+1):
        print "Case #%d:"%c, foo(*map(int,raw_input().split('/')))


if __name__ == '__main__':
    main()
