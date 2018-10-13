{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import collections"
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
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 5, 6, 1000000, 1000000, 2, 917000, 50000, 67100, 79800, 100000, 99009, 99900, 424, 600, 747, 500, 999, 437, 1000, 500, 500, 671, 522, 500, 391, 357, 999, 634, 488, 274, 1000, 1, 1000, 574, 643, 500, 1000, 500, 500, 971, 500, 999, 946, 1000, 5, 500, 449, 1000, 500, 4, 999, 673, 999, 983, 317, 2, 500, 500, 753, 755, 704, 711, 683, 468, 1000, 999, 500, 799, 673, 999, 1000, 694, 603, 999, 999, 1000, 1000, 500, 523, 500, 3, 1000, 1000, 527, 999, 592, 999, 450, 3, 999, 999, 500, 1000, 392, 999, 1000, 544, 999, 394] [2, 2, 2, 1000000, 1, 1, 900000, 25500, 62300, 68000, 12008, 48008, 12008, 353, 474, 715, 206, 511, 341, 499, 500, 2, 542, 407, 244, 296, 284, 487, 599, 444, 250, 255, 1, 511, 486, 633, 499, 999, 248, 256, 800, 249, 999, 839, 489, 1, 116, 403, 512, 128, 1, 498, 630, 2, 835, 308, 2, 1, 250, 666, 567, 673, 625, 531, 368, 506, 512, 245, 795, 604, 1, 2, 622, 511, 420, 127, 500, 488, 117, 470, 127, 2, 256, 127, 483, 256, 483, 255, 398, 1, 998, 499, 101, 498, 311, 506, 388, 459, 497, 370]\n"
     ]
    }
   ],
   "source": [
    "N = []\n",
    "K = []\n",
    "with open('bath.in','r') as f:\n",
    "    for line in f :\n",
    "        try :\n",
    "            l = line.split()\n",
    "            K.append(int(l[1]))\n",
    "            N.append(int(l[0]))\n",
    "        except :\n",
    "            pass\n",
    "print(N,K)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def my_func(x) :\n",
    "    if x%2 :\n",
    "        return(x//2,x//2)\n",
    "    return(x//2,x//2-1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def c1(a) :\n",
    "    un,cnt = np.unique(a, return_counts=True)\n",
    "    d = dict(zip(un,cnt))\n",
    "    m = max(un)\n",
    "    return m,d[m]\n",
    "\n",
    "def c2(a) :\n",
    "    c = collections.Counter(a)\n",
    "    m = max(a)\n",
    "    return m, c[m]\n",
    "\n",
    "def c3(a) :\n",
    "    m = max(a)\n",
    "    return m,(a==m).sum()"
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
    "out_b = []\n",
    "for i in range(len(N)) :\n",
    "    spaces = np.array([N[i]])\n",
    "    count = 0\n",
    "    while 42 :\n",
    "        v,q = c3(spaces)\n",
    "        fans = my_func(v)\n",
    "        if count+q >= K[i] :\n",
    "            out_b.append(fans)\n",
    "            break\n",
    "        spaces = np.concatenate((spaces[spaces!=v],np.array(fans*q)))\n",
    "        count += q\n",
    "\n",
    "with open('bath.out','w') as f2 :\n",
    "    for idx,ans in enumerate(out_b) :\n",
    "        f2.write('Case #{}: {} {}\\n'.format(idx+1,ans[0],ans[1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100000 loops, best of 3: 16.3 µs per loop\n",
      "The slowest run took 4.08 times longer than the fastest. This could mean that an intermediate result is being cached.\n",
      "100000 loops, best of 3: 11.2 µs per loop\n"
     ]
    }
   ],
   "source": [
    "a = np.array([4,1,3,2,1,2,3,4,3,2,3,4,4,4,4,4,4,4])\n",
    "#print(c1(a),c2(a),c3(a))\n",
    "#%timeit c1(a)\n",
    "%timeit c2(a)\n",
    "%timeit c3(a)"
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
