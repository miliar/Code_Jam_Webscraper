{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-08T14:36:37.680488",
     "start_time": "2017-04-08T14:36:37.675818"
    },
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from __future__ import division, print_function\n",
    "from builtins import input\n",
    "import numpy as np\n",
    "import sys\n",
    "old_stdin = sys.stdin\n",
    "old_stdout = sys.stdout"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-08T14:36:40.087842",
     "start_time": "2017-04-08T14:36:40.075001"
    },
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 1 0\n",
      "Case #2: 1 0\n",
      "Case #3: 1 1\n",
      "Case #4: 0 0\n",
      "Case #5: 500 499\n"
     ]
    }
   ],
   "source": [
    "\n",
    "def f(n, k):\n",
    "    mx, mn = n//2, (n-1)//2\n",
    "    if k==1:\n",
    "        return mx, mn\n",
    "    if k%2==1:\n",
    "        return f(mn, (k-1)//2)\n",
    "    else:\n",
    "        return f(mx, k//2)\n",
    "    \n",
    "\n",
    "def main():\n",
    "    for tc in range(int(input().strip())):\n",
    "        N, K = (int(x) for x in input().split())\n",
    "        mx, mn = f(N, K)\n",
    "        print(\"Case #%d: %d %d\"%(tc+1, mx, mn))\n",
    "\n",
    "sys.stdin = open(\"./C.in\")\n",
    "\n",
    "main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-08T14:39:54.448146",
     "start_time": "2017-04-08T14:39:54.426290"
    },
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "inout = \"./C-small-1-attempt0\"\n",
    "inout = \"./C-small-2-attempt0\"\n",
    "inout = \"./C-large\"\n",
    "\n",
    "sys.stdin = open(inout+\".in\")\n",
    "sys.stdout = open(inout+\".out\", \"w\")\n",
    "\n",
    "main()\n",
    "\n",
    "sys.stdin = old_stdin\n",
    "sys.stdout = old_stdout"
   ]
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
 "nbformat_minor": 2
}
