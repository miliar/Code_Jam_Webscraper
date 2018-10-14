def checkOneGame(firstRow, secondRow, matrix1, matrix2):
    result = [val for val in matrix1[firstRow-1] if val in matrix2[secondRow-1]]
    if    result == []: return "Volunteer cheated!"
    elif  len(result) == 1: return str(result[0])
    else: return "Bad magician! "
if __name__ == '__main__':
    games = []
    numberOfGames = int(raw_input())
    for i in range(numberOfGames):
        firstRow = int(raw_input())
        matrix1 = [map(int, raw_input().split()) for _ in range(4)]
        secondRow = int(raw_input())
        matrix2 = [map(int, raw_input().split()) for _ in range(4)]
        print("Case #"+str(i+1)+": " + checkOneGame(firstRow, secondRow, matrix1, matrix2))
