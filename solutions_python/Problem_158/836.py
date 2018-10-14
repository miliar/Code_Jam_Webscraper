with open('D-small-attempt1.in') as f:
    cases = int(f.readline())
    
    for i in range(cases):
        x, r, c = [int(chunk) for chunk in f.readline().split()]
        
        # if x is 7 or larger, Richard can pick an omino
        # with a 1-tile hole in it and Gabriel is doomed.
        # (jerk move if you ask me)
        # (only relevant for large input)
        if x > 6:
            print("Case #{0}: RICHARD".format(i + 1))
            continue
        
        # short-circuit if the board size isn't a multiple
        # of the omino size
        elif (r * c) % x:
            print("Case #{0}: RICHARD".format(i + 1))
            continue
        
        # in these cases either the I-block or the L-block
        # allow Richard to win because there is no way
        # to fit them on the board    
        elif (x > max(r, c)) or ((x / 2.0) > min(r, c)):
            print("Case #{0}: RICHARD".format(i + 1))
            continue
        
        # by this point, the only thing that's left is
        # x = 4, r x c = 4 x 4, 3 x 4, or 2 x 4, and we just
        # enumerate these cases (sigh); Richard wins for 
        # 2 x 4, Gabriel otherwise        
        elif (x is 4) and ((r, c) in [(2, 4), (4, 2)]):
            print("Case #{0}: RICHARD".format(i + 1))
            continue
            
        else:
            print("Case #{0}: GABRIEL".format(i + 1))