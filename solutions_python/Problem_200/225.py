numbers = [((10**n) - 1) / 9 for n in range(20, 0, -1)]

def solve():
    n = input()
    res = 0
    addnum = 0
    for num in numbers:
        while(addnum < 9 and res + num <= n):
            res += num
            addnum += 1
    return res
    
if __name__ == "__main__":
    t = input()
    for i in range(t):
        print("Case #%d: "%(i+1) + str(solve()))



