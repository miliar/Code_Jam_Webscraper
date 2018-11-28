#!/usr/bin/env python2
# -*- coding: utf-8 -*-


"""
CodeJam2017 / QR / B. Tidy Numbers
__author__ = 'krikit <krikit@naver.com>'
"""


###########
# imports #
###########
from __future__ import unicode_literals
from __future__ import print_function

import codecs
import logging
logging.basicConfig(level=logging.INFO)
import optparse
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')    # pylint: disable=no-member


#############
# functions #
#############
def _is_left_decreasing(left):
    if len(left) <= 1:
        return True
    if left[-2] > left[-1]:
        return False
    return _is_left_decreasing(left[:-1])


def _solve(N):
    for idx in range(len(N)):
        left = N[:idx+1]
        right = N[idx+1:]
        if not _is_left_decreasing(left):
            bound = left.index(left[-2])
            left = N[:bound+1]
            right = N[bound+1:]
            break
    if not right:
        return int(N)
    new_N = left + ('0' * len(right))
    return int(new_N)-1


########
# main #
########
def main():
    """
    CodeJam2017 / QR / B. Tidy Numbers
    """
    for case_num, N in enumerate(sys.stdin):
        if case_num == 0:
            continue
        N = N.strip()
        answer = _solve(N)
        logging.info('%s ==> %d', N, answer)
        print('Case #%d: %d' % (case_num, answer))


if __name__ == '__main__':
    _PARSER = optparse.OptionParser(description='CodeJam2017 / QR / B. Tidy Numbers')
    _PARSER.add_option('--input', help='input file <default: stdin>', metavar='FILE')
    _PARSER.add_option('--output', help='output file <default: stdout>', metavar='FILE')
    _OPTS, _ = _PARSER.parse_args()
    if _OPTS.input:
        sys.stdin = codecs.open(_OPTS.input, 'rt', encoding='UTF-8')
    if _OPTS.output:
        sys.stdout = codecs.open(_OPTS.output, 'wt', encoding='UTF-8')
    main()
