#!/usr/bin/env python
# -*- coding: utf-8 -*-
def solve(index, N, M, content):
    index += 1
    if N == 1 or M == 1:
        return 'Case #{index}: YES'.format(index=index)
    content_matrix = []
    for i in xrange(N):
        content_matrix.append(content[i].split())
    for i in xrange(N):
        for j in xrange(M):
            if sum(1 for k in xrange(N) \
                    if content_matrix[k][j] > content_matrix[i][j]) > 0 \
                    and sum(1 for k in xrange(M) \
                            if content_matrix[i][k] > content_matrix[i][j]) > 0:
                return 'Case #{index}: NO'.format(index=index)
    return 'Case #{index}: YES'.format(index=index)

def main():
    with open('B-small-attempt2.in') as f:
        content = f.read()
    content = content.split('\n')

    j = 1
    for i in xrange(int(content[0])):
        N, M = map(int, content[j].split())
        print(solve(i, N, M, content[j+1:j+N+1]))
        j += N + 1

if __name__ == '__main__':
    main()
