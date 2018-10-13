{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import os\n",
    "import sys"
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
   "execution_count": 57,
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
    "### Problem #1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
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
    "for line in getinput('A-small-attempt0.in'):\n",
    "    x, k = line\n",
    "    printout(solve([b for b in x], int(k)), 'output.txt')\n",
    "    #printout(solve([b for b in x], int(k)))\n",
    "    "
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
   "version": "3.5.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
