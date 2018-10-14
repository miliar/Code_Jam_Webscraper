def get_max_speed(my_position, another_horse_position, its_speed, dest):
    return (dest - my_position) / ((dest - another_horse_position) / its_speed)

def calc_time(position, speed, dest):
    return (dest-position)/speed

def solve( horses, dest ):
    #times = [ (dest-h[0])/h[1] for h in horses]
    #return times

    sorted_horses = sorted(horses, key=lambda x: x[0], reverse = True)

    if len(horses) == 1:
        return  get_max_speed(0, horses[0][0], horses[0][1], dest)
    
    for h in range(1, len(sorted_horses)):
        if calc_time(sorted_horses[h-1][0], sorted_horses[h-1][1], dest) > \
                calc_time(sorted_horses[h][0], sorted_horses[h][1], dest):
            # the horse in front is slower
            max_speed = get_max_speed(sorted_horses[h][0], sorted_horses[h-1][0], sorted_horses[h-1][1], dest)
            if max_speed < sorted_horses[h][1]:
                sorted_horses[h] = (sorted_horses[h][0], max_speed)
    return get_max_speed(0, sorted_horses[-1][0], sorted_horses[-1][1], dest)

rows = int(input())
for i in range(rows):
    dest, num_horses = [int(var) for var in input().split()]
    horses = []
    for h in range(num_horses):
        pos, speed = [int(var) for var in input().split()]
        horses.append( (pos,speed) ) 
    print('Case #' + str(i+1) + ': ' + str(solve(horses, dest)))
