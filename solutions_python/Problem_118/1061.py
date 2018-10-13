# fair_and_square.py
#
# For Google Code Jam 2013
# David Lister
#

def is_palindrome(num):
    test = str(num)
    over = False
    while not over:
        if len(test) == 1 or len(test) == 0:
            return True
        elif test[0] == test[-1]:
            test = test[1:-1]
        else:
            return False

def has_square(num):
    if int(num **(0.5)) == num **(0.5):
        return True
    
    return False

def is_fair_and_square(num):
    if is_palindrome(num):
        if has_square(num):
            if is_palindrome(int(num ** (0.5))):
                return True
    return False


def count_fair_and_square(lst):
    tally = 0
    for num in lst:
        if is_fair_and_square(num):
            tally += 1
        
    return tally

   
fname = raw_input('Please enter file name: ')
fout = str(fname.split('.')[0]) + '.txt'

f = list(open(fname, 'r'))

lst = []
i = 1

over = False
while not over:
    try:
        lst.append(f[i][:-1].split(' '))
        i += 1
    except:
        over = True



output = ''
i = 1
for case in lst:
        output = output + 'Case #' + str(i) + ': ' + str(count_fair_and_square(range(int(case[0]), int(case[1]) + 1))) + '\n'
        i += 1

out = open(fout, 'w')
out.write(output)
out.close()

print output


