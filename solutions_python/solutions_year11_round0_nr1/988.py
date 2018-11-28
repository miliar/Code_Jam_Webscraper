
import sys
import string
import re


def get_next_position(robot, current_robot_pos, ops,current_op):
    for i in xrange(current_op,len(ops)):
       if ops[i][0] == robot:
           return ops[i][1];
    return current_robot_pos;



def get_answer(ops):
    print ops;            
    print len(ops);
    
    b_pos = 1;      
    o_pos = 1;      
                        
    current_op = 0;         

    secs = 0;    

                    
    next_b_pos = get_next_position('B',b_pos,ops,current_op);
    next_o_pos = get_next_position('O',o_pos,ops,current_op);

    
    
    while current_op < len(ops):

        secs = secs + 1;

        turn = ops[current_op][0];
        
        if turn is 'O':
            if o_pos is next_o_pos:
                current_op = current_op + 1;
        elif turn is 'B':
            if b_pos is next_b_pos:
                current_op = current_op + 1;
           

        
        if b_pos is not next_b_pos:
            if next_b_pos > b_pos:
                b_pos = b_pos+1;
            else:
                b_pos = b_pos-1;
                
        if o_pos is not next_o_pos:
            if next_o_pos > o_pos:
                o_pos = o_pos+1;
            else:
                o_pos = o_pos-1;

        next_b_pos = get_next_position('B',b_pos,ops,current_op);
        next_o_pos = get_next_position('O',o_pos,ops,current_op);

    return secs;





def solve_problem(input_file_path , output_file_path):
        
    input_file = open(input_file_path,"r");
    output_file = open(output_file_path,"w");
    
    test_count  = int(input_file.readline());

    solution_string = "";
    
    
    for index in xrange(test_count):

        test_case = input_file.readline().split();

        print test_case;
        
        op_count = int(test_case[0])*2;
        ops = [];
        positions = [];

        for i in xrange(1,op_count+1):
            if test_case[i] =='O'  or test_case[i] == 'B':
                ops.append(test_case[i]);
            else:
                positions.append(int(test_case[i]));

        print ops
        print positions
        answer = get_answer(zip(ops,positions));
        
        
        solution_string = solution_string + "Case #%d: %d\n"%(index+1,answer);            

    print solution_string;
    output_file.write(solution_string+'\n');

    
    input_file.close()
    output_file.close()

    
def  start_me_up():
    if len(sys.argv) == 1:
        print "Usage:"
        print "%s input_file_path [output_file_path]" % ( sys.argv[0]);
        print "Note: Solution is output to console too." ;      

    elif len(sys.argv) == 2:
        solve_problem(sys.argv[1], sys.argv[1]+'.out');
    
    elif len(sys.argv) >= 3:    
        solve_problem(sys.argv[1], sys.argv[2]);
        


if __name__ == "__main__":
    start_me_up();














