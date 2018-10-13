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
   "execution_count": 52,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def tidy(s):\n",
    "    \n",
    "    s = str(s)\n",
    "    #print()\n",
    "    for i in range(len(s)-1,0,-1):\n",
    "        if s[i] < s[i-1]:\n",
    "            x = int(s) - int(s[i:]) -1\n",
    "            s = str(x)\n",
    "        #print(i,x)\n",
    "    #print(s)\n",
    "    return s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "129\n",
      "999\n",
      "7\n",
      "99999999999999999\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'99999999999999999'"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tidy(132)\n",
    "tidy(1000)\n",
    "tidy(7)\n",
    "tidy(111111111111111110)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "\n",
    "f = open('B-large.in','r')\n",
    "#f = open('A-large.in','r')\n",
    "sol = open('sol_b0','w')\n",
    "t = int(f.readline()) # int(input())  # read a line with a single integer\n",
    "for i in range(1, t + 1):\n",
    "    s = int(f.readline()) #.split(' ') # input().split(\" \")\n",
    "    #S = [(1 if s == '+' else -1) for s in L[0]]\n",
    "    #K = int(L[1]     )\n",
    "    #print(S,K)\n",
    "    #print(\"Case #{}: {}\".format(i, pancake(S,K)))\n",
    "    sol.writelines(\"Case #{}: {}\\n\".format(i, tidy(s)))\n",
    "    \n",
    "sol.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
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
      "Case #4: 88\n",
      "Case #5: 39\n",
      "Case #6: IMPOSSIBLE\n",
      "Case #7: 500\n",
      "Case #8: 998\n",
      "Case #9: 170\n",
      "Case #10: IMPOSSIBLE\n",
      "Case #11: IMPOSSIBLE\n",
      "Case #12: IMPOSSIBLE\n",
      "Case #13: 190\n",
      "Case #14: IMPOSSIBLE\n",
      "Case #15: 67\n",
      "Case #16: IMPOSSIBLE\n",
      "Case #17: IMPOSSIBLE\n",
      "Case #18: IMPOSSIBLE\n",
      "Case #19: IMPOSSIBLE\n",
      "Case #20: IMPOSSIBLE\n",
      "Case #21: 111\n",
      "Case #22: 216\n",
      "Case #23: IMPOSSIBLE\n",
      "Case #24: 35\n",
      "Case #25: IMPOSSIBLE\n",
      "Case #26: IMPOSSIBLE\n",
      "Case #27: 69\n",
      "Case #28: 50\n",
      "Case #29: 115\n",
      "Case #30: IMPOSSIBLE\n",
      "Case #31: IMPOSSIBLE\n",
      "Case #32: IMPOSSIBLE\n",
      "Case #33: 56\n",
      "Case #34: 0\n",
      "Case #35: 45\n",
      "Case #36: IMPOSSIBLE\n",
      "Case #37: IMPOSSIBLE\n",
      "Case #38: 7\n",
      "Case #39: IMPOSSIBLE\n",
      "Case #40: 9\n",
      "Case #41: IMPOSSIBLE\n",
      "Case #42: 2\n",
      "Case #43: IMPOSSIBLE\n",
      "Case #44: IMPOSSIBLE\n",
      "Case #45: 5\n",
      "Case #46: 43\n",
      "Case #47: 333\n",
      "Case #48: IMPOSSIBLE\n",
      "Case #49: IMPOSSIBLE\n",
      "Case #50: IMPOSSIBLE\n",
      "Case #51: 9\n",
      "Case #52: IMPOSSIBLE\n",
      "Case #53: 3\n",
      "Case #54: 302\n",
      "Case #55: IMPOSSIBLE\n",
      "Case #56: 8\n",
      "Case #57: IMPOSSIBLE\n",
      "Case #58: 28\n",
      "Case #59: IMPOSSIBLE\n",
      "Case #60: 500\n",
      "Case #61: 3\n",
      "Case #62: 6\n",
      "Case #63: 70\n",
      "Case #64: IMPOSSIBLE\n",
      "Case #65: IMPOSSIBLE\n",
      "Case #66: IMPOSSIBLE\n",
      "Case #67: IMPOSSIBLE\n",
      "Case #68: 76\n",
      "Case #69: 34\n",
      "Case #70: 0\n",
      "Case #71: 78\n",
      "Case #72: IMPOSSIBLE\n",
      "Case #73: IMPOSSIBLE\n",
      "Case #74: IMPOSSIBLE\n",
      "Case #75: IMPOSSIBLE\n",
      "Case #76: 26\n",
      "Case #77: IMPOSSIBLE\n",
      "Case #78: IMPOSSIBLE\n",
      "Case #79: IMPOSSIBLE\n",
      "Case #80: IMPOSSIBLE\n",
      "Case #81: IMPOSSIBLE\n",
      "Case #82: 75\n",
      "Case #83: 500\n",
      "Case #84: IMPOSSIBLE\n",
      "Case #85: 1\n",
      "Case #86: IMPOSSIBLE\n",
      "Case #87: 1\n",
      "Case #88: IMPOSSIBLE\n",
      "Case #89: 1\n",
      "Case #90: IMPOSSIBLE\n",
      "Case #91: IMPOSSIBLE\n",
      "Case #92: 8\n",
      "Case #93: 0\n",
      "Case #94: 34\n",
      "Case #95: IMPOSSIBLE\n",
      "Case #96: 999\n",
      "Case #97: 341\n",
      "Case #98: 1\n",
      "Case #99: 2\n",
      "Case #100: 3\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "\n",
    "f = open('a.in','r')\n",
    "f = open('A-large.in','r')\n",
    "sol = open('sol_Large','w')\n",
    "t = int(f.readline()) # int(input())  # read a line with a single integer\n",
    "for i in range(1, t + 1):\n",
    "    L = f.readline().split(' ') # input().split(\" \")\n",
    "    S = [(1 if s == '+' else -1) for s in L[0]]\n",
    "    K = int(L[1]     )\n",
    "    #print(S,K)\n",
    "    print(\"Case #{}: {}\".format(i, pancake(S,K)))\n",
    "    sol.writelines(\"Case #{}: {}\\n\".format(i, pancake(S,K)))\n",
    "    \n",
    "sol.close()"
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
