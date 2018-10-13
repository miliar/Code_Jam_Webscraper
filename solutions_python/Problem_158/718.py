GABRIEL = "GABRIEL"
RICHARD = "RICHARD" 

def solve(x, r, c):
    #print(x, r, c)
    if (r * c % x == 0) and (x == 1 or x == 2 or (x == 3 and r * c > 3) or (x == 4 and r * c > 8)):
        return GABRIEL
    else:
        return RICHARD

num_test = int(input())
for i in range(num_test):
    line = [int(i) for i in input().split()]
    print("Case #{0}: {1}".format(i+1, solve(line[0], line[1], line[2])))
