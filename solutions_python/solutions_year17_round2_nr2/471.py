def findOrder(order):
    order = sorted(order, key=lambda order :order[1])
    order.reverse()
    return order

def conflict(placed, next):
    return (placed == next)

def placeFirstAndLast(places, order):
    order = findOrder(order)
    r1,r2 = order[0:2]
    # 2 of same type left
    name1, num1 = r1
    name2, num2 = r2
    if(num1 > 1):
        return "IMPOSSIBLE"
    elif conflict(name1, name2):
        return "IMPOSSIBLE"
    elif conflict(name1, places[1]):
        if conflict(name1, places[-2]):
            return "IMPOSSIBLE"
        elif conflict(name2, places[1]):
            return "IMPOSSIBLE"
        else:
            places[0] = name2
            places[-1] = name1
            return
    elif conflict(name2, places[1]):
        if conflict(name2, places[-2]):
            return "IMPOSSIBLE"
        else:
            places[0] = name1
            places[-1] = name2
            return
    else:
        places[0] = name1
        places[-1] = name2
        return  

def findPlacement(N, R, O, Y, G, B, V):
    places = ["E"] * N # E for empty
    order = [["R", R], ["Y", Y], ["B", B]]
    for i in xrange(1, N-1):
        order = findOrder(order)
        placed = False
        for j in xrange(len(order)):
            un = order[j]
            c, num = un
            if (num > 0 and not conflict(places[i-1], c)):
                places[i] = c
                placed = True
                order[j][1] -= 1
                break
        if(not placed):
            return "IMPOSSIBLE"
    result = placeFirstAndLast(places, order)
    if(result == "IMPOSSIBLE"):
        return "IMPOSSIBLE"
    return "".join(places)

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  N, R, O, Y, G, B, V = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  placement = findPlacement(N, R, O, Y, G, B, V)
  print "Case #{}: {}".format(i, placement)
  # check out .format's specification for more formatting options