def solve(T, S):
    ans = 0
    standing = 0
    for i in range(T+1):
        if standing < i:
            friend = i - standing
            ans += friend
            standing += friend
        standing += int(S[i])
    return ans

def main():
    N = int(raw_input())
    for i in range(N):
        T, S = raw_input().split()
        print "Case #%d: %d" % (i+1, solve(int(T), S))

if __name__ == "__main__":
    main()