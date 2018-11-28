# -*- coding: utf-8 -*-

from sys import exit, stdin
from pprint import PrettyPrinter
from itertools import chain


p = PrettyPrinter()


def check_matrix(N, M, matrix):
    heights = list(set(list(chain(*matrix))))
    heights.reverse()

    # неподстриженный газон
    trimmed = [
        [100 for _ in range(M)]
        for _ in range(N)
    ]

    for height in heights:
        # ходим по X
        for x in range(N):
            # берем ту высоту с которой обязаны начать, если идем тут
            #height = matrix[x][0]
            # проверяем можно ли пройтись так, чтобы не испортить
            may_go = reduce(
                lambda a, b: a and b,
                [
                    height >= matrix[x][y]
                    for y in range(M)
                ],
                True
            )

            if may_go:
                # если можем, подстригаем этот маршрут такой высотой
                for y in range(M):
                    trimmed[x][y] = height

        # ходим по Y
        for y in range(M):
            # берем ту высоту с которой обязаны начать, если идем тут
            #height = matrix[0][y]
            # проверяем можно ли пройтись так, чтобы не испортить
            may_go = reduce(
                lambda a, b: a and b,
                [
                    height >= matrix[x][y]
                    for x in range(N)
                ],
                True
            )

            if may_go:
                # если можем, подстригаем этот маршрут такой высотой
                for x in range(N):
                    trimmed[x][y] = height

    #for l in trimmed:
    #    print l

    return trimmed == matrix


if __name__ == '__main__':
    T = int(stdin.readline())

    for index in range(T):
        N, M = map(int, stdin.readline().strip().split())

        matrix = [
            map(int, stdin.readline().strip().split())
            for _ in range(N)
        ]

        print 'Case #%d: %s' % (index + 1, 'YES' if check_matrix(N, M, matrix) else 'NO')

    exit()
