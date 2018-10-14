import numpy as np

X = 1
O = -1
T = 2
dot = 0

def all_x(subset):
    return np.all(np.logical_or(subset == X, subset == T))

def all_o(subset):
    return np.all(np.logical_or(subset == O, subset == T))

def is_any_empty_left(state):
    return np.any(state == dot)

def solve_game(state):
    for i in range(4):
        # rows
        if all_x(state[:, i]):
            return("X won")
        elif all_o(state[:, i]):
            return("O won")
        if all_x(state[i, :]):
            return("X won")
        elif all_o(state[i, :]):
            return("O won")
    if all_x(np.diag(state)):
        return("X won")
    elif all_o(np.diag(state)):
        return("O won")
    elif all_x(np.diag(state[::-1,:])):
        return("X won")
    elif all_o(np.diag(state[::-1,:])):
        return("O won")
    if is_any_empty_left(state):
        return("Game has not completed")
    else:
        return("Draw")


if __name__ == '__main__':
    #test = np.array([[X, O, O, X],
    #                [X, O, X, O],
    #                [T, O, dot, O],
    #                [O, X, X, X]])
    #print(solve_game(test))
    f = open( "A-large.in", "r" )
    cases = f.readline().strip();
    for i in range(int(cases)):
        current_case = []
        for j in range(4):
            line = f.readline().strip()
            data = []
            for x in line:
                if x == 'X':
                    data.append(1)
                elif x == 'O':
                    data.append(-1)
                elif x == '.':
                    data.append(0)
                else:
                    data.append(2)
            current_case.append(data)
        f.readline()
        game = np.array(current_case)
        print("Case #%d: %s" % (i+1, solve_game(game)))










