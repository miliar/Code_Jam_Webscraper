{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 62,
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
   "execution_count": 63,
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
   "execution_count": 64,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "testset = 'C-small-2-attempt0'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "def do_solve(N, K):\n",
    "    e = int(math.log(K)/math.log(2))\n",
    "    a = ((N-K)/2**e)\n",
    "    z = a/2\n",
    "    y = a - z\n",
    "    \n",
    "    return y, z"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 1 0\n",
      "Case #2: 1 0\n",
      "Case #3: 1 1\n",
      "Case #4: 0 0\n",
      "Case #5: 500 499\n",
      "Case #6: 1 0\n",
      "Case #7: 0 0\n",
      "Case #8: 1 0\n",
      "Case #9: 250000 249999\n",
      "Case #10: 0 0\n",
      "Case #11: 1 0\n",
      "Case #12: 1 1\n",
      "Case #13: 0 0\n",
      "Case #14: 0 0\n",
      "Case #15: 0 0\n",
      "Case #16: 0 0\n",
      "Case #17: 2 1\n",
      "Case #18: 0 0\n",
      "Case #19: 0 0\n",
      "Case #20: 0 0\n",
      "Case #21: 3906 3905\n",
      "Case #22: 1 0\n",
      "Case #23: 0 0\n",
      "Case #24: 0 0\n",
      "Case #25: 1 0\n",
      "Case #26: 1 0\n",
      "Case #27: 1 1\n",
      "Case #28: 1 0\n",
      "Case #29: 0 0\n",
      "Case #30: 249999 249999\n",
      "Case #31: 1 1\n",
      "Case #32: 0 0\n",
      "Case #33: 0 0\n",
      "Case #34: 7812 7811\n",
      "Case #35: 1 0\n",
      "Case #36: 0 0\n",
      "Case #37: 0 0\n",
      "Case #38: 0 0\n",
      "Case #39: 0 0\n",
      "Case #40: 3 2\n",
      "Case #41: 0 0\n",
      "Case #42: 0 0\n",
      "Case #43: 0 0\n",
      "Case #44: 1953 1952\n",
      "Case #45: 1 1\n",
      "Case #46: 0 0\n",
      "Case #47: 1 0\n",
      "Case #48: 1 0\n",
      "Case #49: 1 0\n",
      "Case #50: 0 0\n",
      "Case #51: 0 0\n",
      "Case #52: 1 1\n",
      "Case #53: 1 0\n",
      "Case #54: 0 0\n",
      "Case #55: 0 0\n",
      "Case #56: 1 0\n",
      "Case #57: 0 0\n",
      "Case #58: 3 2\n",
      "Case #59: 1 0\n",
      "Case #60: 0 0\n",
      "Case #61: 7812 7811\n",
      "Case #62: 0 0\n",
      "Case #63: 1 1\n",
      "Case #64: 0 0\n",
      "Case #65: 0 0\n",
      "Case #66: 3 2\n",
      "Case #67: 0 0\n",
      "Case #68: 0 0\n",
      "Case #69: 0 0\n",
      "Case #70: 0 0\n",
      "Case #71: 2 2\n",
      "Case #72: 0 0\n",
      "Case #73: 1 1\n",
      "Case #74: 3906 3905\n",
      "Case #75: 499999 499999\n",
      "Case #76: 1 1\n",
      "Case #77: 0 0\n",
      "Case #78: 1 0\n",
      "Case #79: 1 0\n",
      "Case #80: 0 0\n",
      "Case #81: 0 0\n",
      "Case #82: 1 0\n",
      "Case #83: 0 0\n",
      "Case #84: 0 0\n",
      "Case #85: 1 1\n",
      "Case #86: 0 0\n",
      "Case #87: 0 0\n",
      "Case #88: 125000 124999\n",
      "Case #89: 0 0\n",
      "Case #90: 0 0\n",
      "Case #91: 250000 249999\n",
      "Case #92: 1 0\n",
      "Case #93: 1 1\n",
      "Case #94: 0 0\n",
      "Case #95: 0 0\n",
      "Case #96: 500000 499999\n",
      "Case #97: 1 0\n",
      "Case #98: 0 0\n",
      "Case #99: 3905 3905\n",
      "Case #100: 0 0\n"
     ]
    }
   ],
   "source": [
    "with open(basepath + testset + '.in') as fin, open(basepath + testset + '.out', 'w') as fout:\n",
    "    T = int(fin.readline().rstrip('\\r\\n'))\n",
    "    for i in xrange(T):\n",
    "        N, K = tuple(map(int, fin.readline().rstrip('\\r\\n').split(' ')))\n",
    "        \n",
    "        sol = do_solve(N, K)\n",
    "        \n",
    "        sol_string = 'Case #{}: {} {}'.format(i+1, *sol)\n",
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
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
