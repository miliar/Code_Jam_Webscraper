import sys
import fractions

#input = open('test.in')
input = open('C-small-attempt1.in')
#input = open('B-large.in')
#output = sys.stdout
output = open('C-small-attempt1.out','w')
#output = open('B-large.out','w')
    
def myread():
    return input.readline().rstrip("\n\r")

def int_ize(an_array):
    return map(lambda x: int(x), an_array)

'''def arya(a,b):
    if a > b:
        if a > 2*b:
            return (a - b*(a/b-1),b)
        else:
            return (a - b, b)
    else:
        if b > 2*a:
            return (a,b - )

def bryan(a,b):
    if a > b:
        return (a-b,b)
    else:
        return (a,b-a)'''

def winning(a,b):
    if a == b:
        return False
    gcd = fractions.gcd(a,b)
    if gcd == a or gcd == b:
        return True

    a = a/gcd
    b = b/gcd

    if a > b:
        if a >= b*2:
            #if winning(a-b*(a/b))
            return True
        else:
            return not winning(a-b,b)
    if b > a:
        if b >= a*2:
            return True
        else:
            return not winning(a,b-a)

def main():
    n_cases = int(input.readline())
    
    case_no = 1
    while case_no <= n_cases:
        case_result = solve_case()
        output.write("Case #%d: %s\n" % (case_no, case_result))
        case_no+=1
    
def solve_case():
    (a1,a2,b1,b2) = int_ize(myread().split(" "))

    wins = 0
    for a in range(a1,a2+1):
        for b in range(b1,b2+1):
            print "try %d,%d: " % (a,b)
            if winning(a,b):
                wins += 1
                print "winning!"

    return wins

main()
