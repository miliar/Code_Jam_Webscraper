#!/usr/bin/env python
# -*- coding: utf-8 -*-
def verify(index, content):
    count = index * 5 + 1
    index += 1
    content_matrix = []
    for i in xrange(4):
        content_matrix.append(list(content[count + i]))
    for i in xrange(4):
        if sum(1 for j in xrange(4) \
                if content_matrix[i][j] == 'X' or content_matrix[i][j] == 'T') == 4 \
                or sum(1 for j in xrange(4) \
                        if content_matrix[j][i] == 'X' or content_matrix[j][i] == 'T') == 4:
            return 'Case #{index}: X won'.format(index=index)
        elif sum(1 for j in xrange(4) \
                if content_matrix[i][j] == 'O' or content_matrix[i][j] == 'T') == 4 \
                or sum(1 for j in xrange(4) \
                        if content_matrix[j][i] == 'O' or content_matrix[j][i] == 'T') == 4:
            return 'Case #{index}: O won'.format(index=index)
    if sum(1 for i in xrange(4) for j in xrange(4) if i == j \
            and (content_matrix[i][j] == 'X' or content_matrix[i][j] == 'T')) == 4 \
            or sum(1 for i in xrange(3, -1, -1) for j in xrange(4) if i + j == 3 \
                    and (content_matrix[i][j] == 'X' or content_matrix[i][j] == 'T')) == 4:
        return 'Case #{index}: X won'.format(index=index)
    elif sum(1 for i in xrange(4) for j in xrange(4) if i == j \
            and (content_matrix[i][j] == 'O' or content_matrix[i][j] == 'T')) == 4 \
            or sum(1 for i in xrange(3, -1, -1) for j in xrange(4) if i + j == 3 \
                    and (content_matrix[i][j] == 'O' or content_matrix[i][j] == 'T')) == 4:
        return 'Case #{index}: O won'.format(index=index)
    elif sum(1 for i in xrange(4) for j in xrange(4) if content_matrix[i][j] == '.') > 0:
        return 'Case #{index}: Game has not completed'.format(index=index)
    else:
        return 'Case #{index}: Draw'.format(index=index)

def main():
    with open('A-large.in') as f:
        content = f.read()
    content = content.split('\n')

    for i in xrange(int(content[0])):
        print(verify(i, content))

if __name__ == '__main__':
    main()
