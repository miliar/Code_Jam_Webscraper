{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def arr2list(a):\n",
    "    \"\"\"\n",
    "    a: list of strings\n",
    "    \"\"\"\n",
    "    result = {}\n",
    "    for i, s in enumerate(a):\n",
    "        t = s.replace('?', '')\n",
    "        for c in t:\n",
    "            result[c] = (i, s.index(c))\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(a):\n",
    "    S = arr2list(a)\n",
    "    N = len(s)\n",
    "    R = len(a)\n",
    "    C = len(a[0])\n",
    "    result = [list(s) for s in a]\n",
    "    starti = 0\n",
    "    startj = 0\n",
    "    klist = list(S.keys())\n",
    "    cdlist = [S[c] for c in S.keys()]\n",
    "    rlist = [cd[0] for cd in cdlist]\n",
    "    clist = [cd[1] for cd in cdlist]\n",
    "    while klist != []:\n",
    "        i = min(rlist)\n",
    "        samerow = [cd[1] for cd in cdlist if cd[0] == i]\n",
    "        j = min(samerow)\n",
    "        for c in klist:\n",
    "            if S[c] == (i, j):\n",
    "                break\n",
    "        samerow.remove(j)\n",
    "        if samerow == []:\n",
    "            endj = C - 1\n",
    "        else:\n",
    "            endj = min(samerow) - 1\n",
    "        samecol = [cd[0] for cd in cdlist if (cd[1] <= endj and cd[1] >= startj)]\n",
    "        #print(S, cdlist, c, startj, endj)\n",
    "        samecol.remove(i)\n",
    "        if samecol == []:\n",
    "            endi = R - 1\n",
    "        else:\n",
    "            endi = min(samecol) - 1\n",
    "        for ii in range(starti, endi + 1):\n",
    "            for jj in range(startj, endj + 1):\n",
    "                result[ii][jj] = c\n",
    "        cdlist.remove((i, j))\n",
    "        rlist.remove(i)\n",
    "        clist.remove(j)\n",
    "        klist.remove(c)\n",
    "        if endj == C - 1:\n",
    "            f = False\n",
    "            for ii in range(R):\n",
    "                if f:\n",
    "                    break\n",
    "                for jj in range(C):\n",
    "                    if result[ii][jj] == '?' or (result[ii][jj] in klist):\n",
    "                        starti = ii\n",
    "                        startj = jj\n",
    "                        f = True\n",
    "                        break\n",
    "        else:\n",
    "            startj = endj + 1\n",
    "    #results = []\n",
    "    #for row in result:\n",
    "        #rows = ''\n",
    "        #for c in row:\n",
    "            #rows += c\n",
    "            #results += [rows]\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
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
    "        s = []\n",
    "        R, C = [int(i) for i in infile.readline().split()]\n",
    "        for ii in range(R):\n",
    "            s += [infile.readline().strip()]\n",
    "        result = solve(s)\n",
    "        outfile.write('Case #' + str(i + 1) + ':\\n')\n",
    "        for ii in range(R):\n",
    "            outfile.write(''.join(result[ii]) + '\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "gcj('A-test.in', 'A-test.out')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
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
   "execution_count": null,
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
   "execution_count": 16,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'c']"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list({'a': (1, 2), 'c': (4, 5)}.keys())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C', 'C']]\n",
      "[['C', 'C', 'D', 'D'], ['C', 'C', 'D', 'D'], ['A', 'A', 'B', 'B'], ['A', 'A', 'B', 'B']]\n",
      "[['D', 'D', 'D', 'D', 'D'], ['C', 'C', 'C', 'A', 'A'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B']]\n",
      "[['A', 'B'], ['C', 'D']]\n"
     ]
    }
   ],
   "source": [
    "print(solve(['A??','?B?', '??C']))\n",
    "print(solve(['????', '?CD?', '?AB?', '????']))\n",
    "print(solve(['???D?', '?C?A?', '??B??', '?????']))\n",
    "print(solve(['AB','CD']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'A': (0, 4), 'B': (0, 11)}"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = [\"????A??????B???\"]\n",
    "arr2list(s)\n",
    "#b = s.replace('?','')\n",
    "#print(b)"
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
   "version": "3.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
