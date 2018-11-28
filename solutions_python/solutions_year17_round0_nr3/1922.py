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
   "execution_count": 97,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "class l_sort():\n",
    "    \n",
    "    def __init__(self):\n",
    "        self.L = []\n",
    "        \n",
    "    def add(self,k):\n",
    "        if k > 0:\n",
    "            self.L.append(k)\n",
    "        #print(self.L)\n",
    "    def get_max(self):\n",
    "        #print(self.L)\n",
    "        return max(self.L)\n",
    "    \n",
    "    def pop(self,k):\n",
    "        \n",
    "        self.L.remove(k)\n",
    "        \n",
    "    def enter_bath(self):\n",
    "        \n",
    "        k = self.get_max()\n",
    "        a,b = self.enter(k)\n",
    "        self.add(a)\n",
    "        self.add(b)\n",
    "        self.pop(k)\n",
    "        return a,b\n",
    "    \n",
    "    def enter(self,k):\n",
    "        \n",
    "        k=k-1\n",
    "        a = int(np.ceil(k/2))\n",
    "        b = int(np.floor(k/2))\n",
    "        #print(a,b)\n",
    "        return b,a\n",
    "    \n",
    "    def solve(self,n,k):\n",
    "        \n",
    "        self.add(n)\n",
    "        for i in range(k):\n",
    "            #print(i)\n",
    "            res = self.enter_bath()\n",
    "        return res[1], res[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 1)"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ll = l_sort()\n",
    "ll.solve(6,2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: (1, 0)\n",
      "Case #2: (1, 0)\n",
      "Case #3: (1, 1)\n",
      "Case #4: (0, 0)\n",
      "Case #5: (500, 499)\n",
      "Case #6: (1, 1)\n",
      "Case #7: (1, 0)\n",
      "Case #8: (0, 0)\n",
      "Case #9: (0, 0)\n",
      "Case #10: (0, 0)\n",
      "Case #11: (0, 0)\n",
      "Case #12: (0, 0)\n",
      "Case #13: (1, 1)\n",
      "Case #14: (0, 0)\n",
      "Case #15: (1, 0)\n",
      "Case #16: (0, 0)\n",
      "Case #17: (0, 0)\n",
      "Case #18: (0, 0)\n",
      "Case #19: (1, 0)\n",
      "Case #20: (3, 2)\n",
      "Case #21: (0, 0)\n",
      "Case #22: (0, 0)\n",
      "Case #23: (2, 1)\n",
      "Case #24: (3, 2)\n",
      "Case #25: (0, 0)\n",
      "Case #26: (0, 0)\n",
      "Case #27: (0, 0)\n",
      "Case #28: (3, 3)\n",
      "Case #29: (1, 0)\n",
      "Case #30: (1, 0)\n",
      "Case #31: (0, 0)\n",
      "Case #32: (249, 249)\n",
      "Case #33: (1, 0)\n",
      "Case #34: (1, 0)\n",
      "Case #35: (0, 0)\n",
      "Case #36: (0, 0)\n",
      "Case #37: (0, 0)\n",
      "Case #38: (1, 0)\n",
      "Case #39: (0, 0)\n",
      "Case #40: (0, 0)\n",
      "Case #41: (0, 0)\n",
      "Case #42: (0, 0)\n",
      "Case #43: (0, 0)\n",
      "Case #44: (0, 0)\n",
      "Case #45: (1, 1)\n",
      "Case #46: (0, 0)\n",
      "Case #47: (1, 1)\n",
      "Case #48: (0, 0)\n",
      "Case #49: (1, 1)\n",
      "Case #50: (250, 249)\n",
      "Case #51: (0, 0)\n",
      "Case #52: (0, 0)\n",
      "Case #53: (0, 0)\n",
      "Case #54: (3, 2)\n",
      "Case #55: (0, 0)\n",
      "Case #56: (0, 0)\n",
      "Case #57: (1, 0)\n",
      "Case #58: (7, 6)\n",
      "Case #59: (3, 3)\n",
      "Case #60: (0, 0)\n",
      "Case #61: (0, 0)\n",
      "Case #62: (1, 0)\n",
      "Case #63: (0, 0)\n",
      "Case #64: (0, 0)\n",
      "Case #65: (250, 249)\n",
      "Case #66: (499, 499)\n",
      "Case #67: (0, 0)\n",
      "Case #68: (0, 0)\n",
      "Case #69: (0, 0)\n",
      "Case #70: (1, 1)\n",
      "Case #71: (3, 3)\n",
      "Case #72: (1, 1)\n",
      "Case #73: (1, 0)\n",
      "Case #74: (0, 0)\n",
      "Case #75: (1, 1)\n",
      "Case #76: (125, 124)\n",
      "Case #77: (2, 2)\n",
      "Case #78: (3, 2)\n",
      "Case #79: (0, 0)\n",
      "Case #80: (1, 0)\n",
      "Case #81: (1, 1)\n",
      "Case #82: (1, 0)\n",
      "Case #83: (0, 0)\n",
      "Case #84: (1, 0)\n",
      "Case #85: (0, 0)\n",
      "Case #86: (1, 0)\n",
      "Case #87: (0, 0)\n",
      "Case #88: (3, 3)\n",
      "Case #89: (0, 0)\n",
      "Case #90: (7, 6)\n",
      "Case #91: (0, 0)\n",
      "Case #92: (1, 0)\n",
      "Case #93: (0, 0)\n",
      "Case #94: (1, 0)\n",
      "Case #95: (0, 0)\n",
      "Case #96: (0, 0)\n",
      "Case #97: (0, 0)\n",
      "Case #98: (1, 1)\n",
      "Case #99: (0, 0)\n",
      "Case #100: (0, 0)\n"
     ]
    }
   ],
   "source": [
    "\n",
    "f = open('C-small-1-attempt1.in','r')\n",
    "#f = open('A-large.in','r')\n",
    "sol = open('Sol_c1.out','w')\n",
    "t = int(f.readline()) # read a line with a single integer\n",
    "\n",
    "for i in range(1, t + 1):\n",
    "    n,k = [int(x) for x in f.readline().split(' ')]\n",
    "    ll = l_sort()\n",
    "    res = ll.solve(n,k)\n",
    "    print(\"Case #{}: {}\".format(i, res))\n",
    "    sol.writelines(\"Case #{}: {} {}\\n\".format(i,res[0],res[1] ))\n",
    "    \n",
    "sol.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "4 2\n",
    "5 2\n",
    "6 2\n",
    "1000 1000\n",
    "1000 1"
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
   "execution_count": 56,
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
    "sol = open('Sol.out','w')\n",
    "t = int(f.readline()) # read a line with a single integer\n",
    "for i in range(1, t + 1):\n",
    "    s = int(f.readline()) \n",
    "    #print(\"Case #{}: {}\".format(i, pancake(S,K)))\n",
    "    sol.writelines(\"Case #{}: {}\\n\".format(i, tidy(s)))\n",
    "    \n",
    "sol.close()\n",
    "\n",
    "f = open('a.in','r')\n",
    "f = open('A-large.in','r')\n",
    "sol = open('Sol_A.out','w')\n",
    "t = int(f.readline()) # int(input())  # read a line with a single integer\n",
    "for i in range(1, t + 1):\n",
    "    L = f.readline().split(' ') # input().split(\" \")\n",
    "    S = [(1 if s == '+' else -1) for s in L[0]]\n",
    "    K = int(L[1])\n",
    "    print(\"Case #{}: {}\".format(i, pancake(S,K)))\n",
    "    sol.writelines(\"Case #{}: {}\\n\".format(i, pancake(S,K)))\n",
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
   "source": []
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
