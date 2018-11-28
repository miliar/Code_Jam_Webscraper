

def game_func(r, t):
    circle = 0;
    while(1):
        white_r = r
        black_r = r+1
        area_of_black_r = black_r * black_r
        area_of_white_r = white_r * white_r
        paint_needed = area_of_black_r - area_of_white_r
        if paint_needed > t:
            break;
        else:
            circle = circle + 1
            t = t - paint_needed
            r = r + 2


    return circle


input = open('A-small-attempt0.in', 'r')
T = int(input.readline())
for i in range(0, T):
    temp = input.readline()
    r = int(temp.split(" ")[0])
    t = int(temp.split(" ")[1])
    result = game_func(r, t)
    print "Case #" + str(i+1) + ": " + str(result) 
    
    
