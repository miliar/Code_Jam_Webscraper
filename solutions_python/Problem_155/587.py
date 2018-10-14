{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#Problem A. Standing Ovation"
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
    "cases = [] \n",
    "with open('A-large-attempt0.in') as f:\n",
    "    n_cases = int(f.readline())\n",
    "    for _ in range(n_cases):\n",
    "        _, case = f.readline().strip().split()\n",
    "        cases.append(case)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "ret = []\n",
    "for i, case in enumerate(cases):\n",
    "    standing = 0\n",
    "    x = 0\n",
    "    for level, count in enumerate(case):\n",
    "        count = int(count)\n",
    "        if standing < level:\n",
    "            x += level - standing\n",
    "            standing = level\n",
    "        standing += count\n",
    "    ret.append('Case #%s: %s' % (i + 1, x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "with open('A-large-attempt0.out', 'w') as f:\n",
    "    for line in ret:\n",
    "        f.write(line + '\\n')"
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
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
