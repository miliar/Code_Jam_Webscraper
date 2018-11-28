# python 3

MSG_DICT = {True: 'YES', False: 'NO'}


def transposed(list_of_lists):
    return list(zip(*list_of_lists))

    
def get_cells_with_elem(data, e):
    cells = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == e:
                cells.append((i, j))  # row, column
    return cells


def get_rows_with_elem(data, e):
    return [i for i in range(len(data)) if e in data[i]]
    
    
def get_cols_with_elem(data, e):
    cols = transposed(data)
    return [j for j in range(len(cols)) if e in cols[j]]
    

if __name__ == '__main__':
    num_cases = int(input())
    for case_num in range(1, num_cases+1):
        #---- read case data ----
        n, m = [int(x) for x in input().split()]
        data = [[int(x) for x in input().split()] for row in range(n)]
        
        #---- calculate ----
        # get sorted list of unique heights
        heights = set()
        for row in data:
            for height in row:
                heights.add(height)
        heights = sorted(heights)
        
        # iterate throught unique heights, ensuring layout is possible
        possible = True
        for height in heights:
            rows = get_rows_with_elem(data, height)
            cols = get_cols_with_elem(data, height)
            valid_rows = [i for i in rows if all([x <= height for x in data[i]])]
            valid_cols = [j for j in cols if all([x <= height for x in transposed(data)[j]])]
            
            cells = get_cells_with_elem(data, height)
            if not all([i in valid_rows or j in valid_cols for i, j in cells]):
                possible = False
                break
            
        
        #---- display results ----
        print('Case #{0}: {1}'.format(case_num, MSG_DICT[possible]))