{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 2, 1, 0]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(4-1, -1, -1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def solve(in_file, out_file):\n",
    "    with open(in_file, 'r') as fin, open(out_file, 'w') as fout:\n",
    "        T = int(fin.readline().strip())\n",
    "        for t in range(1, T+1):\n",
    "            D, N = map(int, fin.readline().strip().split(' '))\n",
    "            pos, vs = np.empty(N), np.empty(N)\n",
    "            times = np.zeros(N)\n",
    "            \n",
    "            for h in range(N):\n",
    "                p, s = map(int, find.readline().strip().split(' '))\n",
    "                pos[h], vs[h] = p, s\n",
    "            \n",
    "            # set the last one\n",
    "            times[-1] = (D - pos[-1]) / vs[-1]\n",
    "            \n",
    "            # N-2, skip the last one\n",
    "            for h in range(N-2, -1, -1):\n",
    "                times[h] = max((D - pos[h]) / vs[h], times[h+1])\n",
    "                \n",
    "            # solve for Annie\n",
    "            va = D / times[0]\n",
    "            print('Case #{t}: {v:.6f}'.format(t=t, v=va))\n",
    "            "
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
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
 "nbformat_minor": 0
}
