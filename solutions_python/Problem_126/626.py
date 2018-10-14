import sys

if len(sys.argv) != 3:
    print("Usage: python scriptA.py <input_file> <output_file>")
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

#input_file = 'sampleA.in'
#output_file = 'sampleA.out'

def generate_all_substrings(mystr):
    for i in xrange(0,len(mystr)):
        for j in xrange(i + 1,len(mystr) + 1):
            yield mystr[i:j]

def count_cons(mystr):
    cnt = max_cnt = 0
    for i in xrange(0,len(mystr)):
        if not mystr[i:i+1] in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
        else:
            if cnt > max_cnt: max_cnt = cnt
            cnt = 0
    if cnt > max_cnt: max_cnt = cnt
    return max_cnt

def check_string(mystr, num):
    cnt = 0
    for tmp in generate_all_substrings(mystr):
        nc = count_cons(tmp)
        if nc >= num: cnt += 1
    return cnt

results = []
with open(input_file, 'r') as f:
    T = int(f.readline())
    for t in xrange(0,T):
        line = f.readline()
        mystr, n = tuple(line.split(' '))
        n = int(n)
        mns = check_string(mystr, n)
        results.append('Case #' + str(t + 1) + ': ' + str(mns) + '\n')

with open(output_file, 'w') as f:
        f.writelines(results)


