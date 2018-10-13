{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "cases = [] \n",
    "with open('C-small-attempt0.in') as f:\n",
    "    n_cases = int(f.readline())\n",
    "    for _ in range(n_cases):\n",
    "        c, d, v = map(int, f.readline().split())\n",
    "        vals = map(int, f.readline().strip().split(' '))\n",
    "        cases.append((c, v, vals))"
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
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def process(c, v, coins):\n",
    "    coins = sorted(coins, reverse=True)\n",
    "    opts = [0] \n",
    "    for coin in coins:\n",
    "        nopts = [o + m * coin for o in opts for m in range(c + 1)]\n",
    "        opts = nopts\n",
    "    x = set(range(v + 1)) - set(opts)\n",
    "    return x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\n",
      "[4, 1, 2]\n",
      "[1, 2]\n",
      "[10, 26, 1, 2, 4, 8]\n",
      "[1, 2, 5, 4, 13]\n",
      "[15, 20, 1, 2, 4, 8]\n",
      "[1, 4, 7, 2]\n",
      "[1, 3, 7, 12, 2]\n",
      "[2, 18, 30, 1, 4, 8, 16]\n",
      "[21, 1, 2, 4, 8, 16]\n",
      "[1, 2, 4, 12, 8, 28]\n",
      "[3, 5, 1, 2]\n",
      "[3, 1, 2, 7, 14]\n",
      "[6, 8, 1, 2, 4]\n",
      "[1, 2]\n",
      "[1, 6, 9, 2, 4]\n",
      "[9, 1, 2, 4, 8]\n",
      "[2, 3, 1, 7, 14]\n",
      "[21, 1, 2, 4, 8, 16]\n",
      "[5, 1, 2, 4, 13]\n",
      "[6, 9, 1, 2, 4]\n",
      "[1, 2, 4, 8, 16]\n",
      "[3, 4, 5, 1, 2]\n",
      "[2, 7, 14, 24, 1, 4]\n",
      "[4, 1, 2, 8, 16]\n",
      "[2, 5, 9, 1, 4, 22]\n",
      "[2, 1, 4]\n",
      "[5, 10, 20, 1, 2, 4]\n",
      "[1, 2]\n",
      "[21, 1, 2, 4, 8, 16]\n",
      "[3, 7, 1, 2, 14]\n",
      "[24, 30, 1, 2, 4, 8, 16]\n",
      "[25, 1, 2, 4, 8, 16]\n",
      "[10, 22, 24, 27, 1, 2, 4, 8]\n",
      "[8, 19, 23, 1, 2, 4, 16]\n",
      "[2, 7, 1, 4, 15]\n",
      "[1, 2, 4, 8, 16]\n",
      "[1]\n",
      "[9, 1, 2, 4, 8]\n",
      "[16, 1, 2, 4, 8]\n",
      "[11, 1, 2, 4, 8]\n",
      "[4, 9, 18, 1, 2, 8]\n",
      "[3, 1, 2, 7, 14]\n",
      "[1, 2, 4, 8, 16]\n",
      "[5, 8, 14, 1, 2, 4]\n",
      "[1, 6, 2, 4, 14, 28]\n",
      "[2, 3, 6, 14, 1, 13]\n",
      "[1, 2, 4, 8, 16]\n",
      "[12, 1, 2, 4, 8]\n",
      "[4, 9, 1, 2, 8]\n",
      "[1, 2, 4]\n",
      "[1, 4, 8, 2]\n",
      "[5, 1, 2, 4]\n",
      "[4, 21, 25, 1, 2, 8, 16]\n",
      "[5, 1, 2, 4, 13]\n",
      "[2, 5, 9, 1, 4]\n",
      "[3, 5, 10, 23, 27, 1, 2, 22]\n",
      "[24, 29, 1, 2, 4, 8, 16]\n",
      "[2, 5, 1, 4, 13, 26]\n",
      "[5, 6, 1, 2, 4, 19]\n",
      "[1, 2]\n",
      "[11, 12, 1, 2, 4, 8]\n",
      "[2, 3, 6, 1, 13, 26]\n",
      "[17, 22, 24, 1, 2, 4, 8, 16]\n",
      "[1, 2, 4, 8, 16]\n",
      "[11, 26, 1, 2, 4, 8]\n",
      "[15, 1, 2, 4, 8]\n",
      "[9, 21, 1, 2, 4, 8]\n",
      "[1, 4, 2, 8]\n",
      "[12, 25, 1, 2, 4, 8]\n",
      "[6, 10, 1, 2, 4]\n",
      "[1, 2, 4, 8, 16]\n",
      "[2, 1, 4, 8, 16]\n",
      "[3, 1, 2, 7, 14]\n",
      "[20, 1, 2, 4, 8, 16]\n",
      "[5, 1, 2, 4, 13]\n",
      "[5, 1, 2, 4, 13]\n",
      "[2, 25, 26, 1, 4, 8, 16]\n",
      "[2, 7, 12, 1, 4]\n",
      "[3, 5, 6, 1, 2]\n",
      "[1, 2]\n",
      "[1, 2, 4, 8, 15]\n",
      "[4, 8, 16, 1, 2]\n",
      "[1, 2, 5, 4]\n",
      "[5, 8, 16, 1, 2, 4]\n",
      "[5, 1, 2, 4]\n",
      "[1, 2, 4]\n",
      "[1, 2, 3, 4, 5]\n",
      "[1, 13, 19, 23, 2, 4, 8]\n",
      "[20, 25, 1, 2, 4, 8, 16]\n",
      "[4, 1, 2]\n",
      "[4, 9, 14, 1, 2, 8]\n",
      "[5, 9, 11, 14, 1, 2, 4]\n",
      "[9, 10, 1, 2, 4, 8]\n",
      "[4, 1, 2]\n",
      "[13, 1, 2, 4, 8]\n",
      "[30, 1, 2, 4, 8, 16]\n",
      "[5, 21, 27, 1, 2, 4, 13]\n",
      "[1, 4, 6, 16, 2, 14]\n",
      "[4, 8, 1, 2]\n"
     ]
    }
   ],
   "source": [
    "ret = []\n",
    "for i, (c, v, coins) in enumerate(cases):\n",
    "    n_orig_coins = len(coins)\n",
    "    coins = [coin for coin in coins]\n",
    "    n = math.log(v + 1) / math.log(c + 1) - n_orig_coins\n",
    "    bottom = int(math.ceil(n))\n",
    "    x = process(c, v, coins)\n",
    "    while x:\n",
    "        coins += [min(x)]\n",
    "        x = process(c, v, coins)\n",
    "    print coins\n",
    "    x = len(coins) - n_orig_coins\n",
    "    ret.append('Case #%s: %s' % (i + 1, x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "with open('C-small-attempt0.out', 'w') as f:\n",
    "    for line in ret:\n",
    "        f.write(line + '\\n')"
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
   "version": "2.7.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
