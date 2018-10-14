import numpy as np
import sys

def read_matrix(file_in):
    board1=''
    board2=''
    ans1=int(file_in.readline())
    for i in range(4):
        board1 += file_in.readline()
    
    ans2=int(file_in.readline())
    for i in range(4):
        board2 += file_in.readline()
    board1= np.array(board1.split()).reshape(4,4)
    board2= np.array(board2.split()).reshape(4,4)
    return ans1, board1, ans2, board2
        
def get_row(board_in, ans_in):
    row_in=board_in[ans_in,:]
    return row_in
    


file = open(sys.argv[1],'r')
num_cases = int(file.readline())
file_out = open("output.out",'wr')
print num_cases
for i in range(num_cases):
    ans1, board1, ans2, board2 = read_matrix(file)
    #print board1
    #print board2
    row1 = get_row(board1,ans1-1)
    row2 = get_row(board2,ans2-1)
    #print row1
    #print row2
    bool_acc = True
    count=0
    num=[]
    for j in range(4):
        for k in range(4):
            if (row1[j] == row2[k]):
                count += 1
                num= row1[j]
    #print count
    if (count==1):
        print str(i)+": ",num
        string = 'Case #%s:'%(i+1)+' '+str(num)+'\n'
        file_out.write(string) 
    if (count>1):
        print str(i)+": ","Bad magician!"
        string = 'Case #%s:'%(i+1)+" Bad magician!\n"
        file_out.write(string) 
    if (count==0):
        print str(i)+": ","Volunteer cheated!"
        string = 'Case #%s:'%(i+1)+" Volunteer cheated!\n"
        file_out.write(string) 
