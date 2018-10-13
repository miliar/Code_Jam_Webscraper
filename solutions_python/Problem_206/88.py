{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-22T12:27:39.829447-04:00",
     "start_time": "2017-04-22T12:27:39.809733"
    },
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "basename = 'A-large'\n",
    "#basename = 'sample'\n",
    "input_file = basename + '.in'\n",
    "output_file = basename + '.out'\n",
    "\n",
    "datas = []\n",
    "with open(input_file) as fin:\n",
    "    T = int(fin.readline())\n",
    "    for t in range(T):\n",
    "        D, N = [int(_) for _ in fin.readline().split()]\n",
    "        h = []\n",
    "        for i in range(N):\n",
    "            K, S = [int(_) for _ in fin.readline().split()]\n",
    "            h.append((K, S))\n",
    "        data = {\n",
    "            'D': D,\n",
    "            'N': N,\n",
    "            'h': h,\n",
    "        }\n",
    "        datas.append(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-22T12:27:40.475224-04:00",
     "start_time": "2017-04-22T12:27:40.468602"
    },
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def solve(data):\n",
    "    N, D, h = data['N'], data['D'], data['h']\n",
    "    h_time = [(D - K) * 1.0 / S  for K, S in h]\n",
    "    \n",
    "    return D / max(h_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-22T12:27:40.655729-04:00",
     "start_time": "2017-04-22T12:27:40.644595"
    }
   },
   "outputs": [],
   "source": [
    "with open(output_file, 'w') as fout: \n",
    "    for t, data in enumerate(datas):\n",
    "        res = solve(data)\n",
    "        print('Case #%d: %.8f' % (t + 1, res), file=fout)"
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
