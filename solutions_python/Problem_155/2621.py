from __future__ import print_function
from concurrent.futures import ProcessPoolExecutor
import Tkinter
import time
from tkFileDialog import askopenfilename
root = Tkinter.Tk()

def read_input_file():
    empty_list = []
    filename = askopenfilename(parent=root)
    f = open(filename,"r")
    start = int(round(time.time() * 1000))
    no_of_test_cases = int(f.readline())
    for i in range(1,no_of_test_cases+1):
        credit_amount = int(f.readline())
        no_of_credit_inputs = f.readline()
        credit_inputs = [int(item) for item in f.readline().split(" ")]
        empty_list.append((credit_amount,credit_inputs,i))
    f.close()
    pool	=	ProcessPoolExecutor(max_workers=4)
    results	=	list(pool.map(solve_credit_problem,empty_list))
    print_to_output_file(results)
    end = int(round(time.time() * 1000))
    print("Time Taken: ",end-start)

def solve_credit_problem(input):
    credit_amount,credit_input,case_number = input
    for index1,item1 in enumerate(credit_input):
        for index2,item2 in enumerate(credit_input):
            if item1+item2 == credit_amount and index1 <> index2:
                return "Case #"+str(case_number)+":",index1+1,index2+1

def solve_credit_problem_efficient(input):
     credit_amount,_input,case_number = input
     credit_input = sorted(_input)
     length = len(credit_input)
     i,j = 0,length-1
     while i < j:
         net_amount = credit_input[i] + credit_input[j]
         if net_amount  == credit_amount:
             return "Case #"+str(case_number)+":",_input.index(credit_input[i])+1,_input.index(credit_input[j])+1
         elif net_amount > credit_amount:
             j = j-1
         else:
             i = i + 1
     return None

def print_to_output_file(output):
    output_file = open("output3.txt","wb")
    for item in output:
        a,b,c = item
        if b == c:
            b = b + 1
        if b > c:
            print(a,c,b,file=output_file)
        else:
            print(a,b,c,file=output_file)
    output_file.close()
def main():
    read_input_file()

if __name__=='__main__':
    main()