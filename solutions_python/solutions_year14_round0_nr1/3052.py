#Magic Trick

def main(input_file,output_file='output.txt'):
    with open(input_file, 'r') as inf:
        with open(output_file, 'w') as outf:
            #outf.write('\n') #skip first line
            #inf.readline() #skipline
            T = int(inf.readline().rstrip('\n')) #number of cases
            for case in range(T): #read case input
            
                picked_row_1_index = int(inf.readline().rstrip('\n'))-1
                first_pick = []
                for i in range(4):
                    first_pick.append(inf.readline().rstrip('\n').split())
                    
                picked_row_2_index = int(inf.readline().rstrip('\n'))-1
                second_pick = []
                for i in range(4):
                    second_pick.append(inf.readline().rstrip('\n').split())
                
                #check one row verse the others for repeats
                picked_row_1 =set(first_pick[picked_row_1_index])
                picked_row_2 =set(second_pick[picked_row_2_index])
                same_values = []

                for i in picked_row_1:
                    if i in picked_row_2:
                        same_values.append(i)
                if len(same_values)<1: 
                    outf.write('Case #%s: Volunteer cheated!\n'%str(case+1))
                elif len(same_values) == 1:
                    outf.write('Case #%s: %s\n'%(str(case+1),same_values[0]))
                else:
                    outf.write('Case #%s: Bad magician!\n'%str(case+1))
   
   
if __name__=='__main__':
    import sys
    if len(sys.argv)<3:
        main(sys.argv[1])
    else:
        main(sys.argv[1],sys.argv[2])
    
