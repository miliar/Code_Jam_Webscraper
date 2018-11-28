{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-08T01:00:24.487265-04:00",
     "start_time": "2017-04-08T01:00:24.369204"
    },
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def solve(s, k):\n",
    "    s = [int(c == '+') for c in s]\n",
    "    n = len(s)\n",
    "    ans = 0\n",
    "    for i in range(n - k + 1):\n",
    "        if s[i] == 0:\n",
    "            for j in range(i, i + k):\n",
    "                s[j] = 1 - s[j]\n",
    "            ans += 1\n",
    "    if sum(s) == n:\n",
    "        return '%d' % ans\n",
    "    else:\n",
    "        return 'IMPOSSIBLE'\n",
    "\n",
    "\n",
    "input_filename = 'A-large.in'\n",
    "output_filename = 'A-large.out'\n",
    "\n",
    "inps = []\n",
    "with open(input_filename) as fin:\n",
    "    T = int(fin.readline())\n",
    "    for t in range(T):\n",
    "        tks = fin.readline().split()\n",
    "        s, k = tks[0], int(tks[1])\n",
    "        inps.append((s, k))\n",
    "\n",
    "anss = []\n",
    "for s, k in inps:\n",
    "    ans = solve(s, k)\n",
    "    anss.append(ans)\n",
    "\n",
    "with open(output_filename, 'w') as fout:\n",
    "    for c, ans in enumerate(anss):\n",
    "        print('Case #%d: %s' % (c + 1, ans), file=fout)"
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
   "display_name": "Python ML (env35)",
   "language": "python",
   "name": "env35"
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
   "version": "3.5.3"
  },
  "latex_envs": {
   "LaTeX_envs_menu_present": true,
   "bibliofile": "biblio.bib",
   "cite_by": "apalike",
   "current_citInitial": 1,
   "eqLabelWithNumbers": true,
   "eqNumInitial": 1,
   "labels_anchors": false,
   "latex_user_defs": false,
   "report_style_numbering": false,
   "user_envs_cfg": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
