import sys



numcases = int(sys.stdin.readline())
for casenumber in xrange(1,numcases+1):
    num_elems = int( sys.stdin.readline().rstrip("\r\n") )
    elems = [int(x) for x in sys.stdin.readline().rstrip("\r\n").split(" ")]
    sorted_elems = sorted(elems)
    num_swaps = 0
    for i in xrange(0, len(elems)):
        current_value = elems[i]
        desired_value = sorted_elems[i]
        if current_value != desired_value:

            # find the element that contains what's needed and swap
            potential_positions = []
            for j in xrange(0, len(sorted_elems)):
                if sorted_elems[j] == desired_value:
                    potential_positions.append(j)

            # for each potential position, see if this swap makes it correct
            # on both.  if not, just take the first
            inserted = False
            for j in potential_positions:
                if current_value == sorted_elems[j]:
                    new_value = elems[j]
                    old_value = elems[i]
                    elems[i] = new_value
                    elems[j] = old_value
                    num_swaps = num_swaps + 1
                    inserted = True
                    break
                    
            if not inserted:
                j = potential_positions[0]
                new_value = elems[j]
                old_value = elems[i]
                elems[i] = new_value
                elems[j] = old_value
                num_swaps = num_swaps + 1
                inserted = True

    avg_num_smashes = num_swaps
    print "Case #%d: %u.000000" % (casenumber, avg_num_smashes)

