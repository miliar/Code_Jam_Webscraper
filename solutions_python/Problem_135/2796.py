
def solve(input1, board1, input2, board2):
    answer = set(board1[input1-1]).intersection(set(board2[input2-1]))
    if len(answer) == 1:
        return answer.pop()
    if len(answer) == 0:
        return "Volunteer cheated!"
    return "Bad magician!"

def main():
    numcases = int(input())
    for i in range(numcases):
        input1 = int(input())
        board1 = [map(int, input().split()) for n in range(4)]
        input2 = int(input())
        board2 = [map(int, input().split()) for n in range(4)]
        print('Case #{}: {}'.format(i+1, solve(input1, board1, input2, board2)))

if __name__ == '__main__':
    main()
