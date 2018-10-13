import glob, pprint, os, pickle

PALINSQPALIN_FILE = "list.pkl"

def is_palindrome(num_str):
    ## split base number in two
    N = len(num_str) / 2
    for n in range(N):
        if num_str[n] != num_str[-(n+1)]:
            return False
    return True

def is_funky_palindrome(num_str):
    return is_palindrome(num_str.strip("0"))

def is_good_palindrome(num_str):
    return is_funky_palindrome(str(int(num_str)**2))

def generate_fair_from_fair(length):
    if length==1:
        l = ["0","1","2","3"]
        for el in l:
            yield el
    elif length==2:
        l = ["00","11","22"]
        for el in l:
            yield el
    else:
        l = list(generate_fair_from_fair(length-2))
        print "%d -> %d"%(length-2,len(l))
        for i in l:
            if is_good_palindrome("0"+i+"0"):
                yield("0"+i+"0")
            if is_good_palindrome("1"+i+"1"):
                yield("1"+i+"1")
            if is_good_palindrome("2"+i+"2"):
                yield("2"+i+"2")

def generate_fair_palindromes(maximum):
    l1 = list(generate_fair_from_fair(maximum))
    l2 = list(generate_fair_from_fair(maximum-1))
    l1 = [x.strip('0') for x in l1]
    l2 = [x.strip('0') for x in l2]
    l1[0] = '0'
    l2 = l2[1:]
    palins = l1
    palins.extend(l2)
    palins = [x**2 for x in sorted([int(x) for x in palins])]
    return palins
    
def processquestion(index, a,b):
    print "Case #%d:"%index,
    print a,b


""" generate/get palindrome list """
if not os.path.exists(PALINSQPALIN_FILE):
    ## generate palindromes
    fpalins = generate_fair_palindromes(53)
    pickle.dump(fpalins, open(PALINSQPALIN_FILE, "w"))
    print "wrote {} palinsqpalins to {}".format(len(fpalins), PALINSQPALIN_FILE)
else:
    fpalins = pickle.load(open(PALINSQPALIN_FILE))
    print "loaded {} palinsqpalins from {}".format(len(fpalins), PALINSQPALIN_FILE)
pprint.pprint(fpalins[:100])

""" answer questions """
def answerquestion(A, B):
    return len([x for x in fpalins if A <= x <= B])

output = ""
with open(glob.glob('*.in')[0]) as p:
    numquestions = int(p.readline().strip())
    for questionindex in xrange(numquestions):
        A, B = [int(x) for x in p.readline().strip().split(' ')]
        answer = answerquestion(A, B)
        answer_str = "Case #{}: {}".format(1+questionindex, answer)
        output += answer_str + '\n'
        print answer_str
ofile = open('output', 'w').write(output)
    
