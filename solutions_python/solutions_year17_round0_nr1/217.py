def solve():
    s, k = raw_input().split()
    k = int(k)
    s = [(int)(s[i] == '+') for i in range(len(s))]
    flipped = [0] * len(s)
    for i in range(len(s) - k):
        if(s[i] == 0):
            s[i] ^= 1
            s[i + k] ^= 1
            flipped[i] ^= 1
            flipped[i+1] ^= 1

    if s[len(s) - k] == 0 :
        flipped[len(s) - k] ^= 1
        for i in range(len(s) - k, len(s)):
            s[i] ^= 1

    if(sum(s) != len(s)):
        return "IMPOSSIBLE"

    else:
        return sum(flipped)
            
        

if __name__ == "__main__":
    t = input()
    for i in range(t):
        print("Case #%d: "%(i+1) + str(solve()))



