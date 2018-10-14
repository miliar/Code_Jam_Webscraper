from codejam import readfile, takeby
from bisect import bisect_right

problems = takeby(3, readfile()[1:])

def score(naomi, ken):
    naomi.sort()
    ken.sort()
    score = 0
    while naomi:
        if naomi[0] < ken[0]:
            ken.pop(-1)
            naomi.pop(0)
        else:
            naomi.pop(0)
            ken.pop(0)
            score += 1
    return score

def score_normal(naomi, ken):
    naomi.sort()
    ken.sort()
    score = 0
    while naomi:
        naomi_told = naomi.pop(-1)
        ken_index = bisect_right(ken, naomi_told)
        if ken_index < len(ken):
            ken_told = ken.pop(ken_index)
        else:
            score += 1
            ken_told = ken.pop(0)
    return score

for index, problem in enumerate(problems, 1):
    n, naomi, ken, = problem
    naomi = map(float, naomi.split())
    ken = map(float, ken.split())
    print "Case #%s:" % index, score(naomi[:], ken[:]), score_normal(naomi[:], ken[:])
