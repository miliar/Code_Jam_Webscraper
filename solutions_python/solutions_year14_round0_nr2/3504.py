class CookieClickerInput:
    c = 0
    f = 0
    x = 0


class CookieClickerSolver:
    """
    @type problem_input: CookieClickerInput
    """
    problem_input = None

    @staticmethod
    def solve_problem(problem_input):
        """
        @type problem_input: CookieClickerInput
        """
        solver = CookieClickerSolver()
        solver.problem_input = problem_input

        return solver.__solve_problem()

    def __solve_problem(self):
        num_farms = 0
        t = self.__time_to_purchase_farms(0) + self.__time_to_purchase_cookies_having_purchased_farms(0)
        minimum_t_found = False
        while not minimum_t_found:
            num_farms += 1
            new_t = self.__time_to_purchase_farms(num_farms) + self.__time_to_purchase_cookies_having_purchased_farms(
                num_farms)
            if new_t < t:
                t = new_t
            else:
                minimum_t_found = True

        return t

    def __time_to_purchase_farms(self, farm_count):
        ret = 0
        c = self.problem_input.c
        f = self.problem_input.f
        for x in range(0, farm_count):
            ret += c / (2 + x * f)

        return ret

    def __time_to_purchase_cookies_having_purchased_farms(self, purchased_farms):
        f = self.problem_input.f
        x = self.problem_input.x
        return x / (2 + purchased_farms * f)


def main():
    f = open("input.txt", 'r')
    test_cases = int(f.readline())
    for x in range(1, test_cases + 1):
        problem_parameters = [float(x) for x in f.readline().split()];
        problem_input = CookieClickerInput()

        problem_input.c = problem_parameters[0]
        problem_input.f = problem_parameters[1]
        problem_input.x = problem_parameters[2]

        print("Case #" + str(x) + ": " + str(CookieClickerSolver.solve_problem(problem_input)))

if __name__ == "__main__":
    main()