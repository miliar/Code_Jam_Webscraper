"""
Brute forces the small input for ominous omino.
"""

import fileinput

def main():
    #Set up the brute force answers
    #Indexed as dimension-dimension-x. All offset by 1. 0 = gabriel wins.
    richard_wins = [[[0 for x in range(4)]
                    for col in range(4)]
                   for row in range(4)];
    richard_wins[0][0] = [0, 1, 1, 1] #1x1
    richard_wins[1][1] = [0, 0, 1, 1] #2x2
    richard_wins[1][0] = [0, 0, 1, 1] #2x1
    richard_wins[2][2] = [0, 1, 0, 1] #3x3
    richard_wins[2][1] = [0, 0, 0, 1] #3x2
    richard_wins[2][0] = [0, 1, 1, 1] #3x1
    richard_wins[3][3] = [0, 0, 1, 0] #4x4
    richard_wins[3][2] = [0, 0, 0, 0] #4x3
    richard_wins[3][1] = [0, 0, 1, 1] #4x2
    richard_wins[3][0] = [0, 0, 1, 1] #4x1
    
    #Read from stdin
    firstLine = True;
    count = 1
    for line in fileinput.input():
        if firstLine:
            firstLine = False
            continue
        
        values = [int(num) for num in line.split()];
        X = values[0]
        dim_one = values[1]
        dim_two = values[2]
        
        smaller = min(dim_one, dim_two)
        larger = max(dim_one, dim_two)
        
        richard_winner = richard_wins[larger-1][smaller-1][X-1]
        winner_string = "RICHARD" if richard_winner == 1 else "GABRIEL"
        print("Case #" + str(count) + ": " + winner_string)
        count += 1
        
main()