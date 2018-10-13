import math

def omino(x, r, c):
    if (r*c % x != 0):
        return "RICHARD"
    elif (x == 1 and r == 1 and c == 1):
        return "GABRIEL"
    elif (max_omino(x,r,c)):
        return "RICHARD"
    elif(x == 4 and ((r == 2 and c == 4) or (r == 4 and c == 2))):
        return "RICHARD"
    else:
        return "GABRIEL"

def max_omino(x,r,c):
    for i in range(int(math.ceil(x/2)+1)):
        if ((x-i > r or i >= c) and (x-i > c or i >= r)):
            return True
    return False


in_file = "D-small-attempt5.in"
out_file = "output.txt"

with open(in_file, "r") as f_in:
    with open(out_file, "w") as f_out:
        tests = int(f_in.readline())
        print(tests)
        
        for i in range(1,tests+1):
            values = f_in.readline().strip().split(" ")
            values = list(map(int, values))
            print(values)
            print("Case #{}: {}".format(i, omino(values[0], values[1], values[2])))
            f_out.write("Case #{}: {}\n".format(i, omino(values[0], values[1], values[2])))
            
'''
If it is possible, GABRIEL wins,
if not, RICHARD wins
'''
