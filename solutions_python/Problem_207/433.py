def match(c, n):
    for i in range(3):
        if c[i] == n:
            c[i] = -1
            return i

def make_color_list(ri, yi, bi):
    colors = [0, 0, 0]
    colors[ri] = 'R'
    colors[yi] = 'Y'
    colors[bi] = 'B'
    return colors

if __name__ == '__main__':
    
    test_cases = int(input())
    for case_no in range(1, test_cases + 1):

        n, r, o, y, g, b, v = map(int, input().split(' '))

        c = [r, y, b]
        c.sort()

        if c[2] > c[0] + c[1]:
            print('Case #' + str(case_no) + ': ' + 'IMPOSSIBLE')
        else:

            print('Case #' + str(case_no) + ': ', end='')
            
            from copy import deepcopy
            c1 = deepcopy(c)
            
            r_ind = match(c1, r)
            y_ind = match(c1, y)
            b_ind = match(c1, b)

            colors = make_color_list(r_ind, y_ind, b_ind)

            n3 = c[0] - (c[2] - c[1])
            n2 = c[1] - n3

            for i in range(n3):
                print(colors[2] + colors[1] + colors[0], end='')
            for i in range(n2):
                print(colors[2] + colors[1], end='')
            for i in range(c[2] - n2 - n3):
                print(colors[2] + colors[0], end='')
            print()

            
