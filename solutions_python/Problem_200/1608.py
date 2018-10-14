{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "i_f = open('B-large.in', 'r')\n",
    "o_f = open('outputB-large.txt', 'w')\n",
    "t = int(i_f.readline())  # read a line with a single integer\n",
    "for i in range(1, t + 1):\n",
    "    n = int(i_f.readline())  # read a list of integers, 2 in this case\n",
    "    o_f.write(\"Case #{}: {}\\n\".format(i, solve(n)))\n",
    "o_f.close()\n",
    "i_f.close()"
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
    "def solve(n):\n",
    "    if(n<10):\n",
    "        return n\n",
    "    c = n\n",
    "    l = []\n",
    "    while (c>0):\n",
    "        l.insert(0, c%10)\n",
    "        c = c//10\n",
    "    l2 = aux(l)\n",
    "    s = 0\n",
    "    for i in range(len(l2)):\n",
    "        s = 10*s + l2[i]\n",
    "    return s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def aux(l):\n",
    "    k=0\n",
    "    for i in range(len(l)-1):\n",
    "        if l[i]>l[i+1]:\n",
    "            break\n",
    "        k+=1\n",
    "    if (k+1 == len(l)):\n",
    "        return l\n",
    "    for i in range(k+1,len(l)):\n",
    "        l[i]=9\n",
    "    b = True\n",
    "    while (k>=0):\n",
    "        if l[k]>0:\n",
    "            l[k]-=1\n",
    "            break\n",
    "        l[k]=9\n",
    "        k-=1\n",
    "    return aux(l)"
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
