import sys
import copy
import math
import decimal
#obtain the name of the input
def fileName():
    filename = 'input'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print("File was not indicated")
        exit()
    return filename

fn = fileName()
fn_se = fn.split('.')
fn_se = fn_se[0]
file = open(fn, 'r')
out = open(fn_se+'.out', 'w')
line_number = 0
max_testcases = 0

while True:
    line = file.readline()
    if line:
        line = line.replace("\n","")
        inputs = line.split(" ")
        #how many test cases are
        if line_number == 0:
            max_testcases = int(inputs[0])
            line_number = 1
            tc_ln = 0
            continue
        #just check the test cases given
        testcase = line_number
        if testcase > max_testcases:
            break

        S_max = int(inputs[0])
        Ss = list(inputs[1])
        for i in range(0, S_max + 1):
            Ss[i] = int(Ss[i])

        invitations = 0
        persons = Ss[0]
        for i in range(1, S_max + 1):
            delta = 0
            if persons < i and Ss[i] > 0:
                delta = i - persons
                invitations += delta
            persons += Ss[i] + delta

        out.write("Case #"+str(testcase)+": "+str(invitations)+"\n")
        out.flush()
        line_number += 1
    else:
        break
file.close()
out.close()
exit()