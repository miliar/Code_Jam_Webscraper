{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(s, k):\n",
    "    l = [True if c == '+' else False for c in s]\n",
    "    result = 0\n",
    "    for i in range(len(l) - k + 1):\n",
    "        if not l[i]:\n",
    "            result += 1\n",
    "            for j in range(k):\n",
    "                l[i + j] = not l[i + j]\n",
    "    if all(l):\n",
    "        return str(result)\n",
    "    else:\n",
    "        return \"IMPOSSIBLE\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'3'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solve('---+-++-', 3)"
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
    "def gcj(infilename, outfilename):\n",
    "    infile = open(infilename, 'r')\n",
    "    outfile = open(outfilename, 'w')\n",
    "    T = int(infile.readline())\n",
    "    for i in range(T):\n",
    "        s, kstr = infile.readline().split()\n",
    "        k = int(kstr)\n",
    "        outfile.write('Case #' + str(i + 1) + ': ' + solve(s, k) + '\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "gcj('A-test.in', 'A-test.out')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "gcj('A-small-attempt0.in', 'A-small-attempt0.out')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "gcj('A-large.in', 'A-large.out')"
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
