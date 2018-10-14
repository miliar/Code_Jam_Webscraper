# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 17:49:58 2017

@author: kprashan
"""
def fillMat(mat,R,C):
    for i in range(R):
        if mat[i].find('?') == -1 :
            continue
        else :
            count = mat[i].count('?')
            #Complete row is empty
            # copy previous row if exist
            #else copy next
            if count == C :
                continue
            else :
                emptyIdx = mat[i].find('?')
                while emptyIdx != -1 :
                    if emptyIdx == 0:
                        start_idx = mat[i].find('?')
                        idx = 1
                        while mat[i][start_idx+idx] == '?' and (start_idx + idx <C-1):
                            idx += 1
                        mat[i] = mat[i][idx]*idx + mat[i][idx:]
                        emptyIdx = mat[i].find('?')
                    else :
                        start_idx = mat[i].find('?')
                        idx = 0
                        print("start_idx:", start_idx)
                        while (mat[i][start_idx+idx] == '?') and (start_idx + idx < C-1):
                            idx += 1
                        print("mat:",mat[i])
                        print("idx", idx)
                        mat[i] = mat[i][0:start_idx] + mat[i][start_idx-1]*(idx) + mat[i][start_idx+idx:]
                        if (emptyIdx == C- 1):
                            mat[i] = mat[i][0:-1] + mat[i][-2]
                        emptyIdx = mat[i].find('?')
                        
    for i in range(R):
        found = False
        if mat[i].find('?') != -1:
            j = i
#            print("i",i)
#            print("mat:",mat[i])
#            print("j",j)
            while ((j > 0) and (mat[j].find('?') != -1)) :
#                print("j-1",j-1)
                j = j - 1
#                print("mat[j]",mat[j])
                if mat[j].find('?') == -1 :
                    mat[i] = mat[j]
#                    print("found",mat[i])
                    found = True
                    break
            if not found :
                j = i
#                print("j",j)
                while (j < C) and (mat[j].find('?') != -1) :
#                    print("j+1",j+1)
                    j = j + 1
#                    print("mat[j]",mat[j])
                    if mat[j].find('?') == -1 :
                        mat[i] = mat[j]
                        found = True
                        break
                    
            
file_in = 'A-large.in'
fileName = 'A-large.out'
fileOut = open(fileName,'w')
with open(file_in) as f :
    T = int(f.readline().rstrip())
    for i in range(1,T+1):
        R,C = [int(num) for num in f.readline().rstrip().split()]
        mat =[]
        for j in range(R):
            mat.append(f.readline().rstrip())
        fillMat(mat,R,C)
        print("Case #{}:".format(i),file=fileOut)
#        print("Case #{}:".format(i))
        for string in mat:
            print("{}".format(string),file=fileOut)
#            print("{}".format(string))
#        print()
#        print("Case #{}: {} {}".format(i,mat),file=fileOut)
        
fileOut.close()