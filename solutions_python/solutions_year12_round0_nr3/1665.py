pairs = {}
def solve(a, b):
    l1 = len(str(a))
    l2 = len(str(b))
    if(l1 == l2 == 1):
        return 0
    for n in range(a, b ):
        length = len(str(n))
        for j in range(1,l2):
            x = n / (10**j)
            y  = n /1.0/ (10**j) - x
            if(str(y)[2] == "0"):
                continue
            y2 = y * (10**(length))
            z = (y2+x)
            m = int(round(z))
            if(n < m and m >= a and m <= b  ):
                 pairs[(n,m)] = 1
    return len(pairs)


input = open("C-small-attempt0.in","rU")
out = open("number.out","w")
T = int(input.readline().rstrip('\n'))
for i in range(0, T):
    nums = input.readline().rstrip('\n').split(" ",2)
    pairs.clear()
    out.write("Case #" + str(i + 1) + ": " + str(solve(int(nums[0]), int(nums[1]))) + "\n")
out.close()