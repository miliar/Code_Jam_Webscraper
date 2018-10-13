#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tidy numbers."""


def is_tidy(n):
    """
    Check if n is tidy.

    Examples
    --------
    >>> is_tidy(7)
    True
    >>> is_tidy(1234)
    True
    >>> is_tidy(1230)
    False
    """
    n = str(n)
    for i, j in zip(n, n[1:]):
        if int(i) > int(j):
            return False
    return True


def find_tindy_before(n):
    """
    Find the biggest tidy number in 1...n.

    Examples
    --------
    >>> find_tindy_before(132)
    129
    >>> find_tindy_before(1000)
    999
    >>> find_tindy_before(7)
    7
    >>> find_tindy_before(111111111111111110)
    99999999999999999
    """
    last_tidy = n
    while not is_tidy(last_tidy):
        # Find where the problem is
        last_tidy = list(str(last_tidy))
        pos = 1
        for i, j in zip(last_tidy, last_tidy[1:]):
            if int(i) > int(j):
                break
            pos += 1
        # Set all following to 0
        for i in range(pos, len(last_tidy)):
            last_tidy[i] = "0"
        last_tidy = int("".join(last_tidy)) - 1
    return last_tidy


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    testcases = input()
    for caseNr in range(1, testcases + 1):
        n = input()
        print("Case #%i: %s" % (caseNr, find_tindy_before(n)))
