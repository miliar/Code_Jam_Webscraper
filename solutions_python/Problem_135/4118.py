def get_matrix(filename):
    """This function reads a file and returns a matrix """
    line = []
    try:
        handler = open(filename, 'r')
        line = [ map(int, line.split(' ')) for line in handler]
        return line
            
    except Exception, e:
        pass


def get_row(n,matrix):
    """this function takes row selected and the matrix and returns a  list for that row """
    return matrix[n-1]


def find_number(ls1, ls2):
    count = 0
    answer = 0
    for i in ls1:
        for j in ls2:
            if i == j:
                count +=1
                answer = i

    if answer == 0:
        return 'Volunteer cheated!'
        

    if count !=1:
        return 'Bad magician!'

    if answer !=0 and count==1:
        return answer


def write_to_file(output, filename):
    """ """
    try:
        handler = open(filename, 'w+')
        handler.write(output+"\n")
        handler.close()
            
    except Exception, e:
        pass
    
matrix = get_matrix('list.txt')
first = matrix[0]
del matrix[0]
counter = 0
row = []
ls = []

for i in range(0,len(matrix),5):
    row.append(matrix.pop(counter))
    counter = counter+4
# print ls

for i in range(0, len(matrix),4):
    ls.append(matrix[i:i+4])
    
def magic(first_matrix, second_matrix, row1, row2):
    first_list, second_list = first_matrix[row1-1], second_matrix[row2-1]
    return find_number(first_list, second_list)
counter = 0 
handler = open('output.out','w+')
for i in range(0,len(ls),2):
    result = magic(ls[i],ls[i+1], row[i][0], row[i+1][0])
    counter = counter+1
    handler.write('Case #%s: %s\n'%(counter, result)) 
handler.close()

