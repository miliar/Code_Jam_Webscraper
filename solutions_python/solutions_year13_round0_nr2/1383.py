import sys

input_file=None
output_file=open("output.txt", 'w')

#def printLawn(lawn):
    
def getMaxCol(final_lawn, col):    
    max_value = 0
    for row in final_lawn:
        if row[col] > max_value:
            max_value = row[col]
    return max_value

def main():
    input_file=open(sys.argv[1], 'r')
    number_of_test_cases = int(input_file.readline())
    for k in range(0,number_of_test_cases):
        rows_col_line = (input_file.readline()).split()
        row_count = int(rows_col_line[0])
        coloumn_count = int(rows_col_line[1])
        
        raw_lawn = [None]*row_count
        for i in range(0, row_count):
            raw_lawn[i] = [None]*coloumn_count
        final_lawn = [None]*row_count
        for i in range(0, row_count):
            final_lawn[i] = [None]*coloumn_count
    
        for i in range (0, row_count):
            line = input_file.readline().split()
            for j in range(0,coloumn_count):
                raw_lawn[i][j] = 100
                final_lawn[i][j] = int(line[j])
#        print raw_lawn
#        print final_lawn
        for i in range(0, row_count):
            max_value_in_range = max(final_lawn[i])
            for j in range(0,coloumn_count):
                if raw_lawn[i][j] > max_value_in_range:
                    raw_lawn[i][j] = max_value_in_range
        for i in range(0, coloumn_count):
            max_value_of_coloumn = getMaxCol(final_lawn, i)
            for j in range(0, row_count):
                if raw_lawn[j][i] > max_value_of_coloumn:
                    raw_lawn[j][i] = max_value_of_coloumn
                
        if raw_lawn == final_lawn:
            output_file.write("Case #%d: YES\n" % (k+1))
        else :
            output_file.write("Case #%d: NO\n" % (k+1))
    return

main()