def solve(people):
    needed = 0
    standing = 0
    for shy, p in enumerate(people):
        p = int(p)
        if standing < shy:
            needed += shy - standing
            standing += shy - standing
        standing += p
    return needed

def main():
    n = int(raw_input())
    for c in range(1, n + 1):
        needed = solve(raw_input().split()[1])
        print 'Case #%d: %d' % (c, needed)
    
if __name__ == "__main__":
  main()
    