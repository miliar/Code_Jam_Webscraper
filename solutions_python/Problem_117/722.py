
if __name__ == '__main__':
    infile = open('data.in', 'rb')
    num_cases = int(infile.readline())
    for case_num in range(1, num_cases + 1):
        height, width = map(int, infile.readline().split())
        rows = []
        is_ok = []
        mowable = True        
        for row_num in range(height):
            row = map(int, infile.readline().split())
            is_ok.append([True] * len(row))
            rows.append(row)
        if not (width == 1 or height == 1):
            for row_num in range(height):
                row = rows[row_num]
                max_val = max(row)
                for col_num in range(width):
                    if row[col_num] != max_val:
                        is_ok[row_num][col_num] = False
            
            for col_num in range(width):
                max_val = 0
                col = []
                for row_num in range(height):
                    val = rows[row_num][col_num]
                    col.append(val)
                    if val > max_val:
                        max_val = val
                for row_num in range(height):
                    if col[row_num] != max_val:
                        if not is_ok[row_num][col_num]:
                            mowable = False
                            break
        if mowable:
            result = 'YES'
        else:
            result = 'NO'
        print 'Case #%d: %s' % (case_num, result)
