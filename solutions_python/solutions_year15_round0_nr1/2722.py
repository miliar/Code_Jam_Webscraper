##
#
#
#   Input :
#           The first line of the input gives the number of test cases T. T test cases follow.
#       Each consists of one line with Smax, the maximum shyness level of the shyest person in the audience
#       Followed by string of Smax + 1 single digits. The kth digit of this string represents how many people in the
#       the audience have shyness level k.
#   Output :
#       For each test case, output one line containing "Case #x : y", where x is the test case number (starting from 1)
#           and y is the minimum number of friends you must invite.
##

test_cases = int(input())

inputs = []

for i in range(test_cases):
    inputs.append((str(input())).split(' '))
# print inputs


optreqA = []
for inp in inputs:

    stood = 0
    optreq = 0
    counter = 0
    for val in str(inp[1]):
       if counter > stood:
           req = counter - stood
           if req > optreq:
                optreq = req

       stood += int(val)
       counter += 1
    optreqA.append(optreq)

counter = 1
for val in optreqA:
    print('Case #' + str(counter) + ': ' + str(val))
    counter += 1




