import sys 

def main():
    # Open input.
    with open(sys.argv[1], 'r') as f:
        # Read T in.
        t = int(f.readline())
        # Do following T times:
        for i in range(1, t+1):
            # Read first row from volunteer in.
            # Remember: The volunteer is not a computer scientist, so their
            # row 1 is at index 0 for our program!
            volunteer_1 = int(f.readline()) - 1
            # Read first card arrangement in.
            magician_1  = [ set(map(int, f.readline().split(' ')))
                            for k in range(0, 4) ]
            # Read second row from volunteer in.
            volunteer_2 = int(f.readline()) - 1
            # Read second card arrangement in.
            magician_2  = [ set(map(int, f.readline().split(' ')))
                            for k in range(0, 4) ]
            # Get intersection of two arrangements (lists of sets)
            ans = magician_1[volunteer_1] & magician_2[volunteer_2]
            # If size of their intersections > 1: case 2 (bad magician)
            if len(ans) > 1:
                print('Case #{0}: Bad magician!'.format(i))
            # If size of their intersections = 0: case 3 (volunteer cheated)
            elif len(ans) == 0:
                print('Case #{0}: Volunteer cheated!'.format(i))
            # Otherwise, case 1, so print the one number in the set, via pop().
            else:
                print('Case #{0}: {1}'.format(i, ans.pop()))


if __name__ == '__main__':
    main()
