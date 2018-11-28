from sys import argv

def calc_winner(numOfBlocks, x, y):
    area = x * y
    
    for i in range(1, numOfBlocks+1):
        if numOfBlocks % i == 0:
            j = numOfBlocks/i
            if i > x and i > y:
                if j > y and j > x:
                    return "RICHARD"
    
    if area % numOfBlocks == 0:
        if numOfBlocks > 2:
            if numOfBlocks >= area:
                return "RICHARD"
        if numOfBlocks == 4 and (x == 2 or y == 2):
            return "RICHARD"
        
        return "GABRIEL"
    else:
        return "RICHARD"

if __name__ == "__main__" and True:
    output = ""
    with open(argv[1], 'r') as f:
        cases = int(f.readline())
        for i in range(1, cases+1):
            blocks, x, y = f.readline().split(" ")
            winner = calc_winner(int(blocks), int(x), int(y))
            output += "Case #{}: {}\n".format(i, winner)
    
    print(output)
    with open("output.txt", "w") as f:
        f.write(output.strip())
    print("Finished")
            