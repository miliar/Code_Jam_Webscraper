{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1000000000000000001L"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max(1000000000000000000, 1000000000000000001)"
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
      "Wall time: 26.9 s\n"
     ]
    }
   ],
   "source": [
    "%%time\n",
    "from copy import copy\n",
    "best = 0\n",
    "def join_number(N):\n",
    "    return int(''.join([str(x) for x in N]))\n",
    "\n",
    "def solve(N):\n",
    "    def recurse(digit, val, carry=0):   \n",
    "        global best\n",
    "        if digit == 0:\n",
    "            cur = min(original[digit] - carry, val)\n",
    "            number[digit] = cur\n",
    "            if cur < 0:\n",
    "                return\n",
    "            best = max(best, join_number(number))\n",
    "            return\n",
    "        \n",
    "        cur = min(original[digit] - carry, val)\n",
    "        number[digit] = cur\n",
    "        if cur >=0:\n",
    "            recurse(digit-1, cur)\n",
    "        \n",
    "        cur = min(9, val)\n",
    "        number[digit] = cur\n",
    "        recurse(digit-1, cur, 1)\n",
    "    \n",
    "    number = [int(x) for x in str(N)]\n",
    "    original = copy(number)\n",
    "    \n",
    "    \n",
    "    \n",
    "   \n",
    "    recurse(len(number)-1, 9)\n",
    "    \n",
    "    return best\n",
    "\n",
    "infile = open('B-large.in')\n",
    "outfile = open('out.txt', 'w')\n",
    "\n",
    "T = int(infile.readline())\n",
    "for t in range(1, T+1):\n",
    "    N = int(infile.readline())\n",
    "    best = 0\n",
    "    solve(N)\n",
    "    outfile.write('Case #{}: {}\\n'.format(t, best))\n",
    "            \n",
    "            \n",
    "infile.close()\n",
    "outfile.close()\n",
    "\n",
    "#print solve(1000000000000000000)\n",
    "#best = 0\n",
    "#print solve(12345)\n",
    "\n",
    "#join_number([0,2,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from random import randint\n",
    "with open('bigtest.txt', 'w') as outfile:\n",
    "    outfile.write('100\\n')\n",
    "    for x in range(100):\n",
    "        outfile.write('{}\\n'.format(randint(1, 1000)))"
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
   "language": "python",
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
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
