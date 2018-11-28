{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-05-13T14:16:56.343899Z",
     "start_time": "2017-05-13T14:16:56.339960Z"
    },
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from collections import Counter\n",
    "import numpy\n",
    "import sys\n",
    "\n",
    "from joblib import Parallel, delayed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-05-13T14:16:56.618674Z",
     "start_time": "2017-05-13T14:16:56.605500Z"
    },
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "filepath = 'A-small-attempt0'\n",
    "\n",
    "filepath_in = filepath + '.in'\n",
    "filepath_out = filepath + '.out'\n",
    "\n",
    "with open(filepath_in) as fin:\n",
    "    T = int(fin.readline())\n",
    "    data = []\n",
    "    for t in range(T):\n",
    "        N, P = [int(_) for _ in fin.readline().strip('\\r\\n').split()]\n",
    "        G = [int(_) for _ in fin.readline().strip('\\r\\n').split()]\n",
    "        data.append({'N': N, 'P': P, 'G': G})"
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
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-05-13T14:17:00.669264Z",
     "start_time": "2017-05-13T14:17:00.396409Z"
    },
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(data_):\n",
    "    N, P, G = [data_[key] for key in 'NPG']\n",
    "\n",
    "    G = [_ % P for _ in G]\n",
    "    counter = Counter(G)\n",
    "\n",
    "    assert P in [2, 3, 4]\n",
    "    if P == 2:\n",
    "        return counter[0] + (counter[1] + 1) // 2\n",
    "    elif P == 3:\n",
    "        res = counter[0]\n",
    "\n",
    "        tmp = min(counter[1], counter[2])\n",
    "        res += tmp\n",
    "        counter[1] -= tmp\n",
    "        counter[2] -= tmp\n",
    "\n",
    "        for i in [1, 2]:\n",
    "            res += (counter[i] + 2) // 3\n",
    "        return res\n",
    "\n",
    "    elif P == 4:\n",
    "        res = counter[0]\n",
    "\n",
    "        tmp = min(counter[1], counter[3])\n",
    "        res += tmp\n",
    "        counter[1] -= tmp\n",
    "        counter[3] -= tmp\n",
    "\n",
    "        tmp = counter[2] // 2\n",
    "        res += tmp\n",
    "        counter[2] -= tmp * 2\n",
    "\n",
    "        tmp = min(counter[1] // 2, counter[2])\n",
    "        res += tmp\n",
    "        counter[1] -= tmp * 2\n",
    "        counter[2] -= tmp\n",
    "\n",
    "        tmp = min(counter[3] // 2, counter[2])\n",
    "        res += tmp\n",
    "        counter[3] -= tmp * 2\n",
    "        counter[2] -= tmp\n",
    "\n",
    "        for i in [1, 2, 3]:\n",
    "            tmp = (counter[i] + 3) // 4\n",
    "            res += tmp\n",
    "            \n",
    "        return res\n",
    "\n",
    "    return res\n",
    "\n",
    "\n",
    "res = Parallel(n_jobs=-1)(delayed(solve)(data_) for data_ in data)\n",
    "\n",
    "with open(filepath_out, 'w') as fout:\n",
    "    #fout = sys.stdout\n",
    "    for t, res_ in enumerate(res):\n",
    "        print('Case #%d: %s' % (t + 1, res_), file=fout)"
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
   "display_name": "Python 3 ML",
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
   "version": "3.6.1"
  },
  "latex_envs": {
   "LaTeX_envs_menu_present": true,
   "autocomplete": true,
   "bibliofile": "biblio.bib",
   "cite_by": "apalike",
   "current_citInitial": 1,
   "eqLabelWithNumbers": true,
   "eqNumInitial": 1,
   "hotkeys": {
    "equation": "Ctrl-E",
    "itemize": "Ctrl-I"
   },
   "labels_anchors": false,
   "latex_user_defs": false,
   "report_style_numbering": false,
   "user_envs_cfg": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
