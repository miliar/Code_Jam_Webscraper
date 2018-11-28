{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-05-13T14:39:57.014572Z",
     "start_time": "2017-05-13T14:39:57.010586Z"
    },
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from collections import Counter\n",
    "import numpy as np\n",
    "import sys\n",
    "\n",
    "from joblib import Parallel, delayed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-05-13T15:49:20.719131Z",
     "start_time": "2017-05-13T15:49:20.577098Z"
    },
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "filepath = 'B-large'\n",
    "\n",
    "filepath_in = filepath + '.in'\n",
    "filepath_out = filepath + '.out'\n",
    "\n",
    "with open(filepath_in) as fin:\n",
    "    T = int(fin.readline())\n",
    "    data = []\n",
    "    for t in range(T):\n",
    "        N, C, M = [int(_) for _ in fin.readline().strip('\\r\\n').split()]\n",
    "        P, B = [], []\n",
    "        for i in range(M):\n",
    "            Pi, Bi = [int(_) for _ in fin.readline().strip('\\r\\n').split()]\n",
    "            P.append(Pi)\n",
    "            B.append(Bi)\n",
    "        data.append({'N': N, 'C': C, 'M': M, 'P': P, 'B': B})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-05-13T15:49:20.903370Z",
     "start_time": "2017-05-13T15:49:20.781947Z"
    },
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def ok_1(R, p2b, data_):\n",
    "    N, C, M, P, B = [data_[key] for key in 'NCMPB']\n",
    "    promo = 0\n",
    "    left = [0] * N\n",
    "    used = [0] * C\n",
    "    for i in range(N):\n",
    "        left[i] += R\n",
    "        for b, count_ in p2b[i].items():\n",
    "            count = count_\n",
    "            #print('mk1', i, b, count_, left, used, promo)\n",
    "            for place in reversed(range(i+1)):\n",
    "                while left[place] > 0 and used[b] < R and count > 0:\n",
    "                    left[place] -= 1\n",
    "                    count -= 1\n",
    "                    if place != i:\n",
    "                        promo += 1\n",
    "                    used[b] += 1\n",
    "                    #print('mk3', place)\n",
    "            if count > 0:\n",
    "                return False, 0 # fail...\n",
    "            #print('mk2', i, b, count_, left, used, promo)\n",
    "    \n",
    "    return True, promo\n",
    "\n",
    "\n",
    "def solve(data_):\n",
    "    N, C, M, P, B = [data_[key] for key in 'NCMPB']\n",
    "\n",
    "    P = [_ - 1 for _ in P]\n",
    "    B = [_ - 1 for _ in B]\n",
    "\n",
    "    p2b = [[] for i in range(N)]\n",
    "    for p, b in zip(P, B):\n",
    "        p2b[p].append(b)\n",
    "    for i in range(N):\n",
    "        p2b[i] = Counter(p2b[i])\n",
    "        pass\n",
    "\n",
    "    #print('p2b', p2b)\n",
    "    #return\n",
    "\n",
    "    low, high = 1, M\n",
    "    while low < high:\n",
    "        mid = (low + high) // 2\n",
    "        verdict, promo = ok_1(mid, p2b, data_)\n",
    "        #print('ok_1', mid, verdict)\n",
    "        if verdict:\n",
    "            high = mid\n",
    "        else:\n",
    "            low = mid + 1\n",
    "    assert low == high\n",
    "    R = low\n",
    "    verdict, promo = ok_1(R, p2b, data_)\n",
    "\n",
    "    return '%d %d' % (R, promo)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-05-13T15:49:25.295894Z",
     "start_time": "2017-05-13T15:49:21.430292Z"
    },
    "collapsed": false
   },
   "outputs": [],
   "source": [
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
