{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# imports\n",
    "import numpy as np # http://www.numpy.org/\n",
    "import math # https://docs.python.org/2/library/math.html\n",
    "import itertools as it # https://docs.python.org/2/library/itertools.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "basepath = '/home/epg/halde/codejam/2017/Quals/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "testset = 'B-small-attempt4'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_tidy(N):\n",
    "    return all([str(N)[i] <= str(N)[i+1] for i in xrange(len(str(N))-1)])\n",
    "\n",
    "def prev_digit(d):\n",
    "    if d > 0:\n",
    "        return d-1\n",
    "    return 9\n",
    "    \n",
    "def do_solve(N):\n",
    "    if is_tidy(N):\n",
    "        return N\n",
    "    \n",
    "    res = N    \n",
    "    \n",
    "    while not is_tidy(res):\n",
    "        res -= 1\n",
    "        #s = str(N)\n",
    "        #for i in xrange(len(s)-1):\n",
    "        #    if s[i] > s[i+1]:\n",
    "        #        break\n",
    "\n",
    "        #res = int(s[:i] + str(prev_digit(int(s[i]))) + '9'*(len(s[i+1:])))\n",
    "    \n",
    "    return res"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 129\n",
      "Case #2: 999\n",
      "Case #3: 7\n",
      "Case #4: 899\n",
      "Case #5: 122\n",
      "Case #6: 559\n",
      "Case #7: 899\n",
      "Case #8: 599\n",
      "Case #9: 489\n",
      "Case #10: 199\n",
      "Case #11: 479\n",
      "Case #12: 229\n",
      "Case #13: 299\n",
      "Case #14: 799\n",
      "Case #15: 119\n",
      "Case #16: 299\n",
      "Case #17: 666\n",
      "Case #18: 589\n",
      "Case #19: 388\n",
      "Case #20: 269\n",
      "Case #21: 569\n",
      "Case #22: 199\n",
      "Case #23: 111\n",
      "Case #24: 579\n",
      "Case #25: 459\n",
      "Case #26: 129\n",
      "Case #27: 689\n",
      "Case #28: 799\n",
      "Case #29: 569\n",
      "Case #30: 169\n",
      "Case #31: 599\n",
      "Case #32: 199\n",
      "Case #33: 899\n",
      "Case #34: 699\n",
      "Case #35: 489\n",
      "Case #36: 799\n",
      "Case #37: 599\n",
      "Case #38: 599\n",
      "Case #39: 389\n",
      "Case #40: 799\n",
      "Case #41: 289\n",
      "Case #42: 1\n",
      "Case #43: 699\n",
      "Case #44: 379\n",
      "Case #45: 899\n",
      "Case #46: 889\n",
      "Case #47: 569\n",
      "Case #48: 146\n",
      "Case #49: 799\n",
      "Case #50: 455\n",
      "Case #51: 899\n",
      "Case #52: 899\n",
      "Case #53: 369\n",
      "Case #54: 689\n",
      "Case #55: 39\n",
      "Case #56: 999\n",
      "Case #57: 59\n",
      "Case #58: 579\n",
      "Case #59: 489\n",
      "Case #60: 799\n",
      "Case #61: 57\n",
      "Case #62: 899\n",
      "Case #63: 4\n",
      "Case #64: 799\n",
      "Case #65: 599\n",
      "Case #66: 169\n",
      "Case #67: 49\n",
      "Case #68: 444\n",
      "Case #69: 599\n",
      "Case #70: 199\n",
      "Case #71: 399\n",
      "Case #72: 399\n",
      "Case #73: 118\n",
      "Case #74: 899\n",
      "Case #75: 588\n",
      "Case #76: 69\n",
      "Case #77: 299\n",
      "Case #78: 269\n",
      "Case #79: 799\n",
      "Case #80: 299\n",
      "Case #81: 116\n",
      "Case #82: 679\n",
      "Case #83: 299\n",
      "Case #84: 699\n",
      "Case #85: 589\n",
      "Case #86: 99\n",
      "Case #87: 179\n",
      "Case #88: 112\n",
      "Case #89: 799\n",
      "Case #90: 899\n",
      "Case #91: 339\n",
      "Case #92: 699\n",
      "Case #93: 499\n",
      "Case #94: 899\n",
      "Case #95: 499\n",
      "Case #96: 899\n",
      "Case #97: 126\n",
      "Case #98: 899\n",
      "Case #99: 278\n",
      "Case #100: 599\n"
     ]
    }
   ],
   "source": [
    "with open(basepath + testset + '.in') as fin, open(basepath + testset + '.out', 'w') as fout:\n",
    "    T = int(fin.readline().rstrip('\\r\\n'))\n",
    "    for i in xrange(T):\n",
    "        N, = tuple(map(int, fin.readline().rstrip('\\r\\n').split(' ')))\n",
    "        \n",
    "        sol = do_solve(N)\n",
    "        \n",
    "        sol_string = 'Case #{}: {}'.format(i+1, sol)\n",
    "        fout.write(sol_string + '\\n')\n",
    "        print sol_string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python2",
   "name": "python2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
