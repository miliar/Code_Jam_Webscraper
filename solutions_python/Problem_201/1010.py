{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def bisect(q, t):\n",
    "    def compare(l, r):\n",
    "        if l == r:\n",
    "            if q[l] == t:\n",
    "                return "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def compare(q, term, l, r):\n",
    "    lv = q[l][0]\n",
    "    rv = q[r][0]\n",
    "    if l == r:\n",
    "        if lv == term[0]:\n",
    "            q[l][1] += term[1]\n",
    "        elif lv > term[0]:\n",
    "            q[l : l] = [term]\n",
    "        else:\n",
    "            q[l + 1 : l + 1] = [term]\n",
    "        return q\n",
    "    else:\n",
    "        m = int((l + r) / 2)\n",
    "        if q[m][0] >= term[0]:\n",
    "            compare(q, term, l, m)\n",
    "        else:\n",
    "            compare(q, term, m + 1, r)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def addt(q, term):\n",
    "    if q == []:\n",
    "        q += [term]\n",
    "    else:\n",
    "        compare(q, term, 0, len(q) - 1)\n",
    "    return q"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def solve(n, k):\n",
    "    q = [[n, 1]]\n",
    "    i = k\n",
    "    while i > 0:\n",
    "        #print(q)\n",
    "        t = q.pop()\n",
    "        #print(i, q, t)\n",
    "        l = int((t[0] - 1) / 2)\n",
    "        r = int(t[0] / 2)\n",
    "        if i <= t[1]:\n",
    "            return str(r) + ' ' + str(l)\n",
    "        i -= t[1]\n",
    "        newt1 = [l, t[1]]\n",
    "        newt2 = [r, t[1]]\n",
    "        q = addt(q, newt1)\n",
    "        #print(q)\n",
    "        q = addt(q, newt2)\n",
    "        #print(newt2, q)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
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
    "        [n, k] = [int(i) for i in infile.readline().split()]\n",
    "        outfile.write('Case #' + str(i + 1) + ': ' + solve(n, k) + '\\n')"
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
    "gcj('C-test.in', 'C-test.out')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "gcj('C-small-2-attempt0.in', 'C-small-2-attempt0.out')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'0 0'"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solve(3, 2)\n",
    "#q = [(10, 1)]\n",
    "#t = q.pop()\n",
    "#l = int(t[0] / 2)\n",
    "#print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "print(solve(4, 2) == (1, 0))\n",
    "print(solve(5, 2) == (1, 0))\n",
    "print(solve(6, 2) == (1, 1))\n",
    "print(solve(10000, 10000) == (0, 0))\n",
    "print(solve(1000, 1) == (500, 499))\n",
    "print(solve(10, 2) == (2, 2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "[1, 2, (4, 5)]\n"
     ]
    }
   ],
   "source": [
    "a = (1, 2)\n",
    "print(a[1])\n",
    "b = [1, 2]\n",
    "b[2:2] = [(4, 5)]\n",
    "print(b)"
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
