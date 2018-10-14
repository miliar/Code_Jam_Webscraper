{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sys.setrecursionlimit(1000000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def nb_flip(pancakes, k):\n",
    "    \n",
    "    #print \"Initial : \" + str(pancakes)\n",
    "    \n",
    "    N = len(pancakes)\n",
    "    flip_pancake = lambda p: \"-\" if p == \"+\" else \"+\"\n",
    "    \n",
    "    all_happy = True\n",
    "    for p in pancakes:\n",
    "        if p != '+':\n",
    "            all_happy = False\n",
    "            break\n",
    "    if(all_happy):\n",
    "        return 0\n",
    "    \n",
    "    if k > len(pancakes):\n",
    "        return -1\n",
    "    \n",
    "    if k == len(pancakes):\n",
    "        all_blanck = True\n",
    "        for p in pancakes:\n",
    "            if p != '-':\n",
    "                all_blanck = False\n",
    "                break\n",
    "        if(all_blanck):\n",
    "            return 1\n",
    "        return -1\n",
    "    \n",
    "    for i, p in enumerate(pancakes[:N-k+1]):\n",
    "        if p == \"-\":\n",
    "            for j in range(i,i+k):\n",
    "                pancakes[j] = flip_pancake(pancakes[j])\n",
    "            #print \"Maintenant : \" + str(pancakes)\n",
    "            recursive_flips = nb_flip(pancakes[i:], k)\n",
    "            if recursive_flips != -1:\n",
    "                return 1 + recursive_flips\n",
    "            else:\n",
    "                return -1\n",
    "    return -1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nb_flip(list(\"-+++++++--\"), 2)"
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
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nb_flip(list(\"-+++++++--\"), 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nb_flip(list(\"++-\"), 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
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
      "Case #7: 2\n",
      "Case #8: IMPOSSIBLE\n",
      "Case #9: 46\n",
      "Case #10: IMPOSSIBLE\n",
      "Case #11: IMPOSSIBLE\n",
      "Case #12: IMPOSSIBLE\n",
      "Case #13: IMPOSSIBLE\n",
      "Case #14: IMPOSSIBLE\n",
      "Case #15: 2\n",
      "Case #16: 50\n",
      "Case #17: 107\n",
      "Case #18: 3\n",
      "Case #19: 55\n",
      "Case #20: IMPOSSIBLE\n",
      "Case #21: 202\n",
      "Case #22: 500\n",
      "Case #23: IMPOSSIBLE\n",
      "Case #24: IMPOSSIBLE\n",
      "Case #25: IMPOSSIBLE\n",
      "Case #26: IMPOSSIBLE\n",
      "Case #27: 50\n",
      "Case #28: IMPOSSIBLE\n",
      "Case #29: 204\n",
      "Case #30: IMPOSSIBLE\n",
      "Case #31: IMPOSSIBLE\n",
      "Case #32: 140\n",
      "Case #33: 91\n",
      "Case #34: 500\n",
      "Case #35: 1\n",
      "Case #36: IMPOSSIBLE\n",
      "Case #37: 1\n",
      "Case #38: IMPOSSIBLE\n",
      "Case #39: IMPOSSIBLE\n",
      "Case #40: 73\n",
      "Case #41: IMPOSSIBLE\n",
      "Case #42: IMPOSSIBLE\n",
      "Case #43: 245\n",
      "Case #44: 17\n",
      "Case #45: IMPOSSIBLE\n",
      "Case #46: IMPOSSIBLE\n",
      "Case #47: IMPOSSIBLE\n",
      "Case #48: IMPOSSIBLE\n",
      "Case #49: IMPOSSIBLE\n",
      "Case #50: 5\n",
      "Case #51: 175\n",
      "Case #52: 0\n",
      "Case #53: IMPOSSIBLE\n",
      "Case #54: IMPOSSIBLE\n",
      "Case #55: 500\n",
      "Case #56: IMPOSSIBLE\n",
      "Case #57: IMPOSSIBLE\n",
      "Case #58: 0\n",
      "Case #59: IMPOSSIBLE\n",
      "Case #60: 93\n",
      "Case #61: 1\n",
      "Case #62: IMPOSSIBLE\n",
      "Case #63: IMPOSSIBLE\n",
      "Case #64: 302\n",
      "Case #65: 106\n",
      "Case #66: 164\n",
      "Case #67: 8\n",
      "Case #68: 333\n",
      "Case #69: IMPOSSIBLE\n",
      "Case #70: IMPOSSIBLE\n",
      "Case #71: IMPOSSIBLE\n",
      "Case #72: 3\n",
      "Case #73: IMPOSSIBLE\n",
      "Case #74: IMPOSSIBLE\n",
      "Case #75: 0\n",
      "Case #76: 202\n",
      "Case #77: 9\n",
      "Case #78: 998\n",
      "Case #79: IMPOSSIBLE\n",
      "Case #80: 27\n",
      "Case #81: 136\n",
      "Case #82: 2\n",
      "Case #83: 137\n",
      "Case #84: 121\n",
      "Case #85: IMPOSSIBLE\n",
      "Case #86: IMPOSSIBLE\n",
      "Case #87: 59\n",
      "Case #88: IMPOSSIBLE\n",
      "Case #89: 191\n",
      "Case #90: 999\n",
      "Case #91: 178\n",
      "Case #92: 1\n",
      "Case #93: 100\n",
      "Case #94: 8\n",
      "Case #95: 33\n",
      "Case #96: IMPOSSIBLE\n",
      "Case #97: IMPOSSIBLE\n",
      "Case #98: IMPOSSIBLE\n",
      "Case #99: IMPOSSIBLE\n",
      "Case #100: IMPOSSIBLE\n"
     ]
    }
   ],
   "source": [
    "#filename = \"A-small-attempt1.in\"\n",
    "#filename = \"sampleA.txt\"\n",
    "filename = \"A-large.in\"\n",
    "f = open('datajam/' + filename, 'r')\n",
    "T = int(f.readline())\n",
    "for i in range(T):\n",
    "    l = f.readline().strip().split(\" \")\n",
    "    pancakes = list(l[0])\n",
    "    K = int(l[1])\n",
    "    answer = nb_flip(pancakes, K)\n",
    "    print \"Case #\" + str(i+1) + \": \" + (str(answer) if answer != -1 else \"IMPOSSIBLE\")"
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
   "display_name": "Python [conda env:py27]",
   "language": "python",
   "name": "conda-env-py27-py"
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
