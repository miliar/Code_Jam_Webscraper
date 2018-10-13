import sys

num_cases = int(sys.stdin.readline())

def get_winner(n, k, cols):
    
    tracker = []
    for _ in xrange(n):
        col = []
        for _ in xrange(n):
            # neg's are R pos's are B
            entry = {'D': 0, 'L': 0, 'DD': 0, 'DU': 0}
            col.append(entry)
        tracker.append(col)
    
    red_won = False
    blue_won = False
    
    for i in xrange(n):
        for j in xrange(n):
            piece = cols[i][j]
            if piece == '.':
                tracker[i][j] = {'D': 0, 'L': 0, 'DD': 0, 'DU': 0}
            else:
                _piece = -1 if piece == 'R' else 1

                # check D
                D = tracker[i][j-1]['D'] if j-1 >= 0 else 0
                new_D = D + _piece if D and (D * _piece) > 0 else _piece
                tracker[i][j]['D'] = new_D
                if abs(new_D) >= k:
                    if new_D < 0:
                        red_won = True
                    else:
                        blue_won = True

                # check L
                L = tracker[i-1][j]['L'] if i-1 >= 0 else 0
                new_L = L + _piece if L and (L * _piece) > 0 else _piece
                tracker[i][j]['L'] = new_L
                if abs(new_L) >= k:
                    if new_L < 0:
                        red_won = True
                    else:
                        blue_won = True
                
                # check DD
                DD = tracker[i-1][j+1]['DD'] if i-1 >= 0 and j+1 < n else 0
                new_DD = DD + _piece if DD and (DD * _piece) > 0 else _piece
                tracker[i][j]['DD'] = new_DD
                if abs(new_DD) >= k:
                    if new_DD < 0:
                        red_won = True
                    else:
                        blue_won = True
            
                # check DU
                DU = tracker[i-1][j-1]['DU'] if i-1 >= 0 and j-1 >= 0 else 0
                new_DU = DU + _piece if DU and (DU * _piece) > 0 else _piece
                tracker[i][j]['DU'] = new_DU
                if abs(new_DU) >= k:
                    if new_DU < 0:
                        red_won = True
                    else:
                        blue_won = True
    
    if red_won and blue_won:
        return 'Both'
    elif red_won:
        return 'Red'
    elif blue_won:
        return 'Blue'
    else:
        return 'Neither'


for j in xrange(num_cases):
    n, k = [int(e) for e in sys.stdin.readline().split()]
    
    rows = []
    for i in xrange(n):
        row = sys.stdin.readline().strip().replace('.', '')
        flattened_row = ('.' * (n - len(row))) + row 
        rows.append(flattened_row)
        
    print "Case #%s: %s" % (j+1, get_winner(n, k, rows))
    j += 1
