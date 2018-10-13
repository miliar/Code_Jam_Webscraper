{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#Problem C. Dijkstra"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "cases = [] \n",
    "with open('C-small-attempt2.in') as f:\n",
    "    n_cases = int(f.readline())\n",
    "    for _ in range(n_cases):\n",
    "        l, x = map(int, f.readline().split())\n",
    "        line = f.readline().strip()\n",
    "        assert len(line) == l\n",
    "        cases.append((line, x))"
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
    "lookup = {}\n",
    "for e in ['i', 'j', 'k']:\n",
    "    lookup[(1, e)] = (1, e)\n",
    "    lookup[(e, e)] = (-1, 1)\n",
    "lookup.update({('i', 'j'): (1, 'k'),\n",
    "               ('j', 'k'): (1, 'i'),\n",
    "               ('k', 'i'): (1, 'j'),\n",
    "               ('j', 'i'): (-1, 'k'),\n",
    "               ('k', 'j'): (-1, 'i'),\n",
    "               ('i', 'k'): (-1, 'j'),})"
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
    "move_curr = {'i': 'j', 'j': 'k', 'k': 1, 1: 1}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def solve(case, rep):\n",
    "    sign, tot = 1, 1\n",
    "    curr = 'i'\n",
    "    for l in case * rep:\n",
    "        nsign, tot = lookup[(tot, l)]\n",
    "        sign *= nsign\n",
    "        if sign == 1 and tot == curr:\n",
    "            tot = 1\n",
    "            curr = move_curr[curr]\n",
    "    x = 'NO'\n",
    "    if curr == 1 and tot == 1 and sign == 1:\n",
    "        x = 'YES'\n",
    "    return x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "ret = []\n",
    "for i, (case, rep) in enumerate(cases):\n",
    "    x = solve(case, rep)\n",
    "    ret.append('Case #%s: %s' % (i + 1, x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "with open('C-small-attempt2.out', 'w') as f:\n",
    "    for line in ret:\n",
    "        f.write(line + '\\n')"
   ]
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
