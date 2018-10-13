__author__ = 'prashanthg'
"""
codejam problem:
https://code.google.com/codejam/contest/2974486/dashboard
"""
import numpy as np

def ParseCases(text):
    """splits the string and outputs required matrices"""
    lines = text.splitlines()
    num_cases = int(lines[0])
    first_ans = []
    first_arr = []
    second_ans = []
    second_arr = []
    line_index = 1
    for i in range(num_cases):
        first_ans.append(int(lines[line_index].split()[0]))
        print "To matrix", ToMatrix(lines[line_index + 1: line_index + 5])
        first_arr.append(ToMatrix(lines[line_index + 1: line_index + 5]))
        line_index += 5
        second_ans.append(int(lines[line_index].split()[0]))
        second_arr.append(ToMatrix(lines[line_index + 1: line_index + 5]))
        line_index += 5
    return {'numCases': num_cases, 'ans_1': first_ans,'ans_2': second_ans,'arr_1': first_arr,'arr_2': second_arr}

def ToMatrix(lines):
    """converts 4 lines to matrix"""
    #print lines
    arr = np.zeros([4, 4])
    for j in xrange(4):
        arr[j, :] = np.array([int(num) for num in lines[j].split(" ")])
        #print np.array([int(num) for num in lines[j].split(" ")])
    return arr

def SolveMagic(cases, out_file_name):
    """solves for the magic trick and returns values"""
    with open(out_file_name, 'wb') as out:
        for i in range(cases["numCases"]):
            first_arr = cases['arr_1'][i]
            # find first row
            #index = np.where( first_arr == cases['ans_1'][i] )
            #print index
            row_1 = first_arr[cases['ans_1'][i] - 1]
            # find second row
            second_arr = cases['arr_2'][i]
            #index = np.where( second_arr == cases['ans_2'][i] )
            row_2 = second_arr[cases['ans_2'][i] - 1]

            print "cases comparison: "
            print row_1
            print row_2
            result = np.in1d(row_1, row_2)
            print result
            print np.sum(result)
            # use cases and write to file
            if np.sum(result) == 1: # found answer
                ans = row_1[np.where(result == True)]
                out.write("Case #{i}: {ans}\n".format(i = i+1, ans = str(int(ans[0]))))
            elif np.sum(result) > 1:
                out.write("Case #{i}: {ans}\n".format(i = i+1, ans = "Bad magician!"))
            else:
                out.write("Case #{i}: {ans}\n".format(i = i+1, ans = "Volunteer cheated!"))


if __name__ == "__main__":
    inp_file_name = 'A-small-attempt0.in'
    out_file_name = 'A-small-attempt0.out'
    with open(inp_file_name, 'rb') as inp:
        out = open(out_file_name, 'wb')
        cases = ParseCases(inp.read())
        #print cases
        SolveMagic(cases, out_file_name)

