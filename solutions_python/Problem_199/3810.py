from bitarray import bitarray
import sys
sys.setrecursionlimit(1000000)

IMPOSSIBLE = "IMPOSSIBLE"

HAPPY = "+"
BLANK = "-"

MAX_ALTERNATIVES = 10
MAX_TRIES = 10000


class Solution:
    def __init__(self, states, num_steps):
        self.states = states
        self.num_steps = num_steps

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()


class Case:
    def __init__(self, pancakes_list, k_int, idx):
        self.pancakes_list = pancakes_list
        self.pancakes = None
        self.set_bit_array()
        self.k_int = int(k_int)
        # self.k = None
        # self.set_k_bit_array()
        self.idx = idx
        self.solution = None
        self.num_steps = IMPOSSIBLE
        self.num_tries = 0
        self.already_tried = set()

    def __str__(self):
        return str(self.__dict__)

    def set_bit_array(self):
        self.pancakes = bitarray([bit == HAPPY for bit in self.pancakes_list])

    # def set_k_bit_array(self):
    #     self.k = bitarray([True for i in range(self.k_int)])

    def find_path(self, state, previous_states=list(), steps=0, position=0):
        if state in self.already_tried:
            # print("already tried")
            return None
        self.already_tried.add(state)
        self.num_tries += 1
        if self.num_tries >= MAX_TRIES:
            # print(self.solution)
            # print("max tries")
            return None

        if self.solution is not None and self.solution.num_steps <= steps:
            return None

        if state.all():
            previous_states.append(state)
            self.solution = Solution(previous_states, steps)
            return self.solution

        search_alternatives_iter = state.itersearch(bitarray('0'))

        best_possibility, new_solution = None, None
        alternative_idx = 0
        for position_idx in search_alternatives_iter:
            # print(position_idx)
            alternative_idx += 1
            # if position_idx < position:
            #     continue
            if alternative_idx > MAX_ALTERNATIVES:
                # print([previous_states, state])
                # print("max alternatives")
                continue
            if position_idx + self.k_int > len(self.pancakes_list):
                # print("position_idx + k_int")
                continue

            # print([position, position_idx, self.k_int, len(self.pancakes_list), alternative_idx])

            with open("./states.txt", "a+") as writer:
                # print(state)
                writer.write("{0}{1}\n".format(alternative_idx, state))
                writer.flush()

            new_previous_states = list(previous_states) + [state]
            operator_array = len(self.pancakes_list) * bitarray('0')
            operator_array[0 + position_idx: self.k_int + position_idx] = True
            new_state = state ^ operator_array
            # print([new_previous_states, new_state])

            # if (position_idx + 1 + self.k_int) < len(self.pancakes_list) and \
            #         alternative_idx < MAX_ALTERNATIVES and \
            #         position_idx + 1 > position:
            # if (position_idx + 1 + self.k_int) < len(self.pancakes_list) and \
            #         position_idx + 1 > position:
            if self.num_tries + 1 > MAX_TRIES:
                # print("max tries reached")
                pass
            else:
                new_solution = self.find_path(
                    new_state,
                    previous_states=new_previous_states,
                    steps=steps + 1,
                    position=position_idx + 1)

                if new_solution is not None:
                    if best_possibility is None:
                        best_possibility = new_solution
                    elif best_possibility is not None and \
                            best_possibility.num_steps > new_solution.num_steps:
                        best_possibility = new_solution

        return best_possibility


        # min_steps = None
        # best_states = []
        # for possible_states, possible_steps in all_possibilities:
        #     if min_steps is None or possible_steps < best_states:
        #         min_steps = possible_states
        #         best_states = possible_states

        # return new_states, new_steps

        # return None

    def compute_solution(self):
        print([self.idx, self.k_int, self.pancakes])

        if self.pancakes.all():
            self.solution = Solution([self.pancakes], 0)
            self.num_steps = self.solution.num_steps
        else:
            self.solution = self.find_path(self.pancakes)

            if self.solution is None:
                self.num_steps = IMPOSSIBLE
            elif not self.solution.states[-1:][0].all():
                self.num_steps = IMPOSSIBLE
            else:
                # print(self.solution.states[-1:][0])
                self.num_steps = self.solution.num_steps
        # print([self.solution, self.num_steps])


def parse_case(line, idx):
    pancakes, k = line.split(" ")
    return Case(list(pancakes), k, idx)


def main():
    cases = []
    # input_file = "./A-small-attempt0.in"
    input_file = "./A-large.in"

    import os
    if os.path.exists("./states.txt"):
        os.remove("./states.txt")

    with open(input_file) as reader:
        with open(input_file + ".out.txt", "w+") as writer:
            num_cases = int(reader.readline().strip())
            for idx in range(1, num_cases+1):
                case = parse_case(reader.readline().strip(), idx)
                cases.append(case)
                case.compute_solution()
                print case.num_steps
                writer.write("Case #{0}: {1}\n".format(case.idx, case.num_steps))
                writer.flush()

if __name__ == '__main__':
    main()
