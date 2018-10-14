{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "9876543210\n",
      "Case #1: 8999999999\n"
     ]
    }
   ],
   "source": [
    "T = int(input())\n",
    "for caseNo in range(1, T+1):\n",
    "    N = [int(_) for _ in input()]\n",
    "    nine_start = len(N)\n",
    "    for i in range(len(N)-1, 0, -1):\n",
    "        if N[i] < N[i-1]:\n",
    "            nine_start = i\n",
    "            N[i-1] -= 1\n",
    "    ans = ''.join(str(_) for _ in N[:nine_start]) + '9'*(len(N)-nine_start) \n",
    "    print(\"Case #{}: {}\".format(caseNo, int(ans)))"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [default]",
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
