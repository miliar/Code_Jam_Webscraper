# chandankumar79
# import sys
data = list()
def solve():
    for i in range(1001):
        if i == int(''.join(sorted(str(i)))):
            data.append(i)
        else:
            data.append(data[len(data)-1])

# f = open("output.txt", 'w')
# sys.stdout = f

solve()
t = int(input())
for _ in range(t):
    n = int(input())
    print("Case #{}: {}".format(_+1, data[n]))

# f.close()
