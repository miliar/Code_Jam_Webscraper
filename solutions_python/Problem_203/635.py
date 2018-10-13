import copy
import heapq
import collections

cases = []

class case:

     def __init__(self,row=0,col=0):
         self.row = row
         self.col = col
         self.mat = []
         self.rec = []

     def set(self,row,col):
         self.row = row
         self.col = col
         self.mat = []
         self.rec = []

     def clear(self):
         self.row = 0
         self.col = 0
         self.mat = []
         self.rec = []


with open('A-large.in','r') as infile:
    i,cur_row = 0,0
    read_mat = False
    for row in infile:
        i += 1
        if i > 1:
            if not read_mat:
                tmp_case = case()
                params = row.strip().split(' ')
                #print params
                read_mat = True
                cur_row = int(params[0])
                tmp_case.set(int(params[0]),int(params[1]))
            else:
                #print cur_row,row
                if cur_row > 1:
                    cur_row -= 1
                    tmp_case.mat.append(list(row.strip()))
                else:
                    tmp_case.mat.append(list(row.strip()))
                    tmp_case.rec = tmp_case.mat
                    #print tmp_case.mat
                    cases.append(tmp_case)
                    read_mat = False

def fill(case,direction):

    for i in range(case.row):
        for j in range(case.col):
            if case.mat[i][j] != '?':
                cur = case.mat[i][j]
                if direction == 'col':
                    for k in range(i+1,case.row):
                        if case.mat[k][j] == '?':
                            case.mat[k][j] = cur
                        else:
                            break
                    for k in range(i):
                        if case.mat[k][j] == '?':
                            case.mat[k][j] = cur
                        else:
                            break
                else:
                    for m in range(j+1,case.col):
                        if case.mat[i][m] == '?':
                            case.mat[i][m] = cur
                        else:
                            break
                    for m in range(j):
                        if case.mat[i][m] == '?':
                            case.mat[i][m] = cur
                        else:
                            break

def cake_divider(case):

    fill(case,'col')
    fill(case,'row')

    return case.mat


ans = []
test = []
for i,case in enumerate(cases):
    test.append(case)
    #print case.mat
    res = cake_divider(case)
    ans.append('Case #' + str(i + 1) + ':')
    for item in res:
        ans.append(item)


with open('test.out','w') as outfile:
    for row in ans:
        outfile.write("".join(row)+'\n')

with open('infile.txt','w') as outfile:
    for row in ans:
        outfile.write("".join(row)+'\n')
