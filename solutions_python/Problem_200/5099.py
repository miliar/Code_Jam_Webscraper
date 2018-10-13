{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "s = \"---+-++-\"\n",
    "k = 3 "
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
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "range(10)[::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def checkIfTidy(n):\n",
    "    n_str = str(n)\n",
    "    isTidy = True\n",
    "    for ind,val_str in enumerate(n_str):\n",
    "        if ind+1 < len(n_str):\n",
    "            if int(val_str) > int(n_str[ind+1]):\n",
    "                isTidy = False\n",
    "    return isTidy\n",
    "            \n",
    "        \n",
    "checkIfTidy(555555554)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "print 1111110%110"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "89999"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def findPreviousTinyNumber(n):\n",
    "    while(True):\n",
    "#        if n%110==0 or n%110==10:\n",
    "            \n",
    "        if checkIfTidy(n):\n",
    "            return n\n",
    "        n=n-1\n",
    "        \n",
    "findPreviousTinyNumber(99990)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "89999"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "findPreviousTinyNumber(99990)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "111111111111111110\n",
      "18\n",
      "100000000000000000\n",
      "11111111111111110\n",
      "99999999999999999\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "\n",
    "def foo(n):\n",
    "    print n\n",
    "    m = len(str(n))\n",
    "    print m\n",
    "    d = 10**(m-1)\n",
    "    print d\n",
    "    print n%d\n",
    "    nextTry = n-(n%d)-1\n",
    "    print nextTry\n",
    "    print checkIfTidy(nextTry)\n",
    "    \n",
    "foo(111111111111111110)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def findPreviousTinyNumber2(n):\n",
    "    if checkIfTidy(n):\n",
    "        return n\n",
    "    m = len(str(n))\n",
    "    d = 10**(m-1)\n",
    "    return n-(n%d)-1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "69"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "findPreviousTinyNumber(76)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "79999"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "findPreviousTinyNumber(88880)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "229"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "findPreviousTinyNumber(232)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(88890, False, 88889, 79999, False)\n",
      "(88790, True, 79999, 79999, True)\n",
      "(11110, True, 9999, 9999, True)\n"
     ]
    }
   ],
   "source": [
    "def thereIsAnHgherNumberAfter(n):\n",
    "    n_str = str(n)\n",
    "    isIncreasing = False\n",
    "    isDecreasing= False\n",
    "    isDescreasingAfterHighest=False\n",
    "    isDescreasingAfterHighestAndIncreasing=False\n",
    "    isDescreasingAfterHighestAndIncreasingAt=0\n",
    "    consecutive_increases = 0\n",
    "    isDescreasingAfterHighestAt=0\n",
    "    isDescrasingForTheFirstTimeAt=0\n",
    "    isDescrasingAt=0\n",
    "    itIncreasedAndDecreased=False\n",
    "    itAlwaysIncreased=True\n",
    "    itIncreased=False\n",
    "    itIsAlwaysEqual=True\n",
    "    itDecreased=False\n",
    "    l = \"\"\n",
    "    highestNumber = None\n",
    "    previousNumber = None\n",
    "    isDescreasingNow=False\n",
    "    isIncreasingNow=False\n",
    "    for ind,val in enumerate(n_str):\n",
    "\n",
    "        \n",
    "        \n",
    "        if highestNumber is None:\n",
    "            highestNumber=int(n_str[0])\n",
    "            previousNumber=int(val)\n",
    "        else:\n",
    "            if int(val)<previousNumber:\n",
    "                if ind<len(n_str)-1:\n",
    "                    itAlwaysIncreased=False\n",
    "                itDecreased=True\n",
    "                isDescreasingNow=True\n",
    "                isIncreasingNow=False\n",
    "                isDescrasingAt=ind\n",
    "                if isDescrasingForTheFirstTimeAt==0:\n",
    "                    isDescrasingForTheFirstTimeAt=ind\n",
    "            else:\n",
    "                itIncreased=True\n",
    "                isIncreasingNow=True\n",
    "                isDescreasingNow=False\n",
    "                \n",
    "            if int(val)!=previousNumber and ind<len(n_str)-1:\n",
    "                itIsAlwaysEqual=False\n",
    "            \n",
    "            if int(val)<highestNumber:\n",
    "                l=l+\"-\"\n",
    "                if isIncreasing:\n",
    "                    isDescreasingAfterHighest=True\n",
    "                    isDescreasingAfterHighestAt=ind\n",
    "                isIncreasing=False\n",
    "                isDescreasing=True\n",
    "            else:\n",
    "                highestNumber=int(val)\n",
    "                if consecutive_increases==0:\n",
    "                    consecutive_increases=1\n",
    "                    isIncreasing=True\n",
    "                else:\n",
    "                    isIncreasing=True\n",
    "                    if isDescreasingAfterHighest:\n",
    "                        isDescreasingAfterHighestAndIncreasing=True\n",
    "                        isDescreasingAfterHighestAndIncreasingAt=ind\n",
    "                    if isIncreasing:\n",
    "                        consecutive_increases=consecutive_increases+1\n",
    "                    \n",
    "                    \n",
    "                l=l+\"+\"\n",
    "                \n",
    "    #if isDescreasingAfterHighestAt==len(n_str)-1:\n",
    "        #isDescreasingAfterHighestAndIncreasing=True\n",
    "    #\n",
    "    #print isDescrasingForTheFirstTimeAt,isDescreasingAfterHighestAndIncreasingAt,itIncreased and itDecreased,itAlwaysIncreased,itIsAlwaysEqual\n",
    "    #print len(n_str)\n",
    "    if itIsAlwaysEqual:\n",
    "        isDescreasingAfterHighestAndIncreasing=True\n",
    "    return isDescreasingAfterHighestAndIncreasing       \n",
    "    #return n,l,highestNumber, isIncreasing,isDecreasing, isDescreasingAfterHighest,isDescreasingAfterHighestAndIncreasing,consecutive_increases,10**(len(n_str)-consecutive_increases),n%(10**(len(n_str)-consecutive_increases)),n-n%(10**(len(n_str)-consecutive_increases-1))-1,len(n_str)-consecutive_increases,n%(10**(len(n_str)-consecutive_increases)),n-(n%(10**(len(n_str)-consecutive_increases-1)))-1\n",
    "    \n",
    "l = [88890,88790,11110]\n",
    "print \"\\n\".join([  str((n,thereIsAnHgherNumberAfter(n),findPreviousTinyNumber(n),findPreviousTinyNumber2(n),findPreviousTinyNumber(n)==findPreviousTinyNumber2(n))) for n in l])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "88890 False 88889 79999 88889\n",
      "88790 True 79999 79999 79999\n"
     ]
    }
   ],
   "source": [
    "def combined(n):\n",
    "    if thereIsAnHgherNumberAfter(n):\n",
    "        return findPreviousTinyNumber2(n) \n",
    "    else:\n",
    "        return findPreviousTinyNumber(n)\n",
    "    \n",
    "print 88890,thereIsAnHgherNumberAfter(88890),findPreviousTinyNumber(88890),findPreviousTinyNumber2(88890),combined(88890)\n",
    "print 88790,thereIsAnHgherNumberAfter(88790),findPreviousTinyNumber(88790),findPreviousTinyNumber2(88790),combined(88790)"
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
    "def nextNumberToTry(n):\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "132\n",
      "Case #1: 129\n",
      "1000\n",
      "Case #2: 999\n",
      "7\n",
      "Case #3: 7\n"
     ]
    }
   ],
   "source": [
    "f = open(\"/Users/robertopagano/Desktop/test_input.txt\")\n",
    "n_cases = None\n",
    "count = 0\n",
    "for line in f:\n",
    "    print int(line)\n",
    "    if n_cases==None:\n",
    "        n_cases=int(line)\n",
    "    else:\n",
    "        print \"Case #%d: %d\" % (count,findPreviousTinyNumber(int(line)))\n",
    "        \n",
    "    count = count + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "132\n",
      "Case #1: 99\n",
      "1000\n",
      "Case #2: 999\n",
      "7\n",
      "Case #3: 7\n"
     ]
    }
   ],
   "source": [
    "f = open(\"/Users/robertopagano/Desktop/test_input.txt\")\n",
    "n_cases = None\n",
    "count = 0\n",
    "for line in f:\n",
    "    print int(line)\n",
    "    if n_cases==None:\n",
    "        n_cases=int(line)\n",
    "    else:\n",
    "        print \"Case #%d: %d\" % (count,findPreviousTinyNumber2(int(line)))\n",
    "        \n",
    "    count = count + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
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
     "execution_count": 152,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "combined(111111111111111110)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 129\n",
      "Case #2: 999\n",
      "Case #3: 7\n",
      "Case #4: 99999999999999999\n"
     ]
    }
   ],
   "source": [
    "f = open(\"/Users/robertopagano/Desktop/test_input.txt\")\n",
    "n_cases = None\n",
    "count = 0\n",
    "for line in f:\n",
    "    #print int(line)\n",
    "    if n_cases==None:\n",
    "        n_cases=int(line)\n",
    "    else:\n",
    "        print \"Case #%d: %d\" % (count,combined(int(line)))\n",
    "        \n",
    "    count = count + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "f = open(\"/Users/robertopagano/Downloads/B-small-attempt0.in\")\n",
    "f_out=open(\"/Users/robertopagano/Desktop/B-small-attempt0.out\",\"w\")\n",
    "n_cases = None\n",
    "count = 0\n",
    "for line in f:\n",
    "    #print int(line)\n",
    "    if n_cases==None:\n",
    "        n_cases=int(line)\n",
    "    else:\n",
    "        f_out.write( \"Case #%d: %d\" % (count,combined(int(line))) +\"\\n\")\n",
    "        \n",
    "    count = count + 1\n",
    "f_out.close()"
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
 "nbformat_minor": 0
}
