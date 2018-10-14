import itertools
import time


def rotate(o):

    w, h = map(max, zip(*o))
    for x, y in o:

        yield h - y, x


def reflect(o):

    w, h = map(max, zip(*o))
    for x, y in o:

        yield w - x, y


def generate_ominoes(n):

    ominoes = [frozenset(((0, 0),))]
    viewed = set(ominoes)
    for _ in range(n - 1):

        nominoes = []
        for o in ominoes:

            for x, y in o:

                for dx, dy in ((1, 0), (0, 1)):

                    np = x + dx, y + dy
                    no = o | {np}
                    if no not in viewed:

                        nominoes.append(no)
                        for _ in range(4):

                            viewed.add(no)
                            viewed.add(frozenset(reflect(no)))
                            no = frozenset(rotate(no))

        ominoes = nominoes

    return ominoes


def figures(o):

    for _ in range(4):

        yield o
        yield frozenset(reflect(o))
        o = frozenset(rotate(o))


def can_put(x, y, w, h, f, field):

    for dx, dy in f:

        p = cx, cy = x + dx, y + dy
        if p in field or not (0 <= cx < w) or not (0 <= cy < h):

            return False

    return True


def put(x, y, f, field):

    return field | set(itertools.starmap(lambda dx, dy: (x + dx, y + dy), f))


def yoba(w, h, start, os, field=None):

    field = field or set()
    if set(itertools.product(range(w), range(h))) == field:

        yield True

    if start is not None:

        fs = (start,)

    else:

        fs = os

    for o in fs:

        for f in set(figures(o)):

            for x, y in itertools.product(range(w), range(h)):

                if can_put(x, y, w, h, f, field):

                    nfield = put(x, y, f, field)
                    yield from yoba(w, h, None, os, nfield)


for t in range(int(input())):

    x, r, c = map(int, str.split(input()))
    os = generate_ominoes(x)
    winner = "GABRIEL"
    for o in os:

        try:

            next(yoba(c, r, o, os))

        except StopIteration:

            winner = "RICHARD"

    print(str.format("Case #{}: {}", t + 1, winner))
