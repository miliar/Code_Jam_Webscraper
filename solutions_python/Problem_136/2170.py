
# cookie clicker alpha

INPUT = "B-large.in"
OUTPUT = "out.txt"

def main():
    in_f = open(INPUT, 'r')
    out_f = open(OUTPUT, 'w')
    T = int(in_f.readline())
    for case in range(1, T+1):
        C, F, X = map(float, in_f.readline().split())
        time = solve(C, F, X)
        out_f.write("Case #" + str(case) + ": " + str(time) + "\n")
    in_f.close()
    out_f.close()

# c is price of farm
# f is farm cookie rate
# x is goal number of cookies
def solve(c, f, x):
    time = 0.0
    cookies = 0.0
    cps = 2.0 # cookies per second (base rate)
    while cookies < x:
        time += (c - cookies)/cps
        cookies = c
        goal_time = (x - cookies)/cps
        # cookies + cps*t = (cps + f)*t
        break_even_time = cookies/f
        if break_even_time <= goal_time:
            cookies = 0.0
            cps += f
        else:
            return time + goal_time


main()
