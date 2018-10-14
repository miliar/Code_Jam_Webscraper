from enum import Enum


class MagicTrickSolutionType(Enum):
    Normal = 1
    BadMagician = 2
    VolunteerCheated = 3


class MagicTrickSolution:
    solution_type = MagicTrickSolutionType.Normal
    solution_value = -1


class MagicTrickInput:
    first_row = None
    first_table = None
    second_row = None
    second_table = None


class MagicTrickInputParser:
    @staticmethod
    def get_magic_trick_input(f):
        ret = MagicTrickInput()
        ret.first_row = int(f.readline()) - 1
        ret.first_table = MagicTrickInputParser.__read_table(f)
        ret.second_row = int(f.readline()) - 1
        ret.second_table = MagicTrickInputParser.__read_table(f)

        return ret

    @staticmethod
    def __read_table(f):
        ret = []
        for i in range(0, 4):
            zz = [int(x) for x in f.readline().split()]
            ret.append(set(zz))

        return ret


class MagicTrickInputSolver:
    @staticmethod
    def solve_problem(problem):
        """
        @type problem: MagicTrickInput
        """
        first_set = problem.first_table[problem.first_row]
        second_set = problem.second_table[problem.second_row]
        intersection_set = first_set.intersection(second_set)

        ret = MagicTrickSolution()
        intersection_count = len(intersection_set)
        if intersection_count > 1:
            ret.solution_type = MagicTrickSolutionType.BadMagician
        elif intersection_count == 0:
            ret.solution_type = MagicTrickSolutionType.VolunteerCheated
        else:
            ret.solution_type = MagicTrickSolutionType.Normal
            ret.solution_value = list(intersection_set)[0]

        return ret


class MagicTrickSolutionPrinter:
    @staticmethod
    def print_solution(solution, solution_number):
        """
        @type solution: MagicTrickSolution
        """
        caseString = "Case #" + str(solution_number) + ": "
        if solution.solution_type == MagicTrickSolutionType.VolunteerCheated:
            print(caseString + "Volunteer cheated!")
        elif solution.solution_type == MagicTrickSolutionType.BadMagician:
            print(caseString + "Bad magician!")
        else:
            print(caseString + str(solution.solution_value))


def main():
    f = open("input.txt", 'r')
    test_cases = int(f.readline())
    for x in range(1, test_cases+1):
        magic_trick_input = MagicTrickInputParser.get_magic_trick_input(f)
        solution = MagicTrickInputSolver.solve_problem(magic_trick_input)
        MagicTrickSolutionPrinter.print_solution(solution, x)


if __name__ == "__main__":
    main()