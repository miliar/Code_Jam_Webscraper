# NOTE
# This program bruteforces the solution, it won't work for the large dataset
# as it quite simply doesn't find an end in time ...


#Tidy numbers are where digits are in NON_DESCREASING order
# tidy
# 8, 123, 55555, 1234567

# NOT tidy
# 92, 101010, 321, 495

#### INPUT
# First line is T, T lines follow
# Each line describes a case with a single N
#   N, User counts from 1 to N (N is last number counted, inclusive)

#### OUTPUT
#For each case, output Case #x y
#x = case #, starting from 1
#y = last tidy number encountered when counting to N

# examples
# 132, answer is 129 as 129 is the last number with non-decreasing digits
# 1000, answer is 999
# 7, 7. Done, 1 digit numbers are done

def caseOutput(x, y):
    """Construct a string like Case #X: Y"""
    return 'Case #' + str(x) + ': ' + str(y);

def isTidy(n):
    #x = int(n);
    #for i in range(x,-1,-1):

    ns = str(n);
    for i in range(0, len(ns)-1):
        if(ns[i] > ns[i+1]):
            return False;
    return True;

inFile = open('./B-small-attempt0.in', 'r');

cases = int(inFile.readline());
for x in range(1,cases+1):
    ns = inFile.readline().rstrip('\n');
    n = int(ns);

    if(len(ns) == 1):
        print(caseOutput(x, n));
    else:
        while(n > 0):
            if(isTidy(n)):
                print(caseOutput(x, n));
                break;
            n -= 1;

inFile.close();
