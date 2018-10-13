def solve(set1, answer1, set2, answer2):
    row1 = set1[answer1-1]
    row2 = set2[answer2-1]
    inter = row1 & row2
    if len(inter) == 0:
        return "Volunteer cheated!"
    elif len(inter) > 1:
        return "Bad magician!"
    else:
        return inter.pop()

t = int(input())
for case in range(t):
    answer1 = int(input())
    set1 = [{int(i) for i in input().split(' ')} for x in range(4)]
    answer2 = int(input())
    set2 = [{int(i) for i in input().split(' ')} for x in range(4)]
    print("Case #%d:" % (case+1), solve(set1, answer1, set2, answer2))
