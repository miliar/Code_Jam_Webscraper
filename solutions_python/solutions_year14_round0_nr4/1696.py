__author__ = 'klaxon'


class Problem:
    def __init__(self, naomi, ken):
        self.naomi = sorted(naomi)
        self.ken = sorted(ken)


def read_problems_form(fileName):
    f = open(fileName, "r")
    f.readline()

    problems = []
    #skip array count
    line = f.readline()
    while line:
        naomi = [float(weight) for weight in f.readline().split(" ")]
        ken = [float(weight) for weight in f.readline().split(" ")]
        problems.append(Problem(naomi, ken))
        line = f.readline()

    return problems


def solve_war(p):
    naomi_list = list(p.naomi)
    ken_list = list(p.ken)

    #ken win phase
    for n in naomi_list:
        try:
            ken_higher_weight = next(x for x in ken_list if x > n)
        except StopIteration:
            return len(ken_list)

        ken_list.remove(ken_higher_weight)

    return 0


def solve_deceitful_war(p):
    naomi_list = list(p.naomi)
    ken_list = list(p.ken)

    result = 0
    while naomi_list:
        n = naomi_list[0]
        k = ken_list[0]
        if n < k:
            del naomi_list[0]
            del ken_list[-1]
        else:
            result += 1
            del naomi_list[0]
            del ken_list[0]

    return result



problemList = read_problems_form("in.txt")

result = ""
for (index, problem) in enumerate(problemList, 1):
    result += "Case #" + repr(index) + ": " + repr(solve_deceitful_war(problem)) + " " + repr(solve_war(problem))
    result += "\n"


result_file = open("result.txt", "w")
result_file.write(result)
result_file.close()

