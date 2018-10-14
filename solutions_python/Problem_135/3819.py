import os.path
import sys

def main(in_file, out_file):
    sols = []
    with open(in_file) as fin:
        num_cases = int(fin.readline().strip())

        for i in range(num_cases):
            first_row_index = int(fin.readline().strip())
            for i in range(1, 5):
                row = fin.readline().strip()
                if i == first_row_index:
                    first_row = {int(r) for r in row.split()}
            second_row_index = int(fin.readline().strip())
            for i in range(1, 5):
                row = fin.readline().strip()
                if i == second_row_index:
                    second_row = {int(r) for r in row.split()}
            solution = first_row.intersection(second_row)
            if len(solution) == 1:
                sols.append(str(solution.pop()))
            elif len(solution) == 0:
                sols.append("Volunteer cheated!")
            else:
                sols.append("Bad magician!")

    with open(out_file, "w") as fout:
        for i, s in enumerate(sols):
            fout.write("Case #{}: {}\n".format(i + 1, s))

if __name__ == "__main__":
    in_file = sys.argv[1]
    base_path, _ = os.path.splitext(in_file)
    out_file = base_path + ".out"
    main(in_file, out_file)