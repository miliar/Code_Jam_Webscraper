import sys
a = {'\n' : '', ' ': ' ', 'a' : 'y', 'b' : 'h', 'c' : 'e', 'd' : 's', 'e' : 'o', 'f' : 'c', 'g' : 'v', 'h' : 'x', 'i' : 'd', 'j' : 'u', 'k' : 'i', 'l' : 'g', 'm' : 'l', 'n' : 'b', 'o' : 'k', 'p' : 'r', 'q' : 'z', 'r' : 't', 's' : 'n', 't' : 'w', 'u' : 'j', 'v' : 'p', 'w' : 'f', 'x' : 'm', 'y' : 'a', 'z' : 'q'}
#alphabets = a.keys()
#values = a.values()
#for i in alphabets:
#    if not (i in values):
#        break
#print i


test_cases = int(sys.stdin.readline())

def convert(c):
    return a[c]
def solve_test_case(num):
    line = str(sys.stdin.readline())
    result = map(convert, line)
    print "Case #" + str(num) + ": " + (''.join(result))
        
for i in range(test_cases):
    solve_test_case(i+1)
