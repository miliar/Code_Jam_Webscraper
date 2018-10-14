{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-08T01:13:53.331952-04:00",
     "start_time": "2017-04-08T01:13:53.309449"
    }
   },
   "outputs": [],
   "source": [
    "def solve(s):\n",
    "    n = len(s)\n",
    "    last = 0\n",
    "    i = 0\n",
    "    while i + 1 < n:\n",
    "        i += 1\n",
    "        if s[i - 1] == s[i]:\n",
    "            pass\n",
    "        elif s[i - 1] < s[i]:\n",
    "            last = i\n",
    "        else:\n",
    "            res = list(s)\n",
    "            res[last] = chr(ord(s[last]) - 1)\n",
    "            for j in range(last + 1, n):\n",
    "                res[j] = '9'\n",
    "            while len(res) > 0 and res[0] == '0':\n",
    "                res = res[1:]\n",
    "            res = ''.join(res)\n",
    "            return res\n",
    "    else:\n",
    "        return s\n",
    "\n",
    "input_filename = 'B-small-attempt0.in'\n",
    "output_filename = 'B-small-attempt0.out'\n",
    "\n",
    "inps = []\n",
    "with open(input_filename) as fin:\n",
    "    T = int(fin.readline())\n",
    "    for t in range(T):\n",
    "        inps.append(fin.readline().strip('\\r\\n'))\n",
    "    \n",
    "anss = []\n",
    "for s in inps:\n",
    "    ans = solve(s)\n",
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
