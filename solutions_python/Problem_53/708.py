import sys
inputs_amnt = int(sys.stdin.readline())

for case_number in range(1,inputs_amnt+1):
    (n,k) = ( int(x) for x in sys.stdin.readline().split(' ') )
    if k%(2**n) == (2**n)-1:
        case_solution = 'ON'
    else:
        case_solution = 'OFF'
    sys.stdout.write('Case #%s: %s\n' % (case_number, case_solution))