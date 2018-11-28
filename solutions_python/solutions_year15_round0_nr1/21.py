{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def read_input(fin_name):\n",
    "    with open(fin_name, 'r') as fin:\n",
    "        fin.readline()\n",
    "        for line in fin:\n",
    "            s_max, audiences = line.split()\n",
    "            s_max = int(s_max)\n",
    "            audiences = map(int, audiences)\n",
    "            yield (s_max, audiences)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def proceed(case):\n",
    "    s_max, audiences = case\n",
    "    extra_count = 0\n",
    "    current_up = 0\n",
    "    for i in xrange(s_max+1):\n",
    "        if current_up >= i:\n",
    "            current_up += audiences[i]\n",
    "        else:\n",
    "            extra = i - current_up\n",
    "            current_up += (audiences[i] + extra)\n",
    "            extra_count += extra\n",
    "    return extra_count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def runit(fin_name, fout_name):\n",
    "    with open(fout_name, 'w') as fout:\n",
    "        for i, case in enumerate(read_input(fin_name), 1):\n",
    "            fout.write('Case #{}: {}\\n'.format(i, proceed(case)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "runit('A-small-attempt0.in', 'A-small-attempt0.out')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "runit('A-large.in', 'A-large.out')"
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
   "version": "2.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
