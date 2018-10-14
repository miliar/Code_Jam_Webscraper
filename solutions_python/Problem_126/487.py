vowels = set(list('aeiou'))

def cont(s):
    s = set(list(s))
    if len(s.intersection(vowels)) == 0:
        return True
    else:
        return False

in_data = open('A-small-attempt0.in').readlines()
in_data = [x.strip() for x in in_data]
T = int(in_data[0])
in_data = in_data[1:]

wfile = open('result', 'w')
for case_no in range(T):
    count = 0
    line = in_data[0]
    in_data = in_data[1:]
    s, n = line.split()
    n = int(n)
    ss = 0
    for i in range(0, len(s)-n+1):
        if cont(s[i:(i+n)]):
            count += (i - ss + 1) * (len(s) - i - n + 1)
            ss = i + 1
    output = 'Case #' + str(case_no+1) + ': ' + str(count) + '\n'
    wfile.write(output)    
