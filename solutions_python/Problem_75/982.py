
import sys
import string
import re
import os


def get_answer(combinations,oppositions,call_list):

    comb_dic = {};
    for comb in combinations:
        a,b,c = comb[0],comb[1],comb[2];
        comb_dic[(a,b)]=c;
        comb_dic[(b,a)]=c;
        
    opp_dic = {};  
    for opp in oppositions:
        a,b = opp[0],opp[1];
        opp_dic[(a,b)]= True;
        opp_dic[(b,a)]= True;


    element_list = [];
    
    for call in call_list:

        element_list.append(call);

        while  True:
        
            if len(element_list) > 1 :
                a = element_list[-1];
                b = element_list[-2];
                if comb_dic.has_key((a,b)):
                    del element_list[-1];
                    del element_list[-1];
                    element_list.append(comb_dic[(a,b)]);
                else:
                    break;
            else:
                break;



        new_element = element_list[-1];
    
        
        for element in element_list:
            if opp_dic.has_key((element,new_element)):
                element_list = [];
                break;
            
    
   
    return ', '.join(element_list);



def solve_problem(input_file_path , output_file_path):
        
    input_file = open(input_file_path,"r");
    output_file = open(output_file_path,"w");
    
    test_count  = int(input_file.readline());

    solution_string = "";
    
    
    for index in xrange(test_count):

        test_case = input_file.readline().split();
        
        c_count = int(test_case[0]);
        c = [];
        
        for i in xrange(1,1+ c_count):
           c.append(test_case[i]);

        d_count = int(test_case[1+c_count]);
        d = [];
        
        for i in xrange(1 + c_count + 1,  1 + c_count + 1 + d_count):
           d.append(test_case[i]);

        invoke_count = int(test_case[1+c_count + 1 + d_count]);
        n = test_case[1+c_count + 1 + d_count + 1];
        
       
        answer = get_answer(c,d,n);        
        solution_string = solution_string + "Case #%d: [%s]\n"%(index+1,answer);            

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
        solve_problem(sys.argv[1], os.path.splitext(sys.argv[1])[0]+'.out');
    
    elif len(sys.argv) >= 3:    
        solve_problem(sys.argv[1], sys.argv[2]);
        


if __name__ == "__main__":
    start_me_up();














