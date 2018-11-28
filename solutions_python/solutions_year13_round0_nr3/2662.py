import logging

logging.basicConfig(level=logging.DEBUG)


def readfile(filename='c.txt'):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    lines.pop(0)

    return lines


def gen_palindromes(start, end):
    for i in xrange(start, end + 1):
        s = str(i)
        if is_palindrome(s):
            yield i


def gen_squares(n):
    i = 1
    sq = i * i
    yield sq
    while sq <= n:
        i += 1
        sq = i * i
        if sq <= n:
            yield sq


def is_palindrome(s):
    return s == s[::-1]


def solve(problem, squares):
    solutions = [i
                 for i in gen_palindromes(problem[0], problem[1])
                 if i in squares and is_palindrome(str(getnum(squares, i)))]
    logging.debug('solutions %s', solutions)
    return len(solutions)


problems = [map(int, line.split()) for line in readfile('c.small.in.txt')]

squares = list(gen_squares(1000))


def getnum(squares, square):
    return squares.index(square) + 1


print (squares.index(121) + 1) ** 2

lines = [(i + 1, solve(problem, squares))
         for i, problem in enumerate(problems)]

with open('c.small.out.txt', 'wb') as f:
    f.writelines(['Case #{}: {}\n'.format(i, sol)
                  for i, sol in lines])
