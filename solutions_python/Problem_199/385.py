{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-08T11:45:03.232097",
     "start_time": "2017-04-08T11:45:03.101484"
    },
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from __future__ import division, print_function\n",
    "from builtins import input\n",
    "import numpy as np\n",
    "import sys\n",
    "sys.stdin = sys.__stdin__\n",
    "sys.stdout = sys.__stdout__\n",
    "#sys.stdin = open(\"A.txt\")\n",
    "#sys.stdin = open(\"./A-small-attempt0.in\")\n",
    "#sys.stdout = open(\"./A-small-attempt0.out\", \"w\")\n",
    "sys.stdin = open(\"./A-large.in\")\n",
    "sys.stdout = open(\"./A-large.out\", \"w\")\n",
    "\n",
    "for tc in range(int(input().strip())):\n",
    "    s, k = input().split()\n",
    "    k = int(k)\n",
    "    s = np.array([int(x==\"+\") for x in s])\n",
    "    cnt=0\n",
    "    for i in range(len(s)-k+1):\n",
    "        if s[i]==0:\n",
    "            s[i:i+k] = 1-s[i:i+k]\n",
    "            cnt += 1\n",
    "    print(\"Case #%d: %s\"%(tc+1, cnt if s.sum()==len(s) else \"IMPOSSIBLE\"))\n"
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
