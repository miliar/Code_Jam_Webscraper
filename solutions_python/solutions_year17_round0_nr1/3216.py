#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from copy import deepcopy


def flip(case, k, start):
    """Flip of case k things starting at start."""
    for i in range(start, start + k):
        case[i] = (case[i] + 1) % 2
    return case


def check(situation, k, solution):
    for start, val in enumerate(solution):
        if val:
            situation = flip(situation, k, start)
    return all(situation)


def create_vectors(n, k):
    """
    Create flipping vectors.

    Examples
    --------
    >>> create_vectors(4, 2)
    array([[1, 0, 0],
           [1, 1, 0],
           [0, 1, 1],
           [0, 0, 1]])

    """
    vectors = []
    for i in range(0, n - k + 1):
        v = np.zeros(n, dtype=np.int)
        for j in range(k):
            v[i + j] = 1
        vectors.append(v)
    return np.array(vectors).transpose()


def swap_rows(a, b, row1, row2):
    """
    Swap row1 and row2 in the matrix a and result vector b.

    Examples
    --------
    >>> a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> b = [1, 2, 3]
    >>> swap_rows(a, b, 1, 2)
    ([[1, 2, 3], [7, 8, 9], [4, 5, 6]], [1, 3, 2])
    """
    tmp = deepcopy(a[row1])
    a[row1] = deepcopy(a[row2])
    a[row2] = tmp

    tmp = b[row1]
    b[row1] = b[row2]
    b[row2] = tmp
    return a, b


def add_vectors_z2(a, b):
    result = []
    if len(a) != len(b):
        print("Beide Vektoren müssen gleich lang sein!")
        return False
    for pos in range(0, len(a)):
        result.append((a[pos] + b[pos]) % 2)
    return result


def gauss_z2(a, b, verbose=False):
    """
    Solve system of equations in Z/2Z.

    Parameters
    ----------
    a : matrix
        coefficients
    b : result vector

    Returns
    -------


    bring a in the form
    1xxxxxxx
    01xxxxxx
    001xxxxx
    0001xxxx
    00001xxx
    000001xx
    0000001x
    00000001
    where x is arbitrary
    """

    if verbose:
        print("Started gauss")
        print("Erweiterte Koeffizientenmatrix:")
        for zeilen_nr, zeile in enumerate(a):
            print("%s | %i " % (str(zeile), b[zeilen_nr]))

    for column in range(0, len(a[0])):
        if verbose:
            print("Erweiterte Koeffizientenmatrix (Spalte %i):" % column)
            for zeilen_nr, zeile in enumerate(a):
                print("%s | %i " % (str(zeile), b[zeilen_nr]))
        # column 'column' has to have a 1 in row 'act_row'
        act_row = column
        if a[act_row][column] == 0:
            could_get1 = False
            for row_i in range(act_row + 1, len(a)):
                if a[row_i][column] == 1:
                    a, b = swap_rows(a, b, row_i, act_row)
                    could_get1 = True
                    break
            if not could_get1:
                # Impossible
                return "IMPOSSIBLE"

        # All following columns have to have a 0 in row 'column'
        for row in range(column + 1, len(a)):
            if a[row][column] == 0:
                continue
            else:
                # Die Zeile row hat in der Spalte column keine 0, also hat sie
                # dort eine 1. Es sollte aber eine 0 sein
                # Da die Zeile act_row garantiert auch eine 1 hat, kann man die
                # Zeilen addieren (wir sind im Z2) um eine 0 zu bekommen.
                # for column_i in range(0, len(a[0])):
                a[row] = add_vectors_z2(a[row], a[act_row])
                b[row] = (b[row] + b[act_row]) % 2
    if verbose:
        print("Now (a,b) is in the row-echelon form:")
        for row, el in enumerate(a):
            print(str(el) + str("\t") + str(b[row]))

    # Berechne das Ergebnis.
    # Fange mit dem Koeffizienten des letzen Vektors an.
    results = [None for i in range(0, len(a[0]))]
    for row in range(len(a[0]) - 1, -1, -1):
        should_be = b[row]
        for column in range(row + 1, len(a[0])):
            if a[row][column] == 1:
                should_be = (results[column] + should_be) % 2
        results[row] = should_be

    if verbose:
        print("Results: " + str(results))
        for key, i in enumerate(results):
            print("x_" + str(key + 1) + ": " + str(i))
    return results


def solve(case):
    """Solve problem A."""
    state, k = case.split(" ")
    state = [s == '+' for s in state]
    state_w = [int(s == 0) for s in state]  # inverse it
    n = len(state)
    k = int(k)
    vectors = create_vectors(n, k)
    solution = gauss_z2(vectors, state_w, verbose=False)

    if solution == "IMPOSSIBLE" or not check(state, k, solution):
        return "IMPOSSIBLE"
    else:
        return sum(solution)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    testcases = input()

    for caseNr in range(1, testcases + 1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
