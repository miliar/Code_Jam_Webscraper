import sys
sys.path.append("/Users/jevenson/pers/pers/googlecode")
import base

def solve(problem):
    """
    @problem: (list of list of int) a list where each item is one of the
      lines in the problem. Each item is also a list, of each number in
      the line parsed and separated

    @return: (str)
    """
    added = 0
    total_standing = 0
    prob = list(problem[1])
    for shyness_level, column in enumerate(prob):
        column = int(column)
        if total_standing < shyness_level:
            added += (shyness_level - total_standing)
            total_standing = shyness_level
        total_standing += column
    return added

if __name__ == "__main__":
    base.Settings.parse_int = False
    base.main(solve)
