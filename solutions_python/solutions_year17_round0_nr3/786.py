def choose(open_spaces, num_to_place):
    placed = (open_spaces + 1) / 2
    if num_to_place == 1:
        return max([open_spaces - placed, placed - 1]), min([open_spaces - placed, placed - 1])
    if open_spaces % 2 == 0:
        if num_to_place % 2 == 0:
            return choose(placed, (num_to_place / 2))
        else:
            return choose(placed - 1, (num_to_place) / 2)
    else:
        return choose(placed - 1, (num_to_place / 2))
    
t = int(raw_input())  # read a line with a single integer
for k in xrange(1, t + 1):
    spaces, num = raw_input().split(' ')  # read a list of integers, 2 in this case
    spaces, num = int(spaces), int(num)
    first, second = choose(spaces, num)
    print "Case #{}: {} {}".format(k, first, second)
