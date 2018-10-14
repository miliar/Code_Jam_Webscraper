'''
This script would have template for reading and writing files for the google code jam thing.

@author: nanda
'''

##############################################################################
# This part would contain the logic for solving actual puzzle.
def solve_puzzle(input):
    wp = []
    for i, team in enumerate(input):
        ones = 0
        zeros = 0
        for char in team:
            if char == '1':
                ones = ones + 1
            if char  == '0':
                zeros = zeros + 1
        wp.append((ones * 1.0)/ (ones+zeros))
    
    owp = []
    for i, team in enumerate(input):
        wp_ex = []
        for j, ch in enumerate(team):
            if (i==j):
                continue
            if ch == '.':
                continue
            wp_ex.append(get_wp_ex(input[j], i))
        
        sum = 0.0
        for a in wp_ex:
            sum = sum + a
        owp.append(sum / len(wp_ex))
        
    oowp = []
    for i, team in enumerate(input):
        sum = 0.0
        count = 0
        for j, ch in enumerate(team):
            if ch == '.':
                continue
            sum = sum + owp[j]
            count = count + 1
        oowp.append(sum / count)
    
    rpi = []
    for i, team in enumerate(input):
        rpi.append(0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i])

    return rpi
    
def get_wp_ex(team, bar):
    ones = 0
    zeros = 0
    for i, ch in enumerate(team):
        if (i == bar):
            continue
        if ch == '1':
            ones = ones + 1
        if ch  == '0':
            zeros = zeros + 1    
    return (ones * 1.0)/ (ones+zeros)
        
  
##############################################################################
def main():
    # Code for Reading and writing.
    # Small Files.
    #in_file_name = "A-small-attempt0.in"
    #out_file_name = "A-small-attempt0.out"
    
    # Large Files. 
    in_file_name = "A-large-attempt0.in"
    out_file_name = "A-large-attempt0.out"
    
    in_file =  "d:\codejam\problems\\" + in_file_name
    out_file = "d:\codejam\problems\\" + out_file_name
    
    reader = open(in_file)
    writer = open(out_file, 'w')
    
    lines = reader.readlines()[1:]
    case_no = 0
    while(len(lines) > 0):
        teams = int(lines[0].strip())
        lines = lines[1:]
        teams_scores = []
        c = 0
        while(teams > 0):
            teams_scores.append(lines[c].strip())
            c = c + 1
            teams = teams - 1
        lines = lines[c:]
        result = solve_puzzle(teams_scores)
        writer.write("Case #" + str(case_no+1)+ ":\n")
        for res in result:
            writer.write(str(res))
            writer.write("\n")
        case_no = case_no + 1   
    writer.close()
    
##############################################################################
if __name__== "__main__":
    main()