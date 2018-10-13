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
tc_ln = 0
testcase = 1

qt_m = {'1': {'1':'1', 'i':'i', 'j':'j', 'k':'k'},
        'i': {'1':'i', 'i':'-1', 'j':'k', 'k':'-j'},
        'j': {'1':'j', 'i':'-k', 'j':'-1', 'k':'i'},
        'k': {'1':'k', 'i':'j', 'j':'-i', 'k':'-1'}}

L = 0
X = 0
Ls = []
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
        if testcase > max_testcases:
            break

        if tc_ln == 0:
            L = int(inputs[0])
            X = int(inputs[1])

        if tc_ln == 1:
            Ls = list(inputs[0])

        tc_ln += 1
        if tc_ln > 1:
            answer = 'NO'

            tot_l = X*L

            find_i = True
            str_i = ''
            find_j = True
            str_j = ''
            find_k = True
            str_k = ''

            prev = '1'
            str_prev = ''
            sign_prev = False
            for xs in range(tot_l):
                mx = xs%L

                new = qt_m[prev][Ls[mx]]

                str_new = str_prev + Ls[mx]

                sign_new = False
                if new.find('-') == 0:
                    sign_new = True
                new = new.replace('-', '')
                sign_new = sign_new != sign_prev

                if new == '1' and not sign_new:
                    prev = '1'
                    str_prev = ''
                    sign_prev = False
                    continue

                if find_i:
                    if new == 'i' and not sign_new:
                        str_i = str_new
                        find_i = False
                        prev = '1'
                        str_prev = ''
                        sign_prev = False
                        continue
                elif find_j:
                    if new == 'j' and not sign_new:
                        str_j = str_new
                        find_j = False
                        prev = '1'
                        str_prev = ''
                        sign_prev = False
                        continue
                elif find_k:
                    if new == 'k' and not sign_new:
                        str_k = str_new
                        find_k = False
                        prev = '1'
                        str_prev = ''
                        sign_prev = False
                        continue                    

                prev = new
                str_prev = str_new
                sign_prev = sign_new
            if not find_k and prev == '1' and not sign_prev:
                answer = 'YES'
            out.write("Case #"+str(testcase)+": "+answer+"\n")
            out.flush()

            tc_ln = 0

            testcase += 1
        line_number += 1
    else:
        break
file.close()
out.close()
exit()