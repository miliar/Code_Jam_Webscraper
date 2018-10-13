trendy_type = 'o'
row_col_type = '+'
diag_type = 'x'
empty_type = '.'

model_scores = {
    trendy_type: 2,
    row_col_type: 1,
    diag_type: 1,
    empty_type: 0
}


class ModelSet:

    def __init__(self, size, my_model_type):
        self.my_model_type = my_model_type
        self.dicts = [{row_col_type: 0, diag_type: 0, trendy_type: 0} for _ in range(size)]

    def add(self, i, model_type):
        self.dicts[i][model_type] += 1

    def remove(self, i, model_type):
        self.dicts[i][model_type] -= 1

    def replace(self, i, current_type, new_type):
        self.remove(i, current_type)
        self.add(i, new_type)

    def free(self, i):
        for model_type, count in self.dicts[i].items():
            if model_type != self.my_model_type and count > 0:
                return False
        return True

    def free_without(self, i, remove_type):
        for model_type, count in self.dicts[i].items():
            if model_type == remove_type:
                count -= 1
            if model_type != self.my_model_type and count > 0:
                return False
        return True


def print_ans(case, score, additions):
    print("Case #{0}: {1} {2}".format(case+1, score, len(additions)))
    for model, row, col in additions:
        print(model, row+1, col+1)


def print_grid(g):
    for row in g:
        print(''.join(row))


def get_up_diag(i, j, n):
    return i+j


def get_down_diag(i, j, n):
    return n-1+i-j


def main():
    t = int(input())

    for case in range(t):
        n, m = [int(x) for x in input().strip().split()]

        grid = [[empty_type]*n for _ in range(n)]

        used_rows = ModelSet(n, row_col_type)
        used_cols = ModelSet(n, row_col_type)
        used_down_diags = ModelSet(2*n-1, diag_type)
        used_up_diags = ModelSet(2*n-1, diag_type)

        score = 0
        additions = []

        def set_model(set_row, set_col, set_model_type, new=True, replace=False):
            nonlocal score
            old_model = grid[set_row][set_col]
            grid[set_row][set_col] = set_model_type
            score += model_scores[set_model_type] - model_scores[old_model]
            if new:
                if replace:
                    for addition in additions:
                        if addition[1] == set_row and addition[2] == set_col:
                            addition[0] = set_model_type
                            break
                    else:
                        additions.append([set_model_type, set_row, set_col])
                else:
                    additions.append([set_model_type, set_row, set_col])

        def add_model(add_row, add_col, add_down_diag, add_up_diag, add_model_type, new=True):
            used_rows.add(add_row, add_model_type)
            used_cols.add(add_col, add_model_type)
            used_down_diags.add(add_down_diag, add_model_type)
            used_up_diags.add(add_up_diag, add_model_type)
            set_model(add_row, add_col, add_model_type, new)

        def replace_model(add_row, add_col, add_down_diag, add_up_diag, remove_model_type, add_model_type):
            used_rows.replace(add_row, remove_model_type, add_model_type)
            used_cols.replace(add_col, remove_model_type, add_model_type)
            used_down_diags.replace(add_down_diag, remove_model_type, add_model_type)
            used_up_diags.replace(add_up_diag, remove_model_type, add_model_type)
            set_model(add_row, add_col, add_model_type, replace=True)

        def can_upgrade(add_row, add_col, add_down_diag, add_up_diag, replace_type):
            return (used_rows.free_without(add_row, replace_type) and
                    used_cols.free_without(add_col, replace_type) and
                    used_down_diags.free_without(add_down_diag, replace_type) and
                    used_up_diags.free_without(add_up_diag, replace_type))

        def can_add_trendy(add_row, add_col, add_down_diag, add_up_diag):
            return (used_rows.free(add_row) and used_cols.free(add_col) and
                    used_down_diags.free(add_down_diag) and used_up_diags.free(add_up_diag))

        def can_add_row_col(add_down_diag, add_up_diag):
            return used_down_diags.free(add_down_diag) and used_up_diags.free(add_up_diag)

        def can_add_diag(add_row, add_col):
            return used_rows.free(add_row) and used_cols.free(add_col)

        # read in models
        for model in range(m):
            model_type, row, col = input().strip().split()
            row, col = int(row)-1, int(col)-1

            down_diag = get_down_diag(row, col, n)
            up_diag = get_up_diag(row, col, n)
            add_model(row, col, down_diag, up_diag, model_type, new=False)

        # add trendy models
        # for row in range(n):
        #     for col in range(n):
        #         down_diag = get_down_diag(row, col, n)
        #         up_diag = get_up_diag(row, col, n)
        #         current_type = grid[row][col]
        #         if current_type == empty_type and can_add_trendy(row, col, down_diag, up_diag):
        #             add_model(row, col, down_diag, up_diag, trendy_type)

        # add models
        for row in range(n):
            row = (row - 1) % n
            for col in range(n):
                col = (col + 0) % n
                down_diag = get_down_diag(row, col, n)
                up_diag = get_up_diag(row, col, n)
                current_type = grid[row][col]
                if current_type == empty_type and can_add_row_col(down_diag, up_diag):
                    add_model(row, col, down_diag, up_diag, row_col_type)
                elif current_type == empty_type and can_add_diag(row, col):
                    add_model(row, col, down_diag, up_diag, diag_type)

        # upgrade models
        for row in range(n):
            for col in range(n):
                down_diag = get_down_diag(row, col, n)
                up_diag = get_up_diag(row, col, n)
                current_type = grid[row][col]

                if ((current_type == row_col_type or current_type == diag_type) and
                        can_upgrade(row, col, down_diag, up_diag, current_type)):
                    replace_model(row, col, down_diag, up_diag, current_type, trendy_type)

        print_ans(case, score, additions)
        # print_grid(grid)

if __name__ == '__main__':
    main()
