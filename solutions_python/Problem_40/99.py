import re

def mat2str(mat):
    ans = ''
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            ans += str(mat[x][y]) + ' '
        ans = ans.rstrip() + '\n'
    return ans
def getscore(q, fs):
    #print "q=", q
    q = q.strip()
    first = q.find(' ')
    second = q.find('(')
    if second < 0:
        return float(q)

    count = 0
    for i, ch in enumerate(q[second + 1:]):
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1
        if count < 0:
            break
    third = second + 1 + i
    #print third
    value = float(q[:first])
    feature = q[first:second].strip()
    if feature in fs:
        next_q = q[second + 1:third ]
    else:
        next_q = q[third + 2:-1]
    return value * getscore(next_q, fs)




    print 're:', q
    m = re.match('([\d.]+)\s([a-z]+)\s?\((.+)\)\s?\((.+)\)', q)

    if m:
        #print "matched!", m.group(1), ':', m.group(2), ':', m.group(3), ':', m.group(4)
        if m.group(2).strip() in f:
            next_q = m.group(3)
        else:
            next_q = m.group(4)
        #print m.group(1)
        return float(m.group(1)) * getscore(next_q, f)
    else:
        #print "not matched:", q
        return float(q)



def solve(question, animals):
    q = question.strip()[1:-1]
    q = q.replace('( ', '(')
    q = q.replace(' (', '(')
    q = q.replace(' )', ')')
    q = q.replace(') ', ')')

    ans = ''
    for animal in animals:
        features = set(animal.split()[2:])
        score = getscore(q, features)
        ans += '%1.7f\n' % score
        #print features

    return ans


if __name__ == '__main__':
    str_in = 'A-large.in'
    f_in = open(str_in)
    f_out = open(str_in.rstrip('.in') + '.out', 'w')

    N = int(f_in.next().strip())
    for num_q in range(N):
        A = int(f_in.next().strip())
        question = ''
        for line in range(A):
            question += f_in.next().strip()
        animals = []
        n = int(f_in.next().strip())
        for line in range(n):
            animals.append(f_in.next().strip())

        output = 'Case #' + str(num_q + 1) + ': \n' + solve(question, animals) + '\n'
        f_out.write(output)
        print output,

    f_in.close(); f_out.close()
    #print A_D, set_A
