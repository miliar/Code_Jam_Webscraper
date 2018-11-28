class Toilet:

    def last_optimal(self, case):
        num_stalls = int(case[0])
        num_people = int(case[1])

        if num_stalls == num_people:
            return '0 0'

        num_left = 0
        num_right = 0

        stall_blocks = []
        stall_blocks.append(num_stalls)


        while num_people > 0:
            num_stalls = max(stall_blocks)
            stall_blocks.remove(num_stalls)

            if num_stalls == 0:  # case when there are a lot of stalls but each gap has only one stall lap
                return '0 0'

            num_stalls -= 1

            num_left = int(num_stalls / 2) # as the middle one is always the optimal one
            num_right = num_stalls - num_left
            stall_blocks.append(num_left)
            stall_blocks.append(num_right)

            num_people -= 1

        return str(max(num_left, num_right)) + ' ' + str(min(num_left, num_right))