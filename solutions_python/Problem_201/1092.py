#!/usr/bin/env python2
# -*- coding: utf-8 -*-


"""
CodeJam2017 / QR / C. Bathroom Stalls
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
import heapq
import optparse
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')    # pylint: disable=no-member


############
# function #
############
def _solve(N, K):
    queue = [-N, ]
    for k in range(K, 0, -1):
        n = -heapq.heappop(queue)
        if n < 2:
            return 0, 0
        if k == 1:
            if n % 2 == 0:
                return n / 2, n / 2 - 1
            else:
                return n / 2, n / 2
        right = n / 2
        heapq.heappush(queue, -right)
        if n % 2 == 0:
            left = n / 2 - 1
        else:
            left = right
        heapq.heappush(queue, -left)
    return -1, -1


########
# main #
########
def main():
    """
    CodeJam2017 / QR / C. Bathroom Stalls
    """
    for case_num, case in enumerate(sys.stdin):
        if case_num == 0:
            continue
        N, K = case.split()
        ans_min, ans_max = _solve(int(N), int(K))
        print('Case #%d: %d %d' % (case_num, ans_min, ans_max))


if __name__ == '__main__':
    _PARSER = optparse.OptionParser(description='CodeJam2017 / QR / C. Bathroom Stalls')
    _PARSER.add_option('--input', help='input file <default: stdin>', metavar='FILE')
    _PARSER.add_option('--output', help='output file <default: stdout>', metavar='FILE')
    _OPTS, _ = _PARSER.parse_args()
    if _OPTS.input:
        sys.stdin = codecs.open(_OPTS.input, 'rt', encoding='UTF-8')
    if _OPTS.output:
        sys.stdout = codecs.open(_OPTS.output, 'wt', encoding='UTF-8')
    main()
