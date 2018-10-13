import math

def sol(room, customer):
    while customer != 1:
        if room == customer:
            return [0, 0]

        if room % 2 == 1:
            room = (room - 1) / 2
            customer = customer / 2
        else:
            if customer % 2 == 0:
                room = room / 2
            else:
                room = room / 2 - 1
            customer = customer / 2

    if room % 2 == 1:
        return [ (room - 1) / 2 ] * 2
    else:
        return [ room / 2, room / 2 - 1]

t = int(raw_input())  # read a line with a single integer
for task in xrange(1, t + 1):
    room, customer = [int(num) for num in raw_input().split(" ")]

    ret = sol(room, customer)
    print "Case #{}: {} {}".format(task, ret[0], ret[1])



