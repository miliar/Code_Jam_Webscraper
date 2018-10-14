# open output file
fout = open('outputQ2.txt', 'w+')
	
# open input file	
fin = open('B-small-attempt0.in', 'r')
fin.seek(0)

file_line = fin.readline()

n = file_line
print 'number of casees: ' + n

for case in range(int(n)):

        pout = 'YES\n'
        line1 = fin.readline()
        num_of_rows = int(line1.split(' ')[0])
        num_of_col = int(line1.split(' ')[1])
        matrix = [[0 for col in range(num_of_col)] for row in range(num_of_rows)]
        
        for line_index in range(num_of_rows):
                read_line = fin.readline()
                read_line = read_line[:-1]
                matrix[line_index] = read_line.split(' ')

        for i in range(num_of_rows):
                for j in range(num_of_col):
                        for l in range(num_of_col):
                                if matrix[i][j] < matrix[i][l]:
                                        for k in range(num_of_rows):
                                                if matrix[i][j] < matrix[k][j]:
                                                        pout = 'NO\n'
                                                        
        fout.write('Case #' + str(case+1) + ': ' + pout)

fout.flush()

fout.close()
