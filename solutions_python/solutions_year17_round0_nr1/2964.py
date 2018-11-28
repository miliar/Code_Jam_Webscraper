{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from IPython.core.debugger import Tracer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def find_next_flip(s, start):\n",
    "    try:\n",
    "        return s.index(0, start)\n",
    "    except ValueError:\n",
    "        return len(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def flip(s, start, count):\n",
    "    for i in range(start, start + k):\n",
    "        s[i] ^= 1  # flip them"
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
    "def solve(s, k):\n",
    "    n = 0\n",
    "#     Tracer()()\n",
    "    next_flip = find_next_flip(s, 0)\n",
    "    while next_flip <= len(s) - k:\n",
    "        flip(s, next_flip, k)\n",
    "        n += 1\n",
    "        next_flip = find_next_flip(s, next_flip + 1)\n",
    "    \n",
    "    if next_flip < len(s):\n",
    "        return 'IMPOSSIBLE'\n",
    "    return n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "fin = open(\"pancake_small.in\", 'r')\n",
    "fout = open('pancake.out', 'w')\n",
    "\n",
    "T = int(fin.readline().strip())\n",
    "for test in range(T):\n",
    "    s, k = fin.readline().strip().split()\n",
    "    l = list(map(lambda x: 0 if x == '-' else 1, s))\n",
    "    k = int(k)\n",
    "#     print(s, l)\n",
    "    r = solve(l, k)\n",
    "    print(\"Case #{}: {}\".format(test+1, r), file=fout)\n",
    "\n",
    "fin.close()\n",
    "fout.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# make big file\n",
    "with open('pancake_big.in', 'w') as fout:\n",
    "    fout.writelines('100\\n')\n",
    "    for t in range(100):\n",
    "        fout.write('-' * 1000)\n",
    "        fout.write(' 4')\n",
    "        fout.write('\\n')"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
