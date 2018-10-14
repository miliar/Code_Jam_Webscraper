{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 3\n",
      "Case #2: 0\n",
      "Case #3: IMPOSSIBLE\n",
      "Case #4: IMPOSSIBLE\n",
      "Case #5: IMPOSSIBLE\n",
      "Case #6: IMPOSSIBLE\n",
      "Case #7: 1\n",
      "Case #8: 1\n",
      "Case #9: 2\n",
      "Case #10: IMPOSSIBLE\n",
      "Case #11: IMPOSSIBLE\n",
      "Case #12: IMPOSSIBLE\n",
      "Case #13: IMPOSSIBLE\n",
      "Case #14: 1\n",
      "Case #15: IMPOSSIBLE\n",
      "Case #16: IMPOSSIBLE\n",
      "Case #17: 1\n",
      "Case #18: 0\n",
      "Case #19: 2\n",
      "Case #20: IMPOSSIBLE\n",
      "Case #21: 4\n",
      "Case #22: 3\n",
      "Case #23: 3\n",
      "Case #24: 1\n",
      "Case #25: 1\n",
      "Case #26: 2\n",
      "Case #27: IMPOSSIBLE\n",
      "Case #28: IMPOSSIBLE\n",
      "Case #29: IMPOSSIBLE\n",
      "Case #30: IMPOSSIBLE\n",
      "Case #31: IMPOSSIBLE\n",
      "Case #32: 3\n",
      "Case #33: IMPOSSIBLE\n",
      "Case #34: IMPOSSIBLE\n",
      "Case #35: IMPOSSIBLE\n",
      "Case #36: IMPOSSIBLE\n",
      "Case #37: IMPOSSIBLE\n",
      "Case #38: IMPOSSIBLE\n",
      "Case #39: IMPOSSIBLE\n",
      "Case #40: IMPOSSIBLE\n",
      "Case #41: 8\n",
      "Case #42: IMPOSSIBLE\n",
      "Case #43: 5\n",
      "Case #44: IMPOSSIBLE\n",
      "Case #45: IMPOSSIBLE\n",
      "Case #46: IMPOSSIBLE\n",
      "Case #47: IMPOSSIBLE\n",
      "Case #48: 2\n",
      "Case #49: 1\n",
      "Case #50: 0\n",
      "Case #51: 1\n",
      "Case #52: IMPOSSIBLE\n",
      "Case #53: IMPOSSIBLE\n",
      "Case #54: 4\n",
      "Case #55: 2\n",
      "Case #56: 2\n",
      "Case #57: IMPOSSIBLE\n",
      "Case #58: IMPOSSIBLE\n",
      "Case #59: 9\n",
      "Case #60: IMPOSSIBLE\n",
      "Case #61: IMPOSSIBLE\n",
      "Case #62: IMPOSSIBLE\n",
      "Case #63: IMPOSSIBLE\n",
      "Case #64: 2\n",
      "Case #65: 0\n",
      "Case #66: IMPOSSIBLE\n",
      "Case #67: IMPOSSIBLE\n",
      "Case #68: IMPOSSIBLE\n",
      "Case #69: 1\n",
      "Case #70: 0\n",
      "Case #71: 2\n",
      "Case #72: IMPOSSIBLE\n",
      "Case #73: 1\n",
      "Case #74: IMPOSSIBLE\n",
      "Case #75: IMPOSSIBLE\n",
      "Case #76: 4\n",
      "Case #77: IMPOSSIBLE\n",
      "Case #78: 2\n",
      "Case #79: IMPOSSIBLE\n",
      "Case #80: 0\n",
      "Case #81: 3\n",
      "Case #82: IMPOSSIBLE\n",
      "Case #83: 1\n",
      "Case #84: IMPOSSIBLE\n",
      "Case #85: 3\n",
      "Case #86: IMPOSSIBLE\n",
      "Case #87: 1\n",
      "Case #88: 1\n",
      "Case #89: 1\n",
      "Case #90: 0\n",
      "Case #91: IMPOSSIBLE\n",
      "Case #92: 1\n",
      "Case #93: IMPOSSIBLE\n",
      "Case #94: 1\n",
      "Case #95: 0\n",
      "Case #96: 0\n",
      "Case #97: IMPOSSIBLE\n",
      "Case #98: 3\n",
      "Case #99: IMPOSSIBLE\n",
      "Case #100: 1\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "\n",
    "f = open('a.in','r')\n",
    "f = open('A-small-attempt0.in','r')\n",
    "sol = open('solA','w')\n",
    "t = int(f.readline()) # int(input())  # read a line with a single integer\n",
    "for i in range(1, t + 1):\n",
    "    L = f.readline().split(' ') # input().split(\" \")\n",
    "    S = [(1 if s == '+' else -1) for s in L[0]]\n",
    "    K = int(L[1]     )\n",
    "    #print(S,K)\n",
    "    print(\"Case #{}: {}\".format(i, pancake(S,K)))\n",
    "    sol.writelines(\"Case #{}: {}\".format(i, pancake(S,K)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def pancake(S,K):\n",
    "    \n",
    "    S = np.array(S)\n",
    "    c = 0\n",
    "    if sum(S) == len(S):\n",
    "        return c\n",
    "    for i in range(S.shape[0] - K +1 ):\n",
    "        if S[i] == -1:\n",
    "            S[i:i+K] = -S[i:i+K]\n",
    "            c += 1\n",
    "            if sum(S) == len(S):\n",
    "                return c\n",
    "    return \"IMPOSSIBLE\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pancake([1,-1,1,-1,-1,1,-1], 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'IMPOSSIBLE'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pancake([-1,1,1], 3)"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  },
  "nav_menu": {},
  "toc": {
   "navigate_menu": true,
   "number_sections": true,
   "sideBar": true,
   "threshold": 6,
   "toc_cell": false,
   "toc_section_display": "block",
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
