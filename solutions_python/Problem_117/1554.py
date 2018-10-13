'''
    Google Code Jam 2013 
    Problem B: Lawnmower 

    @author: Masood Behabadi
'''

data_file = "data/B-small-attempt0.in"

def is_valid_pattern(orig, row, col):
    current = [2] * row * col
    
    # Solve rows
    for r in xrange(row):
        if orig[r * col:r * col + col] == [1] * col:
            current[r * col:r * col + col] = [1] * col
    
    # Solve columns
    for c in xrange(col):
        if orig[c::col] == [1] * row:
            current[c::col] = [1] * row
    
    return current == orig


if __name__ == '__main__':
    
    f = open(data_file, "r")
    
    ncase = int(f.readline())
    
    for c in xrange(ncase):
        
        print "Case #%s:" % (c + 1),
        
        row, col = (int(x) for x in f.readline().strip().split(" "))
        
        field_orig = []
        for r in xrange(row):
            field_orig += [int(x) for x in f.readline().strip().split(" ")]
        
        if is_valid_pattern(field_orig, row, col):
            print "YES"
        else:
            print "NO"