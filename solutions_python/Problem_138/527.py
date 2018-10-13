import sys

def do_test_case(ofile, curr_test_case, N, naomi, ken):

    # Make copies, play a deceit game
    deceit_pt = 0
    naomi_deceit = list(naomi)
    ken_deceit = list(ken)

    ken_highest = N - 1
    ken_lowest = 0

    for naomi_elem in naomi_deceit:
        # Get ken_lowest to a real elem
        while (ken_lowest < N) and (ken_deceit[ken_lowest] == None): ken_lowest += 1

        if ken_deceit[ken_lowest] < naomi_elem:
            deceit_pt += 1
            ken_deceit[ken_lowest] = None
            
        else: # Knock out Ken's highest one
            while (ken_highest > -1) and (ken_deceit[ken_highest] == None): ken_highest -= 1
            ken_deceit[ken_highest] = None
        

    

    # Make copies, play a regular game
    regular_pt = 0
    naomi_reg = list(naomi)
    ken_reg = list(ken)

    ken_lowest = 0
    ken_ptr = 0

    for naomi_elem in naomi_reg:
        while (ken_ptr < N) and ((not ken_reg[ken_ptr]) or (ken_reg[ken_ptr] < naomi_elem)): ken_ptr += 1
        if ken_ptr == N: # nothing is bigger
            ken_reg[ken_lowest] = None
            regular_pt += 1 # so, Naomi gets a point
            ken_ptr = ken_lowest
        else:
            ken_reg[ken_ptr] = None
        
        # Advance to the next one
        while (ken_lowest < N) and (ken_reg[ken_lowest] == None): ken_lowest += 1
        
    

    # Counts non-None
    # ken_regular_pt = reduce(lambda acc, elem: acc + 1 if elem else acc, naomi_reg, 0)
    
    print 'Case #%d: %d %d' % (curr_test_case, deceit_pt, regular_pt)
    ofile.write('Case #%d: %d %d' % (curr_test_case, deceit_pt, regular_pt) + "\n")

def main():
    if len(sys.argv) != 3:
        print "Usage: ProblemD.py <input> <output>"
        exit()

    with open(sys.argv[1], 'r') as ifile:
        with open(sys.argv[2], 'w') as ofile:
            ilines = ifile.readlines()
            ncases = int(ilines[0])
            ilines_idx = 1

            for curr_test_case in range(1, ncases + 1):
                N = int(ilines[ilines_idx]); ilines_idx += 1
                naomi = map(lambda a: float(a), ilines[ilines_idx].split())
                ilines_idx += 1
                ken = map(lambda a: float(a), ilines[ilines_idx].split())
                ilines_idx += 1

                naomi.sort()
                ken.sort()
                do_test_case(ofile, curr_test_case, N, naomi, ken)


if __name__ == "__main__":
    main()
