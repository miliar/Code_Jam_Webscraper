{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Tidy Numbers\n",
    "idea - take the last number and move from the least significant digit to the most, make the right part of the number tidy until the whole number is tidy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def get_tidy(num):\n",
    "    snum = str(num)\n",
    "    snum = map(lambda x: int(x), snum[::-1])\n",
    "    for i in range(len(snum) - 1):\n",
    "        if snum[i] < snum[i + 1]:\n",
    "            for j in range(i + 1):\n",
    "                snum[j] = 9\n",
    "            snum[i + 1] -= 1 \n",
    "    return int(''.join(map(lambda x: str(x), snum[::-1])))\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "with open('q2/B-large.in', 'r') as f:\n",
    "    data = f.readlines()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number of cases -  100\n"
     ]
    }
   ],
   "source": [
    "n = int(data[0])\n",
    "print 'number of cases - ', n\n",
    "out = ''\n",
    "for i in range(n):\n",
    "    out += 'Case #%d: %d\\n' % (i + 1, get_tidy(int(data[i + 1])))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "with open('q2/output.txt', 'w') as f:\n",
    "    f.write(out)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "999"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "get_tidy(1000)"
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
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
