from sets import Set

def solve(lines):
    guess1 = int(lines[0])
    guess2 = int(lines[5])

    s1 = Set([int(x) for x in lines[guess1].split(" ")])
    s2 = Set([int(x) for x in lines[guess2+5].split(" ")])
    s3 = s1.intersection(s2)
    if len(s3) == 0:
        return "Volunteer cheated!"
    elif len(s3) > 1:
        return "Bad magician!"
    else: 
        return s3.pop()
    

input_text = [line.strip() for line in open('q1s.txt')]
CASE_COUNT = int(input_text[0])
NUM_EACH_CASE = 10
for CASE_NUM in range(1,CASE_COUNT+1):
    start = (CASE_NUM-1)*NUM_EACH_CASE+1
    end = start + NUM_EACH_CASE
    arr = [x for x in input_text[start:end]]
    print "Case #%d: %s" % (CASE_NUM,solve(arr))
