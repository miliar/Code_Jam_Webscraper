# by Enrique Gonzalez (Enriikke)
# enjoy!

# Setup the files here.
in_file = '../../../Downloads/B-small-attempt0.in'
out_file = 'solution.out'
try:
    in_file = open(in_file, 'r')
    out_file = open(out_file, 'w')
except IOError as e:
    print e.errno
    print e.strerror


# Quick util function to print out a single case solution.
def print_solution(case_number, solution, file=out_file):
    try:
        file.write('Case #{0!s}: {1}\n'.format(case_number, solution))
    except Exception as e:
        print type(e)
        print e.args


# This is just a place holder and it makes it easier to read the code.
def parse_data(file=in_file):
    N, M = file.readline().split()
    N, M = int(N), int(M)
    
    lawn_map = {}
    blueprint = []
    for n in range(1, N + 1):
        lawn_map['row' + str(n)] = file.readline().strip()
        blueprint.append(lawn_map['row' + str(n)].split())
    
    key_list = lawn_map.keys()
    key_list.sort()
    
    for m in range(M):
        col = []
        for key in key_list: col.append(lawn_map[key].split()[m])
        lawn_map['col' + str(m + 1)] = ' '.join(col)
        
    lawn_map['height'] = N
    lawn_map['width'] = M
    lawn_map['blueprint'] = blueprint
    
    
    return lawn_map
    

def solve_it():
    # Number of test cases
    N = int(in_file.readline())
    
    # Iterate through every test case
    for t in range(1, N + 1):
        # Get my case data ready
        lawn_map = parse_data()
        
        # Magic goes here
        solution = 'NO'
        lawn = [['2' for col in range(lawn_map['width'])] for row in range(lawn_map['height'])]
        
        
        for n in range(1, lawn_map['height'] + 1):
            row = lawn_map['row' + str(n)]
            full_row = (row[0] + ' ') * lawn_map['width']
            if full_row.strip()  == row: lawn[n - 1] = row.split()
        
        
        for m in range(lawn_map['width']):
            col = lawn_map['col' + str(m + 1)]
            full_col = (col[0] + ' ') * lawn_map['height']
            if full_col.strip() == col:
                for n in range(lawn_map['height']): lawn[n][m] = col.split()[n]
                   
        
        if lawn == lawn_map['blueprint']: solution = 'YES'
                
        
        # Print solution
        print_solution(t, solution)
    
    
    # Close both files
    in_file.close()
    out_file.close()


solve_it()
