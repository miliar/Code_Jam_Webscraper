
def case(but, rob):
    position = {"O":1, "B":1}
    made_moves = 0 
    total = 0

    for i in xrange(0, len(but)):
        diff = but[i] - position[rob[i]]
        position[rob[i]] += diff
        
        if rob[i] == rob[i-1]:
            made_moves += abs(diff) + 1
            total += abs(diff) + 1
        else:
            if abs(diff) <= made_moves:
                made_moves = 1
            else:
                made_moves = abs(diff) - made_moves + 1
            total += made_moves
    return total 

if __name__ == "__main__":
   T = int(raw_input())
   for i in xrange(1, T+1):
       line = raw_input().split(" ")
       r = line[1::2]
       b = map(int, line[2::2])
       print "Case #%s: %s" % (i, case(b, r))
