{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "cases = [] \n",
    "with open('B-large.in') as f:\n",
    "    n_cases = int(f.readline())\n",
    "    for _ in range(n_cases):\n",
    "        k, l, s = map(int, f.readline().split())\n",
    "        keyboard = f.readline().strip()\n",
    "        target = f.readline().strip()\n",
    "        cases.append((s, keyboard, target))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def max_bananas(target, s):\n",
    "    x = len(target)\n",
    "    for i in range(1, len(target)):\n",
    "        if target[i:] == target[:-i]:\n",
    "            x = i\n",
    "            break\n",
    "    if s < len(target):\n",
    "        return 0\n",
    "    s -= len(target)\n",
    "    return s // x + 1        "
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
    "from collections import Counter"
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
    "def build_automaton(target):\n",
    "    d = {}\n",
    "    fringe = target\n",
    "    state = ''\n",
    "    while len(fringe):\n",
    "        e = fringe[0]\n",
    "        fringe = fringe[1:]\n",
    "        d[state] = {}\n",
    "        for i in range(len(state), 0, -1):\n",
    "            if target.startswith(state[i:]):\n",
    "                l = target[len(state[i:])]\n",
    "                d[state][l] = (state[i:] + l, 0)  \n",
    "        if state + e == target:\n",
    "            if e in d[state] and d[state][e][0] != state + e:\n",
    "                d[state][e] = (d[state][e][0], 1)\n",
    "                state = d[state][e][0]\n",
    "            else:\n",
    "                d[state][e] = ('', 1)   \n",
    "                state = ''\n",
    "        else:\n",
    "            d[state][e] = (state + e, 0) \n",
    "            state += e\n",
    "    return d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from collections import defaultdict"
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
    "def process_target(target, s, probs):\n",
    "    d = build_automaton(target)\n",
    "    #print d\n",
    "    states = [('', 1, 0)] # state, prob, payoff\n",
    "    for _ in range(s):\n",
    "        nstates = []\n",
    "        for state, prob, bananas in states:\n",
    "            tot_prob = 0\n",
    "            for e in d[state]:\n",
    "                nstate, bans = d[state][e]\n",
    "                nprob = prob * probs[e]\n",
    "                nbananas = bananas + bans\n",
    "                nstates.append((nstate, nprob, nbananas))\n",
    "                tot_prob += probs[e]\n",
    "            nstates.append(('', prob * (1 - tot_prob), bananas))\n",
    "        statedict = defaultdict(list)\n",
    "        for state, prob, bananas in nstates:\n",
    "            statedict[(state, bananas)].append(prob)\n",
    "        states = [(state, sum(v), bananas) for (state, bananas), v in statedict.items()]\n",
    "        #print states\n",
    "    return sum([p * b for _, p, b in states])   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "ret = []\n",
    "for i, (s, keyboard, target) in enumerate(cases):\n",
    "    x = 7\n",
    "    if set(target) - set(keyboard) != set() or len(target) > s:\n",
    "        x = 0.\n",
    "    else:\n",
    "        kbs = dict(Counter(keyboard))\n",
    "        norm = float(len(keyboard))\n",
    "        probs = {k: v / norm for k, v in kbs.items()}\n",
    "        max_ban = max_bananas(target, s)\n",
    "        x = max_ban - process_target(target, s, probs)\n",
    "        #print x\n",
    "    ret.append('Case #%s: %s' % (i + 1, x))"
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
    "with open('B-large.out', 'w') as f:\n",
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
   "version": "2.7.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
