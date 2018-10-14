def main():
    num_cases = int(input())
    for case in range(1, num_cases + 1):
        row_id = int(input()) - 1
        square = ([input().split(),
                  input().split(),
                  input().split(),
                  input().split()])
        row = set(square[row_id])
        
        row_id = int(input()) - 1
        square = ([input().split(),
                  input().split(),
                  input().split(),
                  input().split()])

        row &= set(square[row_id])
        output = ""
        if len(row) == 1:
            output = str(list(row)[0])
        elif len(row) == 0:
            output = "Volunteer cheated!"
        else:
            output = "Bad magician!"
        print("Case #{}: {}".format(case, output))

if __name__ == '__main__':
    main()
