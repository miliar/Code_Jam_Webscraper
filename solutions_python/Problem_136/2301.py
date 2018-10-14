import sys

t = int(sys.stdin.readline().strip())

def cookies(c, f, x):
    rate = 2.0
    turns = 0
    while(1):
        turns_til_farm = c/rate
        turns_til_win = x/rate
        turns_til_win_one_more_farm = c/rate + x/(rate + f)
        if turns_til_win < turns_til_win_one_more_farm:
            turns += turns_til_win
            return round(turns, 7)
        else:
            turns += turns_til_farm
            rate += f
     
for test_num in range(1, t + 1):
    c, f, x = sys.stdin.readline().strip().split()
    c = float(c)
    f = float(f)
    x = float(x)
    print "Case #" + str(test_num) + ": " + str(cookies(c, f, x))
    
   
