class AlphabetCake:

    def divide(self, grid):

#        num_blank = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '?':
                    if i == len(grid) - 1 and j == len(grid[i]) - 1:

                        min_i = i
                        while min_i >= 0 and grid[min_i][j] == '?':
                            min_i -=1

                        for count_i in range(min_i+1, i+1):
                            grid[count_i][j] = grid[min_i][j]

                            count_j = j
                            while count_j - 1 >= 0 and grid[i][count_j - 1] == '?':
                                grid[count_i][count_j - 1] = grid[min_i][count_j-1]
                                count_j -= 1
                                #print(grid)

                    continue

                direction = 'H'
                # Fill HORIZONTAL
                orig_j = j
                orig_i = i

                while j - 1 >=0 and grid[i][j-1] == '?':
                    grid[i][j-1] = grid[i][j]
                    direction = 'H'
                    j -=1
                    #print(grid)

                min_j = j
                j = orig_j
                while i - 1 >= 0 and grid[i - 1][j] == '?':
                    while j >= min_j:
                        grid[i-1][j] = grid[i][j]
                        print(grid)
                        j -=1
                    j = orig_j
                    i -=1

                j = orig_j
                i = orig_i

                if j + 1 < len(grid[i]) and grid[i][j + 1] == '?':
                    grid[i][j + 1] = grid[i][j]
                    direction = 'H'
                    j += 1
                    # num_blank -= 1
                    # print(grid)
                j = orig_j

                # L and R are filled, horizontally filled if they have same letters
                if j - 1 >= 0 and grid[i][j] == grid[i][j-1] or j + 1 < len(grid[i]) and grid[i][j] == grid[i][j+1]:
                    direction = 'H'

                if direction == 'H':
                    continue

                # Fill VERTICAL
                orig_i = i
                while i - 1 >= 0 and grid[i-1][j] == '?':
                    grid[i-1][j] = grid[i][j]
                    direction = 'V'
                    i -= 1
                    # num_blank -= 1
                    # print(grid)
                i = orig_i

                while i + 1 < len(grid) and grid[i + 1][j] == '?':
                    grid[i + 1][j] = grid[i][j]
                    direction = 'V'
                    i += 1
                    # num_blank -= 1
                    # print(grid)
                i = orig_i

        # if num_blank > 0:
        #      grid = self.divide(grid)
        return grid
