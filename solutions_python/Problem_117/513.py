def isGreaterInRow(data, rows, cols, row, elem):
    col = 0
    while col < cols:
        if elem < data[row][col]:
            return True
        col = col + 1
    return False
    
def isGreaterInCol(data, rows, cols, col, elem):
    row = 0
    while row < rows:
        if elem < data[row][col]:
            return True
        row = row + 1
    return False
    

def isPossible(data, rows, cols):
    i = 0
    #print "rows = " + str(rows) + " cols = " + str(cols)
    while i < rows:
        j = 0
        while j < cols:
            if isGreaterInRow(data, rows, cols, i, data[i][j]) and isGreaterInCol(data, rows, cols, j, data[i][j]):
                return "NO"
            j = j + 1
        i = i + 1    
    return "YES"

def prepare_input(input_file):
    T = int(input_file.readline().replace('\n',''))
        
    output_file = file("B-large.out", "w")
        
    for test_case_counter in xrange(T):
        input_data = []
        v1 = input_file.readline().replace('\n','').split(' ')
        rows = int(v1[0])
        cols = int(v1[1])
        for i in xrange(rows):
            col = input_file.readline().replace('\n','').split(' ')
            col = map(int, col)
            input_data.append(col)
        
        #print input_data[0][0]
        
        #for i in xrange(rows):
        #    output_file.write(str(input_data[i]) + "\n")
        #lowest count will be the number of switches in the server
        output_file.write("Case #"+str(test_case_counter+1)+": " + isPossible(input_data, rows, cols) + "\n")
        
    output_file.close()
    
if __name__ == "__main__":
    input_file = file("B-large.in")
    prepare_input(input_file)
