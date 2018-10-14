{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "i_f = open('A-large.in', 'r')\n",
    "o_f = open('outputA.txt', 'w')\n",
    "t = int(i_f.readline())  # read a line with a single integer\n",
    "for i in range(1, t + 1):\n",
    "    (s,n) = i_f.readline().split(\" \")  # read a list of integers, 2 in this case\n",
    "    o_f.write(\"Case #{}: {}\\n\".format(i, solve(list(s),int(n),0)))\n",
    "o_f.close()\n",
    "i_f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(s,n,k):\n",
    "    l = len(s)\n",
    "    if (l<n):\n",
    "        return \"IMPOSSIBLE\"\n",
    "    if (l==n):\n",
    "        p=0\n",
    "        m=0\n",
    "        for i in range(l):\n",
    "            if s[i]=='+':\n",
    "                p+=1\n",
    "            elif s[i]=='-':\n",
    "                m+=1\n",
    "        if (p>0)&(m>0):\n",
    "            return \"IMPOSSIBLE\"\n",
    "        if m==0:\n",
    "            return k\n",
    "        return k+1\n",
    "    if s[0]=='+':\n",
    "        return solve(s[1:],n,k)\n",
    "    for i in range(n):\n",
    "        s[i]=flip(s[i])\n",
    "    return solve(s[1:],n,k+1)        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def flip(c):\n",
    "    if c=='+':\n",
    "        return '-'\n",
    "    if c=='-':\n",
    "        return '+'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "sys.setrecursionlimit(1500)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import sys"
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
