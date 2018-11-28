{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "A = open('A-large.in')\n",
    "a = [i.strip().split() for i in A.read().strip().split('\\n')];"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "it = int(a[0][0]); a.remove(a[0]);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "b = [[int(i[0]), [int(j) for j in i[1]]] for i in a];"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "ans = [max([max((j[1][i],i+1)) - sum(j[1][:i+1]) for i in range(len(j[1]))]) for j in b];"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "f = open('A.out','w')\n",
    "for i in range(len(ans)):\n",
    "    #print('Case #%d: %d\\n'%(i+1,ans[i]))\n",
    "    f.write('Case #%d: %d\\n'%(i+1,ans[i]))\n",
    "f.close()"
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
   "version": "3.4.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
