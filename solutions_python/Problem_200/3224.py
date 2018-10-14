{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 26,
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
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def pos_non_tidy(n):\n",
    "    for i in range(len(n) - 1):\n",
    "        if n[i] > n[i+1]:\n",
    "            return i\n",
    "    return -1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def fill_nine(n, start):\n",
    "    for i in range(start, len(n)):\n",
    "        n[i] = 9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
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
   "execution_count": 23,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def solve(n):\n",
    "#     Tracer()()\n",
    "    l = pos_non_tidy(n)\n",
    "    while l >= 0:\n",
    "        n[l] -= 1\n",
    "        fill_nine(n, l+1)\n",
    "        l = pos_non_tidy(n)\n",
    "\n",
    "    if n[0] == 0:\n",
    "        return n[1:]\n",
    "    return n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "fin = open('tidy.in', 'r')\n",
    "# fout = sys.stdout\n",
    "fout = open('tidy.out', 'w')\n",
    "T = int(fin.readline())\n",
    "\n",
    "for i in range(T):\n",
    "    N = fin.readline().strip()\n",
    "    res = solve(list(map(int, N)))\n",
    "    print('Case #{}: {}'.format(i+1, ''.join(map(str, res))), file=fout)\n",
    "\n",
    "fin.close()\n",
    "fout.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 129\r\n",
      "Case #2: 999\r\n",
      "Case #3: 7\r\n",
      "Case #4: 99999999999999999\r\n",
      "Case #5: 9999999\r\n",
      "Case #6: 899999\r\n",
      "Case #7: 8899\r\n"
     ]
    }
   ],
   "source": [
    "%cat tidy.out"
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
    "solve()"
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
    "with open('tidy_big.in', 'w') as f:\n",
    "    f.write('')"
   ]
  }
 ],
 "metadata": {
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
