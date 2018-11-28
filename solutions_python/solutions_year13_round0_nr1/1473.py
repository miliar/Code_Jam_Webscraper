import sys


NR_ROWS = 4

# Status codes
X_WON = 1
O_WON = 2
DRAW = 3
NOT_COMPLETED = 4

# Textual desctiption
status_text = {}
status_text[X_WON] = 'X won'
status_text[O_WON] = 'O won'
status_text[DRAW] = 'Draw'
status_text[NOT_COMPLETED] = 'Game has not completed'

def read_file(filename):
    f = open(filename)
    content = f.read()
    f.close()
    return content
    
def parse_input(f):
    line_idx = 0
    
    cases = []
    nr_cases = int(f.readline())
    
    for case_idx in xrange(nr_cases):
    
        
        case = []
        
        for row_idx in xrange(NR_ROWS):
        
            row = []

            line = f.readline()

            for col_idx in xrange(NR_ROWS):
                row.append(line[col_idx])
                
            case.append(row)
                
        cases.append(case[:])
        

                
        # Line break after every case
        line = f.readline()
        
    
    return cases
    
def check_list(l):
    """
    Return the case status if anyone won, else return None
    """
    if l.count('T') == 1:
        if l.count('X') == NR_ROWS - 1:
            return X_WON
        if l.count('O') == NR_ROWS - 1:
            return O_WON
            
    if l.count('X') == NR_ROWS:
        return X_WON
    if l.count('O') == NR_ROWS:
        return O_WON
        
    return None
    
def check_status(case):
    # Has anyone won
    
    # Check rows
    for row in case:
        status = check_list(row)
        if status is not None:
            return status
                
    # Check cols
    for col_idx in xrange(NR_ROWS):
        # Prepare column as list
        col = []
        for row_idx in xrange(NR_ROWS):
            col.append(case[row_idx][col_idx])
    
        status = check_list(col)
        if status is not None:
            return status
                
    # Check diagonal 1
    diag = []
    for i in xrange(NR_ROWS):
        diag.append(case[i][i])
    status = check_list(diag)
    if status is not None:
        return status
        
    diag = []
    for i in xrange(NR_ROWS):
        diag.append(case[i][NR_ROWS - i - 1])
    status = check_list(diag)
    if status is not None:
        return status
    
    # Check if completed
    for row in case:
        if row.count('.'):
            return NOT_COMPLETED
            
    return DRAW

def main():
    
    f = open(sys.argv[1], 'r')
    cases = parse_input(f)
    f.close()
    
    output_file = open('output.txt', 'w')
    for case_idx, case in enumerate(cases):
        status_code = check_status(case)
        output_file.write('Case #%d: %s\n' % (case_idx + 1, status_text[status_code]))
        
    output_file.close()
    
    
if __name__ == '__main__':
    main()