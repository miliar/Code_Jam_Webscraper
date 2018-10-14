
def is_tidy(n):
    sn = str(n)
    return ''.join(sorted(sn)) == sn

def solve(bound):
    current = bound
    while not is_tidy(current):
        current -= 1
    return current

def main():
    cases = int(input())
    for i in range(1, cases+1):
        bound = int(input())
        print("Case #%d: %s" % (i, solve(bound)))

if __name__ == '__main__':
    main()
