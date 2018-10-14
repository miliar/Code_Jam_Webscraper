f=open('A-large.in')
lines = []
for line in f.readlines():
        lines.append(line)
f.close()
a = lines.pop(0)
n = int(a.strip())
for i in range(n):
        rows = []
        rows_X = []
        rows_O = []
        for j in range(4):
                rows.append((lines.pop(0)).strip())
        if len(lines)>0:
                lines.pop(0)
        incomp = False
        X = False
        O = False
        for row in rows:
                if row.find('.') != -1:
                        incomp = True
        for row in rows:
                rows_X.append(row.replace('T','X'))
                rows_O.append(row.replace('T','O'))
        #check rows
        for row in rows_X:
                if row == 'XXXX':
                        X = True
                        break
        for row in rows_O:
                if row == 'OOOO':
                        O = True
                        break
        #check column
        for j in range(4):
                if rows_X[0][j]+rows_X[1][j]+rows_X[2][j]+rows_X[3][j] == 'XXXX':
                        X = True
                        break
                if rows_O[0][j]+rows_O[1][j]+rows_O[2][j]+rows_O[3][j] == 'OOOO':
                        O = True
                        break
        #check diagonal
        if rows_X[0][0]+rows_X[1][1]+rows_X[2][2]+rows_X[3][3] == 'XXXX':
                        X = True
        elif rows_O[0][0]+rows_O[1][1]+rows_O[2][2]+rows_O[3][3] == 'OOOO':
                        O = True
        elif rows_X[0][3]+rows_X[1][2]+rows_X[2][1]+rows_X[3][0] == 'XXXX':
                        X = True
        elif rows_O[0][3]+rows_O[1][2]+rows_O[2][1]+rows_O[3][0] == 'OOOO':
                        O = True
        
        if X:
                ans = 'X won'
        elif O:
                ans = 'O won'
        elif incomp:
                ans ='Game has not completed'
        else:
                ans = 'Draw'
        print('Case #',i+1,': ',ans,end='\n',sep='')
                
        
                
               
