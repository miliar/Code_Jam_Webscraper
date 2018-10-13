import sys

def ans(first_answer, cards1, second_answer, cards2):
    a = cards1[first_answer-1]
    b = cards2[second_answer-1]
    c = [_a for _a in a if _a in b]

    if len(c) > 1: return "Bad magician!"
    if len(c) == 0: return "Volunteer cheated!"
    return c[0]


with open(sys.argv[1]) as fr, open(sys.argv[1] + '.out', 'w') as fw:
    T = int(fr.readline())
    for i in xrange(T):
        no = i + 1
        first_answer = int(fr.readline())
        cards1 = [] 
        cards1.append(map(int, fr.readline().split(' ')))
        cards1.append(map(int, fr.readline().split(' ')))
        cards1.append(map(int, fr.readline().split(' ')))
        cards1.append(map(int, fr.readline().split(' ')))
        second_answer = int(fr.readline())
        cards2 = [] 
        cards2.append(map(int, fr.readline().split(' ')))
        cards2.append(map(int, fr.readline().split(' ')))
        cards2.append(map(int, fr.readline().split(' ')))
        cards2.append(map(int, fr.readline().split(' ')))
        fw.write("Case #{no}: {ans}\n".format(no=no,ans=ans(first_answer, cards1, second_answer, cards2)))

