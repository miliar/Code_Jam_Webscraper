'''
Created on Apr 12, 2014

@author: jirasch
'''

def solve(c):
    n1 = int(c[0]) - 1
    n2 = int(c[5]) - 1
    case1 = [x.split(' ') for x in c[1:5]]
    case2 = [x.split(' ') for x in c[6:10]]
    case1 = set(case1[n1])
    case2 = set(case2[n2])
    icase = case1.intersection(case2)
    if len(icase) == 1:
        return list(icase)[0]
    elif len(icase) > 1:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'

if __name__ == '__main__':    
    afile = file('A-small-attempt0.in')
    lines = afile.read().splitlines()
    afile.close()
    
    num = int(lines[0].strip())
    
    cases = [lines[(1 + (i * 10)):(1+ (i * 10)) + 10] for i in range(num)]
    i = 1
    for c in cases:
        print 'Case #%d: %s' % (i, solve(c))
        i += 1
