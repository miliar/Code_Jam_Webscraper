{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(s):\n",
    "    pos = -1\n",
    "    for i in range(len(s) - 1):\n",
    "        if s[i] > s[i + 1]:\n",
    "            pos = i\n",
    "            break\n",
    "    if pos == -1:\n",
    "        return s\n",
    "    pos1 = s.find(s[pos])\n",
    "    prefix = s[:pos1] + str(int(s[pos1]) - 1)\n",
    "    result = prefix + '9' * (len(s) - len(prefix))\n",
    "    result = str(int(result))\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
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
    "        s = infile.readline().strip()\n",
    "        outfile.write('Case #' + str(i + 1) + ': ' + solve(s) + '\\n')"
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
    "gcj('B-test.in', 'B-test.out')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "gcj('B-small-attempt0.in', 'B-small-attempt0.out')"
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
    "gcj('B-large.in', 'B-large.out')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'129'"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solve('132')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "''"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print('1' > '0')\n",
    "str(int('099'))\n",
    "'3444'.find('4')\n",
    "pos1 = 0\n",
    "a = '43332'\n",
    "a[:pos1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "33999999\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'129'"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(solve('34444443'))\n",
    "solve('132')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
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
    "print(solve('3') == '3')\n",
    "print(solve('110000000') == '99999999')\n",
    "print(solve('100000000') == '99999999')\n",
    "print(solve('200000000') == '199999999')\n",
    "print(solve('4444443') == '3999999')\n",
    "print(solve('999999999') == '999999999')"
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
