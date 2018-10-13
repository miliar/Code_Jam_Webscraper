# open output file
fout = open('outputQ1large.txt', 'w+')
	
# open input file	
fin = open('A-large.in', 'r')
fin.seek(0)

file_line = fin.readline()

n = file_line
print 'number of casees: ' + n

val_4X = 4*88
val_3XT = 3*88+84
val_4O = 4*79
val_3OT = 3*79 + 84

for case in range(int(n)):
        line1 = fin.readline()
        line2 = fin.readline()
        line3 = fin.readline()
        line4 = fin.readline()
        end_of_case = fin.readline()
        matrix = [line1[:4],line2[:4],line3[:4],line4[:4]]

        winner = ''
        has_empty = False

        for line_index in range(4):
                line_sum = 0
                for char in matrix[line_index]:
                        line_sum = line_sum + ord(char)
                        if char=='.':
                                has_empty = True
                        
                if (line_sum == val_4X) or (line_sum == val_3XT):
                        winner = 'X won\n'
                if (line_sum == val_4O) or (line_sum == val_3OT): 
                        winner = 'O won\n'

        for line_index in range(4):
                col_sum = 0
                for col_index in range(4):
                        col_sum = col_sum + ord(matrix[col_index][line_index])
                        
                if (col_sum == val_4X) or (col_sum == val_3XT):
                        winner = 'X won\n'
                if (col_sum == val_4O) or (col_sum == val_3OT): 
                        winner = 'O won\n'

        diag_sum = ord(matrix[0][0]) + ord(matrix[1][1]) + ord(matrix[2][2]) + ord(matrix[3][3])
        if (diag_sum == val_4X) or (diag_sum == val_3XT):
                winner = 'X won\n'
        if (diag_sum == val_4O) or (diag_sum == val_3OT): 
                winner = 'O won\n'

        inv_diag_sum = ord(matrix[3][0]) + ord(matrix[2][1]) + ord(matrix[1][2]) + ord(matrix[0][3])
        if (inv_diag_sum == val_4X) or (inv_diag_sum == val_3XT):
                winner = 'X won\n'
        if (inv_diag_sum == val_4O) or (inv_diag_sum == val_3OT): 
                winner = 'O won\n'

        if (winner=='') and has_empty==False:
                winner = 'Draw\n'
        if (winner=='') and has_empty==True:
                winner = 'Game has not completed\n'
        
        fout.write('Case #' + str(case+1) + ': ' + winner)

fout.flush()

fout.close()
