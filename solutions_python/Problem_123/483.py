#!/usr/bin/python -tt
# encoding: utf-8

import sys


def main():
    """Read in the specified file and print out the expected output."""
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print 'usage: ./Osmos.py file'
        sys.exit(1)
    with open(filename, 'rU') as file_handle:
        casenum = int(file_handle.readline())
        for case in range(1, casenum + 1):
            print handle_case(case, [file_handle.readline() for x in range(2)])


def handle_case(case, lines, **args):
    """Return a string containing the expected output given a single case.

    Handles the case supplied through the given case and lines and returns a
    string containing the expected output of the given input. The **args may be
    used to contain any additional input variables that may have been
    preprocessed.

    Args:
        case: Number specifying the current case number
        lines: List of input lines relevant to the case
        **args: Additional arguments (e.g. preprocessed input)

    Returns:
        A string of the expected output of the corresponding test case.
    """

    A, N = [int(x) for x in lines[0].split()]
    motes = sorted(int(x) for x in lines[1].split())
    a_curr = A
    op_num = 0
    # for i, m_curr in enumerate(motes):
    #     if a_curr > m_curr:
    #         a_curr += m_curr
    #     else:
    #         m_left = len(motes) - i
    #         m_next = mote_max_inc(a_curr, 1)
    #         if m_curr < m_next:
    #             a_curr = m_next + m_curr
    #             op_num += 1
    #         else:
    #             m_max = mote_max_inc(a_curr, m_left)
    #             if m_curr < m_max:
    #                 step = 1
    #                 new_a = mote_max_inc(a_curr, step)
    #                 op_num += 1
    #                 while new_a <= m_curr:
    #                     step += 1
    #                     new_a = mote_max_inc(a_curr, step)
    #                     op_num += 1

    #                 a_curr = new_a + m_curr
    #             else:
    #                 op_num += m_left
    #                 break

    result = num_op_solve(motes, a_curr, op_num)
    return 'Case #%d: %s' % (case, result)


def num_op_solve(motes, a_curr, op_num):
    """Return the minimum number of operations to make the motes solvable

    Use dynamic programming to get the number of operations necessary.

    Args:
        motes: List of motes
        a_curr: Int size of Armin's mote
        op_num: Int operations accomplished prior
    """

    m_curr = motes[0]
    curr_op_num = 0

    # special case -- can't increase mote size of 1
    if a_curr == 1:
        return len(motes)

    # increase a_curr until a_curr > m_curr -- add operations
    elif a_curr <= m_curr:
        step = 1
        new_a = mote_max_inc(a_curr, step)
        curr_op_num += 1
        while new_a <= m_curr:
            step += 1
            new_a = mote_max_inc(a_curr, step)
            curr_op_num += 1

        a_curr = new_a + m_curr

    # else add m_curr as usual
    elif a_curr > m_curr:
        a_curr += m_curr

    if len(motes) == 1:
        return min(curr_op_num, 1)

    return (min(len(motes),
                num_op_solve(motes[1:], a_curr, op_num) + curr_op_num)
            )


def mote_max_inc(mote, n):
    """Return an int showing the size of a mote after n steps of max increases

    Args:
        mote: Int initial size
        n: Int number of times mote will increase
    """

    return ((2 ** n) * mote) - ((2 ** n) - 1)


if __name__ == '__main__':
    main()
