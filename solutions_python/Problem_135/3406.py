
def get_card(r1, r2):
    sol = set.intersection(r1, r2)

    if len(sol) == 0:
        return "Volunteer cheated!"
    if len(sol) > 1:
        return  "Bad magician!"

    return sol.pop()


for t in range(int(raw_input())):
    a1 = int(raw_input())
    r1 = [set(map(int, raw_input().split())) for i in range(4)]
    a2 = int(raw_input())
    r2 = [set(map(int, raw_input().split())) for i in range(4)]
    print "Case #" + str(t + 1) + ": " +  str(get_card(r1[a1 - 1], r2[a2 - 1]))

