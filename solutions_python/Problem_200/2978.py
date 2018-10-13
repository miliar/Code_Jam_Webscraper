{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import os\n",
    "import sys\n",
    "import pandas as pd\n",
    "from tqdm import tqdm\n",
    "\n",
    "sys.setrecursionlimit(5000)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Templates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "casenum = 0\n",
    "\n",
    "def getinput(fname='input.txt', cast=lambda x: x):\n",
    "    global casenum\n",
    "    casenum = 0\n",
    "    \n",
    "    flag = True\n",
    "    for line in open(fname, 'r'):\n",
    "        if flag:\n",
    "            flag = False # Skip the first line\n",
    "        else:\n",
    "            yield [cast(x) for x in line.strip().split(' ')]\n",
    "        \n",
    "def printout(x, fname=None):\n",
    "    global casenum\n",
    "    casenum += 1\n",
    "    if casenum == 1 and fname:\n",
    "        try:\n",
    "            os.remove(fname)\n",
    "        except:\n",
    "            pass\n",
    "    print(\"Case #{}: {}\".format(casenum, x), file=open(fname, 'a') if fname else sys.stdout)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Problem A"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def flip(x):\n",
    "    return '+' if x == '-' else '-'\n",
    "\n",
    "def solve(x, k, ix=0, flips=0):\n",
    "    \n",
    "    # Find the first bit that needs flipped\n",
    "    while ix < len(x) and x[ix] == '+':\n",
    "        ix += 1\n",
    "        \n",
    "    # If we reached the end, then we are done\n",
    "    if ix + k > len(x):\n",
    "        return flips if all([b == '+' for b in x]) else 'IMPOSSIBLE'\n",
    "        \n",
    "    # Flip the immediately next k bits\n",
    "    for i in range(k):\n",
    "        x[ix + i] = flip(x[ix + i])\n",
    "        \n",
    "    return solve(x, k, ix + 1, flips + 1)\n",
    "\n",
    "\n",
    "for line in getinput('A-large.in'):\n",
    "    x, k = line\n",
    "    printout(solve([b for b in x], int(k)), 'output.txt')\n",
    "    #printout(solve([b for b in x], int(k)))\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Problem B"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# Generate all tidy numbers between 1 and 10^18\n",
    "def genx(base):\n",
    "    last = int(base[-1])\n",
    "    for i in range(last, 10):\n",
    "        num = base + str(i)\n",
    "        yield num\n",
    "        if len(num) <= 18:\n",
    "            yield from genx(num)\n",
    "\n",
    "# Save them in a cache\n",
    "cache = []\n",
    "for i in range(1, 10):\n",
    "    cache += [str(i)]\n",
    "    cache += list(genx(str(i)))\n",
    "\n",
    "# Convert back to numeric type\n",
    "cache = sorted([int(num) for num in cache])"
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
    "def solve(n):\n",
    "    for i in range(len(cache)):\n",
    "        if n < cache[i]: return cache[i-1]\n",
    "\n",
    "for line in getinput('B-large.in', int):\n",
    "    n = line[0]\n",
    "    printout(solve(n), 'output.txt')\n",
    "    #printout(solve(n))\n"
   ]
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
   "version": "3.5.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
