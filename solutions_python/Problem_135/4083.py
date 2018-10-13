import sys

def main():
    if len(sys.argv) == 0:
        print("No file provided")
    else:
        in_file = sys.argv[1]
        solve(open(in_file))

def solve(data_file):
    cases = int(data_file.readline().strip())
    output = ""

    for i in range (cases):
        row_pick = int(data_file.readline().strip())
        rows = []
        for row in range(4):
            data = data_file.readline().strip().split(' ')
            data = [int(x) for x in data]
            rows += [data]
        potential_answers = rows[row_pick - 1]
        
        new_pick = int(data_file.readline().strip())
        new_rows = []
        for row in range(4):
            data = data_file.readline().strip().split(' ')
            data = [int(x) for x in data]
            new_rows += [data] 

        results = []
        for x in range(4):
            if new_rows[new_pick-1][x] in potential_answers:
                results += [new_rows[new_pick-1][x]]
        print("Case #" + str(i + 1) + ": ", end="")
        if len(results) == 0:
            print("Volunteer cheated!")
        elif len(results) == 1:
            print(results[0])
        else:
            print("Bad magician!")

if __name__ == "__main__":
   main()
