import time
#from copy import deepcopy

SMALL_LIMIT = 102
print (time.ctime())

f_in = open('c:/temp/codejam/round2/c/C-small-attempt1.in')
f_out = open('c:/temp/codejam/round2/c/C-small-attempt1.out','w')

def is_bacteria_in_mat (mat):
    for line in mat:
        if True in line:
            return True
    return False

T = int(f_in.readline())
for case in range(1,T+1):

    print (case,end ='  ')
    R  = int(f_in.readline())
    mat = [[False]*SMALL_LIMIT for i in range(SMALL_LIMIT)]
    start_diagonal = 2
    for rect in range(R):
        x1,y1,x2,y2 = [int(x) for x in f_in.readline().split()]
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                mat[x][y] = True

    print ('*')
    
    # simulate

    count_time = 0
    while is_bacteria_in_mat(mat):
        #mat2 = deepcopy(mat)
        for x in range(SMALL_LIMIT-1,0,-1):
            for y in range(SMALL_LIMIT-1,0,-1):
                if mat[x-1][y] and mat[x][y-1]:
                    mat[x][y] = True
                if (not mat[x-1][y]) and (not mat[x][y-1]):
                    mat[x][y] = False
##        for x in range(SMALL_LIMIT):
##            mat2[x][0] = False
##            mat2[0][x] = False

        count_time +=1
        
        
    f_out.write('Case #' + str(case) + ': ' + str(count_time) + '\n')

f_out.close()
f_in.close()

print (time.ctime())

