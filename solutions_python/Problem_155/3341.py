def main():
    t = int(input())
    for i in range(t):
        line = input().split()
        s = [int(j) for j in line[1]]
        to_invite = 0
        standing = s[0]
        for k in range(1, len(s)):
            # k needs to be standing
            if standing < k:
                to_invite += k-standing
                standing += k-standing
            standing += s[k]
        print("Case #{0}: {1}".format(i+1, to_invite))
    
main()