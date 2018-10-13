
def read_input(filename):
    data = []
    with file(filename, 'rt') as f:
        for line in f:
            data.append(line)
        
    field_num = int(data[0].strip())
	
    fields = []
    curr_line = 1
    for _ in xrange(field_num):
        n, m = data[curr_line].strip().split()
        n = int(n)
        m = int(m)
        curr_line += 1
        curr_field = []
        for _ in xrange(n):
            real_line = data[curr_line].split()
            curr_field.append([int(i) for i in real_line])
            curr_line += 1
        fields.append(curr_field)

    print fields
    return fields

def is_field_possible(field):
    # Calculating what mowers must be configured to for creating field
    row_mowers = [max(row) for row in field]
    col_mowers = []
    for m in xrange(len(field[0])):
        col_mowers.append(max([x[m] for x in field]))
        
    # Creating what field would look like after being mowed
    new_field = [[100 for _ in xrange(len(col_mowers))] for _ in xrange(len(row_mowers))]
    for i in xrange(len(row_mowers)):
        for j in xrange(len(col_mowers)):
            new_field[i][j] = min([100, row_mowers[i], col_mowers[j]])
            
    if new_field == field:
        return 'YES'
    else:
        return 'NO'

def get_state(fields):
    res = []
    for field in fields:
        res.append(is_field_possible(field))
        
    print res
    return res

def create_output(res):
    with file('output1.txt', 'wt') as f:
        for (i, line) in enumerate(res):
            print >> f, 'Case #%d: %s' % (i + 1, line) 
            
def main():
    import sys
    data = read_input(sys.argv[1])
    res = get_state(data)
    create_output(res)

if __name__ == "__main__":
    main()