{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def solve(case):\n",
    "    scase = case\n",
    "    case = int(case)\n",
    "    while case > 0:\n",
    "        if isSorted(scase):\n",
    "            return scase\n",
    "        case = nextNum(case,scase)\n",
    "        scase = str(case)\n",
    "    return \"ERROR\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def nextNum(n,sn):\n",
    "    \n",
    "    return n - (int(sn[getErrPos(n,sn):])+1)\n",
    "    \n",
    "def getErrPos(n,strn):\n",
    "    prev = int(strn[0])\n",
    "    for i in range(1,len(strn)):\n",
    "        iq = int(strn[i])\n",
    "        if iq < prev:\n",
    "            return i\n",
    "        prev = iq\n",
    "        \n",
    "    return 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def isSorted(s):\n",
    "    q = []\n",
    "    for c in s:\n",
    "        q.append(int(c))\n",
    "    return sorted(q) == q"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2'"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"132\"[getErrPos(132,\"132\"):]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9999"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nextNum(10999,\"10999\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "99999999999999999"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solve(\"111111111111111110\")"
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
    "f = open(\"B-small.in\")\n",
    "answers = []\n",
    "f.readline()\n",
    "count = 1\n",
    "for case in f:\n",
    "    ans = \"Case #\" + str(count) + \": \"\n",
    "    case = case.strip()\n",
    "    ans += solve(case) + \"\\n\"\n",
    "    count += 1\n",
    "    answers.append(ans)\n",
    "    \n",
    "q = open(\"B-small.out\", 'w')\n",
    "for ans in answers:\n",
    "    q.write(ans)\n",
    "q.close()"
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
 "nbformat_minor": 0
}
