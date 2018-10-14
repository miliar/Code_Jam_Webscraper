def main():
    T = int(input())

    for T in range(T):
        print("Case #{}: {}".format(T+1, solve()))
        
def solve():
    row_1 = int(input())
    grid_1 = get_grid()
    possible_1 = set(grid_1[row_1-1])
    
    row_2 = int(input())
    grid_2 = get_grid()
    possible_2 = set(grid_2[row_2-1])

    newLen = len(possible_1 - possible_2)
    #print(len(possible_1 - (possible_1 - possible_2)))
    if (newLen < 3):
        return "Bad magician!"
    if (newLen == 4):
        return "Volunteer cheated!"
    return tuple(possible_1 - (possible_1 - possible_2))[0]
    
    #print_grid(grid_1)
    #print_grid(grid_2)

    

def print_grid(grid):
    for row in grid:
        print(row)
    print()
    
def get_grid():
    return [list(map(lambda x: int(x), input().split())) for i in range(4)]
    
if __name__ == '__main__':
    main()
