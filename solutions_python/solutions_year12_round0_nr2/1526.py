from auxilary import write_result
def get_std_scores(total):
    scores = [total//3]*3
    for i in range(total%3): scores[i]+=1
    return scores

def get_surprising_scores(total):
    if total in (0,1,29,30): return []
    r = total%3
    scores = get_std_scores(total)
    scores[1] += 1
    scores[(r+1)%3] -= 1
    if r == 0:
        scores[0] += 1
        scores[2] -= 1
    return scores

def get_greter_than_p(p, totals):
    std, surp = 0, 0
    for total in totals:
        if len([x for x in get_std_scores(total) if x>=p]) > 0:
            std += 1
        elif len([x for x in get_surprising_scores(total) if x>=p]) > 0:
            surp += 1
    return std, surp

def parse_line(line):
    line = line.split(' ')
    line = [int(i) for i in line]
    s, p, totals = line[1], line[2], line[3:]
    return s, p, totals

input_file = 'B-large.in'
output_file = 'B-large.out'
if __name__ == '__main__':
    res = []
    with open(input_file) as f:
        for line in f.readlines()[1:]:
            s, p, totals = parse_line(line)
            std, surp = get_greter_than_p(p, totals)
            res.append(str(std + min(s,surp)))
    write_result(res, output_file)