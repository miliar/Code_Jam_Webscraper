def get_int(A, B, N):
    intersects = 0
    i=0
    while i < N-1:
        j=i+1
        while j < N:
            if (A[i] > A[j] and B[i] < B[j]) or (A[i] < A[j] and B[i] > B[j]):
                intersects += 1
            j += 1
        i += 1
    return intersects

def get_count(curr_dir, dir_exist, N):
    count = 0
    dirs = curr_dir.split('/')
    par_dir = ""
    for i in xrange(len(dirs)):
        if dirs[i] !="":
            par_dir += '/' + dirs[i] 
            try:
                dir_exist.index(par_dir)
            except ValueError:
                  count += 1
                  dir_exist.append(par_dir)
                  
    return count
          
def getParentDir(curr_dir):
    
    parent_dir = ""
    i=0
    print dirs
    while i < len(dirs)-1:
        if dirs[i] != "":
          parent_dir += '/' + dirs[i]
        i += 1
    return parent_dir
    
def prepare_input(input_file):
    test_case_count = int(input_file.readline())  #number of test cases
    
    output_file = file("A-large.out", "w")
    
    for test_case_counter in xrange(test_case_count):
        row = []
        lines1 = (input_file.readline().replace('\n','')).split(' ')
        R = int(lines1[0])
        C = int(lines1[1])
        for i in xrange(R):
          lines2 = (input_file.readline().replace('\n','')).split(' ')
          col = []
          for j in xrange(C):
            col.append(lines2[0][j])
          row.append(col)
        
        result = ""
        for i in xrange(R):
            for j in xrange(C):
                if row[i][j] == '#':
                    if i < R-1 and j < C-1:
                        if row[i][j+1] == '#' and row[i+1][j] == '#' and row[i+1][j+1]=='#':
                            row[i][j] = '/'
                            row[i][j+1] = '\\'
                            row[i+1][j] = '\\'
                            row[i+1][j+1] = '/'
                        else:
                            result = "Impossible"
                    else:
                        result = "Impossible"
        
        output_file.write("Case #"+str(test_case_counter+1)+":\n") 
        if result== "Impossible":
            output_file.write(result + "\n") 
        else:
            for i in xrange(R):
                for j in xrange(C):
                    output_file.write(row[i][j])
                output_file.write("\n") 

    output_file.close()
    
if __name__ == "__main__":
    input_file = file("A-large.in")
    prepare_input(input_file)
