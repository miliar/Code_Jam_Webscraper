def foo(a,b,k):
    count = 0
    for i in range(a):
        for j in range(b):
            if i&j < k:
                count += 1
    return count

def main():
    for c in range(1,input()+1):
        print "Case #%d:"%c, foo(*map(int,raw_input().split()))

if __name__ == '__main__':
    main()
