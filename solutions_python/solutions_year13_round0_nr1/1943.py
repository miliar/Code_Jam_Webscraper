#!/usr/bin/env python

def didwin(letter, grid):
    # Ugly ugly hack
    #  replace T with letter
    grid=grid.replace('T',letter)
    # Testing Rows
    if grid[0]+grid[1]+grid[2]+grid[3]==letter*4: return True  
    if grid[4]+grid[5]+grid[6]+grid[7]==letter*4: return True  
    if grid[8]+grid[9]+grid[10]+grid[11]==letter*4: return True 
    if grid[12]+grid[13]+grid[14]+grid[15]==letter*4: return True
    # Testing Cols
    if grid[0]+grid[4]+grid[8]+grid[12]==letter*4: return True  
    if grid[1]+grid[5]+grid[9]+grid[13]==letter*4: return True  
    if grid[2]+grid[6]+grid[10]+grid[14]==letter*4: return True  
    if grid[3]+grid[7]+grid[11]+grid[15]==letter*4: return True  
    # Testing Diagonals
    if grid[0]+grid[5]+grid[10]+grid[15]==letter*4: return True  
    if grid[3]+grid[6]+grid[9]+grid[12]==letter*4: return True  

    return False

if __name__ == "__main__":
    cases = input()
    for case in xrange(0, cases):
        # read in matrix
        message=""
        matrix=""
        matrix+=raw_input() 
        matrix+=raw_input() 
        matrix+=raw_input() 
        matrix+=raw_input() 
        raw_input()

        if didwin("X", matrix):
            message="X won"
        elif didwin("O", matrix):
            message="O won"
        elif matrix.find('.') == -1:
            message ="Draw"
        else:
            message ="Game has not completed"
        print("Case #%i: %s" % (case+1, message))
