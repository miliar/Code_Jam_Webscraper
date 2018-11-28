

def read_input(fname):
    fd=open(fname)
    data=fd.read()
    fd.close()
    return data

#return (X,0,T,.)
def col_count(data,pos_list):
    X_count=0
    O_count=0
    dot_count=0
    T_count=0
    for (row,col) in pos_list:
        if data[row][col] == "X":
            X_count+=1
        elif data[row][col] == "O":
            O_count+=1
        elif data[row][col] == ".":
            dot_count+=1
        elif data[row][col] == "T":
            T_count+=1
        else:
            print "not a know symbolerror"
    return (X_count,O_count,dot_count,T_count)
            


    



#0 X won
#1 0 won
#3   draw
#4   incomplete
def process_game(board_data):
    empty_pos=False
    for i in range(4):
        (X_count,O_count,dot_count,T_count)=col_count(board_data,[(i,0),(i,1),(i,2),(i,3)])
        if X_count == 4 or (X_count==3 and T_count==1):
            return 0
        elif O_count == 4 or (O_count==3 and T_count==1): 
            return 1
        elif not empty_pos and dot_count!=0:
            empty_pos=True
        (X_count,O_count,dot_count,T_count)=col_count(board_data,[(0,i),(1,i),(2,i),(3,i)])
        if X_count == 4 or (X_count==3 and T_count==1):
            return 0
        elif O_count == 4 or (O_count==3 and T_count==1): 
            return 1
        elif not empty_pos and dot_count!=0:
            empty_pos=True
        (X_count,O_count,dot_count,T_count)=col_count(board_data,[(0,0),(1,1),(2,2),(3,3)])
        if X_count == 4 or (X_count==3 and T_count==1):
            return 0
        elif O_count == 4 or (O_count==3 and T_count==1): 
            return 1
        elif not empty_pos and dot_count!=0:
            empty_pos=True
        (X_count,O_count,dot_count,T_count)=col_count(board_data,[(0,3),(1,2),(2,1),(3,0)])
        if X_count == 4 or (X_count==3 and T_count==1):
            return 0
        elif O_count == 4 or (O_count==3 and T_count==1): 
            return 1
        elif not empty_pos and dot_count!=0:
            empty_pos=True
    if empty_pos== False:
        return 3
    else:
        return 4
            
            
    
    


#main
infile_name="small.txt"
raw_data=read_input(infile_name)
raw_data=raw_data.split("\n")
print raw_data
num_of_cases=int(raw_data[0])
print num_of_cases,"games"

raw_data=raw_data[1:]
out_data=[]
for i in range(num_of_cases):
    board_pos=[]
    for j in range(4):
        board_pos.append(raw_data[j])
    raw_data=raw_data[5:]
    print "game ",i, board_pos
    result=process_game(board_pos)
    res_str=0
    res_str="Case #"+str(i+1)+":"
    if result==0:
        res_str+=" X won\n"
    elif result==1:
        res_str+=" O won\n"
    elif result==3:
        res_str+=" Draw\n"
    elif result==4:
        res_str+=" Game has not completed\n"
    else:
        print "error"
    out_data.append(res_str)


outfile=open("result.txt","w")
for i in out_data:
    outfile.write(str(i))
outfile.close()
print out_data
        
        
    
    



