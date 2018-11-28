import re
from math import sqrt

def get_paint(r0,x):
    print "r%d is %d" % (x,r0 + 2*x)
    ans = 2 * r0 * x - x + 2 * (x ** 2)
    print "%d on %d uses %d" % (r0,x,ans)
    return ans

def check_game(state):
    r0,t = state
    x = 3 + 2 * r0
    num = -x + sqrt(x ** 2 + 8 * t)
    guess = num / 4.0
    guess = int(guess - 1)
    while get_paint(r0,guess) <= t:
        guess += 1
    return guess - 1


        

def read_game(f):
    dims = re.split(" ",f.readline())
    return int(dims[0]), int(dims[1])    
    

def main():
    output = []
    with open("A-sample.in","r") as f:
        trials = f.readline()
        for i in range(int(trials.strip())):
            state = read_game(f)
            outline = "Case #%d: %d" % (i+1, check_game(state))
            print outline
            output.append(outline)
    with open("A.out","w") as f:
        f.write("\n".join(output))


if __name__ == "__main__":
    main()