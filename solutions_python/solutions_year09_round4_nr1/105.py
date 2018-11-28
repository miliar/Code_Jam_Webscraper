def num_swaps(matrix):
    visited = set()
    to_visit = [matrix]
    to_visit_tmp = []
    min_swaps = 0
    while True:
        while len(to_visit) > 0:
            matrix = to_visit.pop(0)
            key = tuple(matrix)
            if key in visited:
                continue
            if all_done(matrix):
                return min_swaps
            visited.add(key)
            for i in range(len(matrix)-1):
                to_visit_tmp.append(swap(matrix, i, i+1))
        to_visit = to_visit_tmp
        to_visit_tmp = []
        min_swaps += 1
    return None
        
    
def swap(matrix, i, j):
    matrix = matrix[:]
    tmp = matrix[i]
    matrix[i] = matrix[j]
    matrix[j] = tmp
    return matrix

def all_done(matrix):
    for i in range(len(matrix)):
        if last(matrix[i]) > i:
            return False
    return True

def last(row):
    for i in range(len(row) - 1, -1, -1):
        if row[i] == "1":
            return i
    return 0

def main():
    T = int(raw_input())
    import sys
    for i in range(1, T+1):
        matrix = []
        N = int(raw_input())
        for j in range(N):
            matrix.append(raw_input())

        print "Case #%d: %d" % (i, num_swaps(matrix))



if __name__ == "__main__":
    main()
        
            
