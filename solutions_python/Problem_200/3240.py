{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### A - House of pancakes"
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
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### B - Tidy numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def tidy(number):\n",
    "    N = len(number)\n",
    "    for i in range(N-2,-1,-1):\n",
    "        if number[i] > number[i+1]:\n",
    "            number[i] = str(int(number[i]) - 1)\n",
    "            for j in range(i+1, N):\n",
    "                number[j] = '9'\n",
    "            return tidy(number)\n",
    "    return str(long(\"\".join(number)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'13999'"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tidy(list(str(14123)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 129\n",
      "Case #2: 999\n",
      "Case #3: 7\n",
      "Case #4: 455\n",
      "Case #5: 1\n",
      "Case #6: 599\n",
      "Case #7: 47\n",
      "Case #8: 899\n",
      "Case #9: 588\n",
      "Case #10: 559\n",
      "Case #11: 569\n",
      "Case #12: 799\n",
      "Case #13: 39\n",
      "Case #14: 18\n",
      "Case #15: 899\n",
      "Case #16: 699\n",
      "Case #17: 899\n",
      "Case #18: 799\n",
      "Case #19: 469\n",
      "Case #20: 359\n",
      "Case #21: 269\n",
      "Case #22: 299\n",
      "Case #23: 469\n",
      "Case #24: 245\n",
      "Case #25: 799\n",
      "Case #26: 599\n",
      "Case #27: 899\n",
      "Case #28: 369\n",
      "Case #29: 899\n",
      "Case #30: 899\n",
      "Case #31: 389\n",
      "Case #32: 599\n",
      "Case #33: 899\n",
      "Case #34: 789\n",
      "Case #35: 899\n",
      "Case #36: 899\n",
      "Case #37: 179\n",
      "Case #38: 899\n",
      "Case #39: 689\n",
      "Case #40: 799\n",
      "Case #41: 259\n",
      "Case #42: 299\n",
      "Case #43: 446\n",
      "Case #44: 599\n",
      "Case #45: 299\n",
      "Case #46: 899\n",
      "Case #47: 999\n",
      "Case #48: 99\n",
      "Case #49: 259\n",
      "Case #50: 569\n",
      "Case #51: 699\n",
      "Case #52: 799\n",
      "Case #53: 239\n",
      "Case #54: 399\n",
      "Case #55: 269\n",
      "Case #56: 799\n",
      "Case #57: 366\n",
      "Case #58: 179\n",
      "Case #59: 169\n",
      "Case #60: 138\n",
      "Case #61: 399\n",
      "Case #62: 489\n",
      "Case #63: 499\n",
      "Case #64: 8\n",
      "Case #65: 589\n",
      "Case #66: 899\n",
      "Case #67: 899\n",
      "Case #68: 479\n",
      "Case #69: 699\n",
      "Case #70: 248\n",
      "Case #71: 599\n",
      "Case #72: 444\n",
      "Case #73: 899\n",
      "Case #74: 119\n",
      "Case #75: 69\n",
      "Case #76: 679\n",
      "Case #77: 589\n",
      "Case #78: 899\n",
      "Case #79: 189\n",
      "Case #80: 599\n",
      "Case #81: 899\n",
      "Case #82: 799\n",
      "Case #83: 799\n",
      "Case #84: 568\n",
      "Case #85: 699\n",
      "Case #86: 559\n",
      "Case #87: 89\n",
      "Case #88: 347\n",
      "Case #89: 499\n",
      "Case #90: 258\n",
      "Case #91: 899\n",
      "Case #92: 288\n",
      "Case #93: 899\n",
      "Case #94: 899\n",
      "Case #95: 899\n",
      "Case #96: 399\n",
      "Case #97: 779\n",
      "Case #98: 799\n",
      "Case #99: 799\n",
      "Case #100: 189\n"
     ]
    }
   ],
   "source": [
    "filename = \"B-small-attempt0.in\"\n",
    "f = open('datajam/' + filename, 'r')\n",
    "T = int(f.readline())\n",
    "for i in range(T):\n",
    "    l = f.readline().strip()\n",
    "    answer = tidy(list(l))\n",
    "    print \"Case #\" + str(i+1) + \": \" + answer"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Tests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "l = list(\"lolil\")"
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
   "execution_count": 28,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4994544894165154165464984894148\n"
     ]
    }
   ],
   "source": [
    "print long(\"04994544894165154165464984894148\")"
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
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
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
