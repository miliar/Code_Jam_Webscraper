q_mul_table = {
    '1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
    'i': {'1': 'i', 'i':'-1', 'j': 'k', 'k':'-j'},
    'j': {'1': 'j', 'i':'-k', 'j':'-1', 'k': 'i'},
    'k': {'1': 'k', 'i': 'j', 'j':'-i' ,'k':'-1'}
}

# doesn't work if q1 or q2 starts with '--' or greater
# hopefully, algoryths doesn't suppose this behaveour
def q_mul(q1, q2):
    res = ''
    if q1.startswith('-'):
        res += '-'
        q1 = q1.replace('-', '')
    if q2.startswith('-'):
        res += '-'
        q2 = q2.replace('-', '')
    res += q_mul_table[q1][q2]
    if res.startswith('--'):
        res = res.replace('--', '')
    return res

NOT_FOUND = -1

def dijkstra(string):
    reduct_str = 'ijk'
    separator = 0
    for symbol in reduct_str:
        separator = find_separator(symbol, string, separator)
        if separator == NOT_FOUND:
            return False
    if separator == len(string):
        return True
    elif separator == NOT_FOUND:
        return False
    else:
        end = multimply_leftovers(string, separator)
        if end == '1':
            return True
        else:
            return False
        
def find_separator(symbol, string, start_index):
    current_reduction = '1'
    i = start_index
    while i < len(string) and current_reduction != symbol:
        current_reduction = q_mul(current_reduction, string[i])
        i += 1
    if current_reduction == symbol:
        return i
    else:
        return NOT_FOUND

def multimply_leftovers(string, start_index):
    current_reduction = '1'
    i = start_index
    while i < len(string):
        current_reduction = q_mul(current_reduction, string[i])
        i += 1
    return current_reduction
    
class RepeatableString:
    def __init__(self, string, repeat):
        self.string = string
        self.repeat = repeat
        self.length = repeat * len(string)

    def __len__(self):
        return self.length

    def __getitem__(self, i):
        if 0 <= i < len(self):
            string_index = i % len(self.string)
            return self.string[string_index]
        else:
            raise IndexError("index out of range")

    def __str__(self):
        res = ""
        for b in self:
            res += str(b)
        return res
    
    args = {};
    
# split
with open('d:\input.txt', 'rt') as in_file:
    test_count = int(in_file.readline())
    for i in range(1, test_count+1):
        line = in_file.readline()
        str_args = line.split()
        period = int(str_args[0])
        repeat = int(str_args[1])
        string = in_file.readline().split()[0]
        args[i] = {'string': RepeatableString(string, repeat)}
        
answer = {}

for item in args.items():
    key = item[0]
    value = item[1]
    answer[key] = dijkstra(**value)

with open('d:\output.txt', 'wt') as out_file:
    for item in answer.items():
        test_num = item[0]
        if item[1]:
            test_answer = "YES"
        else:
            test_answer = "NO"
        print("Case #%d: %s" % (test_num, test_answer), file=out_file)