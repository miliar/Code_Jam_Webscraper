{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "4 2\n",
      "Case #1: 1 0\n",
      "5 2\n",
      "Case #2: 1 0\n",
      "6 2\n",
      "Case #3: 1 1\n",
      "1000 1000\n",
      "Case #4: 0 0\n",
      "1000 1\n",
      "Case #5: 500 499\n"
     ]
    }
   ],
   "source": [
    "import heapq\n",
    "T = int(input())\n",
    "for caseNo in range(1, T+1):\n",
    "    N, K = [int(_) for _ in input().split(' ')]\n",
    "    heap = []\n",
    "    heapq.heappush(heap, -N)\n",
    "    for _ in range(K-1):\n",
    "        N = -heapq.heappop(heap)\n",
    "        L = N//2\n",
    "        R = N - L - 1\n",
    "        heapq.heappush(heap, -L)\n",
    "        heapq.heappush(heap, -R)\n",
    "    N = -heapq.heappop(heap)\n",
    "    L = N//2\n",
    "    R = N - L - 1\n",
    "    print(\"Case #{}: {} {}\".format(caseNo, L, R))"
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
