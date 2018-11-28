# Standing Ovation

def ovation(audience):
    standing = 0
    friends_count = 0
    for k in range(len(audience)):
        if standing < k:
            friends_count += k - standing
            standing = k
        standing += audience[k]
    return friends_count

args = {};

with open('d:\input.txt', 'rt') as in_file:
    line_count = int(in_file.readline())
    for i in range(1, line_count+1):
        line = in_file.readline()
        str_args = line.split()
        s_max = int(str_args[0])
        audience_str = str_args[1]
        audience = []
        for man in audience_str:
            audience.append(int(man))
        args[i] = {'audience': audience}
        
answer = {}
for item in args.items():
    key = item[0]
    value = item[1]
    answer[key] = ovation(**value)

with open('d:\output.txt', 'wt') as out_file:
    for item in answer.items():
        test_num = item[0]
        test_answer = item[1]
        print("Case #%d: %d" % (test_num, test_answer), file=out_file)