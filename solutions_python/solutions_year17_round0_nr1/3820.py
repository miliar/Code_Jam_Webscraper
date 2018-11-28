{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['-', '-', '-', '+', '-', '+', '+', '-']\n"
     ]
    }
   ],
   "source": [
    "pk = [x for x in \"---+-++-\"]\n",
    "print(pk)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "pk_len = len(pk)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def flip(p):\n",
    "    if p == \"+\":\n",
    "        return(\"-\")\n",
    "    elif p == \"-\":\n",
    "        return(\"+\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def flipper(pk, K, pos):\n",
    "    for i, p in enumerate(pk):\n",
    "        if pos <= i < pos + K:\n",
    "            pk[i] = flip(p)\n",
    "    return(pk)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "print(pk)\n",
    "print(flipper(pk, 3, 0))\n",
    "print(pk)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(['+', '+', '+', '+', '+', '+', '+', '+'], 3)\n",
      "(['+', '+', '+', '+'], 0)\n",
      "(['+', '+', '-', '+', '+'], 2)\n"
     ]
    }
   ],
   "source": [
    "def solve_p1(pk, K):\n",
    "    n = 0\n",
    "    for i, p in enumerate(pk):\n",
    "        if pk[i] == \"-\" and (len(pk) - i) >= K:\n",
    "            flipper(pk, K, i)\n",
    "            n += 1\n",
    "#            print(pk, n)\n",
    "    return(pk, n)\n",
    "            \n",
    "print(solve_p1([x for x in \"---+-++-\"], 3))\n",
    "print(solve_p1([x for x in \"++++\"], 3))\n",
    "print(solve_p1([x for x in \"-+-+-\"], 4))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "with open('A-small-attempt0.in', 'r') as data:\n",
    "    this_data = data.readlines()[1:]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "results = []\n",
    "\n",
    "for i, row in enumerate(this_data):\n",
    "#    print(row)\n",
    "    pk, K = row.strip().split()\n",
    "    pk = [x for x in pk]\n",
    "    K = int(K)\n",
    "    \n",
    "    if len(pk) >= K:\n",
    "        pk, x = solve_p1(pk, K)\n",
    "        if \"-\" not in pk:\n",
    "            results.append(\"Case #\" + str(i+1) + \": \" + str(x))\n",
    "        else:\n",
    "            results.append(\"Case #\" + str(i+1) + \": IMPOSSIBLE\")\n",
    "    else:\n",
    "        results.append(\"Case #\" + str(i+1) + \": IMPOSSIBLE\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Case #1: 3', 'Case #2: 0', 'Case #3: IMPOSSIBLE', 'Case #4: IMPOSSIBLE', 'Case #5: 0', 'Case #6: 1', 'Case #7: IMPOSSIBLE', 'Case #8: 1', 'Case #9: IMPOSSIBLE', 'Case #10: 3', 'Case #11: IMPOSSIBLE', 'Case #12: IMPOSSIBLE', 'Case #13: IMPOSSIBLE', 'Case #14: IMPOSSIBLE', 'Case #15: IMPOSSIBLE', 'Case #16: IMPOSSIBLE', 'Case #17: IMPOSSIBLE', 'Case #18: 1', 'Case #19: IMPOSSIBLE', 'Case #20: IMPOSSIBLE', 'Case #21: 0', 'Case #22: IMPOSSIBLE', 'Case #23: IMPOSSIBLE', 'Case #24: 3', 'Case #25: IMPOSSIBLE', 'Case #26: 0', 'Case #27: IMPOSSIBLE', 'Case #28: IMPOSSIBLE', 'Case #29: IMPOSSIBLE', 'Case #30: 2', 'Case #31: 1', 'Case #32: 2', 'Case #33: IMPOSSIBLE', 'Case #34: 1', 'Case #35: 2', 'Case #36: IMPOSSIBLE', 'Case #37: IMPOSSIBLE', 'Case #38: IMPOSSIBLE', 'Case #39: IMPOSSIBLE', 'Case #40: IMPOSSIBLE', 'Case #41: 2', 'Case #42: 3', 'Case #43: IMPOSSIBLE', 'Case #44: 0', 'Case #45: 1', 'Case #46: 4', 'Case #47: 3', 'Case #48: 2', 'Case #49: 1', 'Case #50: 0', 'Case #51: IMPOSSIBLE', 'Case #52: 2', 'Case #53: IMPOSSIBLE', 'Case #54: 8', 'Case #55: IMPOSSIBLE', 'Case #56: 2', 'Case #57: 1', 'Case #58: IMPOSSIBLE', 'Case #59: IMPOSSIBLE', 'Case #60: 1', 'Case #61: 2', 'Case #62: IMPOSSIBLE', 'Case #63: IMPOSSIBLE', 'Case #64: 2', 'Case #65: 0', 'Case #66: IMPOSSIBLE', 'Case #67: IMPOSSIBLE', 'Case #68: 1', 'Case #69: IMPOSSIBLE', 'Case #70: IMPOSSIBLE', 'Case #71: 9', 'Case #72: IMPOSSIBLE', 'Case #73: 1', 'Case #74: IMPOSSIBLE', 'Case #75: IMPOSSIBLE', 'Case #76: IMPOSSIBLE', 'Case #77: 1', 'Case #78: IMPOSSIBLE', 'Case #79: 2', 'Case #80: 5', 'Case #81: 2', 'Case #82: IMPOSSIBLE', 'Case #83: 1', 'Case #84: 3', 'Case #85: IMPOSSIBLE', 'Case #86: 2', 'Case #87: IMPOSSIBLE', 'Case #88: 1', 'Case #89: IMPOSSIBLE', 'Case #90: IMPOSSIBLE', 'Case #91: IMPOSSIBLE', 'Case #92: 0', 'Case #93: IMPOSSIBLE', 'Case #94: IMPOSSIBLE', 'Case #95: 3', 'Case #96: 2', 'Case #97: IMPOSSIBLE', 'Case #98: IMPOSSIBLE', 'Case #99: IMPOSSIBLE', 'Case #100: 0']\n"
     ]
    }
   ],
   "source": [
    "print(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "with open('result.out', 'w') as outfile:\n",
    "    outfile.writelines('\\n'.join(results))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "x = [\"1\", \"3\", \"4\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['1', '3', '4']\n"
     ]
    }
   ],
   "source": [
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 4]"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[int(element) for element in x]"
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
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
