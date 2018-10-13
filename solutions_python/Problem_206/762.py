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
    "#"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 255,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(case):\n",
    "    D,N = case[0]\n",
    "    D = int(D)\n",
    "    N = float(N)\n",
    "    horseTimes = []\n",
    "    for horse in case[1:]:\n",
    "        #calc time they reach D -- dist/vel = time\n",
    "        horseTimes.append((D - int(horse[0])) / float(horse[1]))\n",
    "        \n",
    "    mySpeeds = []\n",
    "    for hTime in horseTimes:\n",
    "        #calc speed to meet each horse at the finish line -- dist / time = vel\n",
    "        mySpeeds.append(D / hTime)\n",
    "    \n",
    "    \n",
    "    mySpeeds.sort()\n",
    "    mySpeeds = list(reversed(mySpeeds))\n",
    "    if len(mySpeeds) == 1:\n",
    "        return mySpeeds[0]\n",
    "    for s in mySpeeds:\n",
    "        #determine if this speed will cause collision with any horse -- x = c / m - n\n",
    "        isSafe = True\n",
    "        for horse in case[1:]:\n",
    "            \n",
    "            if float(horse[1]) < s and s*(float(horse[0]) / (s - float(horse[1]))) < float(D):\n",
    "                isSafe = False\n",
    "                break\n",
    "        if isSafe:\n",
    "            return s\n",
    "    return min(mySpeeds)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 262,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def jam():\n",
    "    f = open(\"A-small-attempt5.in\")\n",
    "    answers = []\n",
    "    cases = int(f.readline())\n",
    "    for caseNum in range(0,cases):\n",
    "        ans = \"Case #\" + str(caseNum+1) + \": \"\n",
    "        case = []\n",
    "        D,N = f.readline().strip().split(\" \")\n",
    "        case.append([D,N])  \n",
    "        for i in range(0,int(N)):\n",
    "            case.append(f.readline().strip().split(\" \"))\n",
    "        aq = solve(case)\n",
    "        if 'e' in str(aq):\n",
    "            ans = ans + str('%.20f' % solve(case)) + \"\\n\"\n",
    "        else:\n",
    "            ans = ans + str(aq) + \"\\n\"\n",
    "        \n",
    "        answers.append(ans)\n",
    "    \n",
    "    q = open(\"A-small.out\",'w')\n",
    "    for ans in answers:\n",
    "        q.write(ans)\n",
    "    q.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "jam()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "q = [3,2,3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "q.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 264,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "q = [['2525','1'],['2400','5']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 265,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "101.0"
      ]
     },
     "execution_count": 265,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solve(q)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 266,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "q = [['300','2'],['120','60'],['60','90']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 267,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100.0"
      ]
     },
     "execution_count": 267,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solve(q)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 268,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "q = [['569566545','2'],['111060259','6228'],['218893231','3681']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 269,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5978.71114921793"
      ]
     },
     "execution_count": 269,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solve(q)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 237,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 237,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "isclose(569566545.0,569566545)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100.0"
      ]
     },
     "execution_count": 206,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "round(99.99999)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1000000000000000000.00000000000000000000'"
      ]
     },
     "execution_count": 207,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'%.20f' % 1000000000000000000.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can only concatenate list (not \"int\") to list",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-208-513d74adf916>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mq\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: can only concatenate list (not \"int\") to list"
     ]
    }
   ],
   "source": [
    "q + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):\n",
    "    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)"
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
