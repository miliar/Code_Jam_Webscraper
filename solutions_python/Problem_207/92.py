{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-22T13:34:54.401984-04:00",
     "start_time": "2017-04-22T13:34:54.395652"
    }
   },
   "outputs": [],
   "source": [
    "basename = 'B-small-attempt1'\n",
    "input_file = basename + '.in'\n",
    "output_file = basename + '.out'\n",
    "\n",
    "datas = []\n",
    "with open(input_file) as fin:\n",
    "    T = int(fin.readline())\n",
    "    for t in range(T):\n",
    "        count = [int(_) for _ in fin.readline().split()]\n",
    "        data = {\n",
    "            'count': count\n",
    "        }\n",
    "        datas.append(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-22T13:34:54.731910-04:00",
     "start_time": "2017-04-22T13:34:54.715536"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'count': [6, 2, 0, 2, 0, 2, 0]},\n",
       " {'count': [3, 1, 0, 2, 0, 0, 0]},\n",
       " {'count': [5, 1, 0, 2, 0, 2, 0]},\n",
       " {'count': [5, 3, 0, 1, 0, 1, 0]},\n",
       " {'count': [1000, 500, 0, 1, 0, 499, 0]},\n",
       " {'count': [564, 138, 0, 314, 0, 112, 0]},\n",
       " {'count': [774, 262, 0, 179, 0, 333, 0]},\n",
       " {'count': [399, 34, 0, 187, 0, 178, 0]},\n",
       " {'count': [411, 155, 0, 226, 0, 30, 0]},\n",
       " {'count': [259, 86, 0, 105, 0, 68, 0]},\n",
       " {'count': [975, 304, 0, 375, 0, 296, 0]},\n",
       " {'count': [988, 489, 0, 443, 0, 56, 0]},\n",
       " {'count': [4, 2, 0, 2, 0, 0, 0]},\n",
       " {'count': [21, 18, 0, 1, 0, 2, 0]},\n",
       " {'count': [682, 192, 0, 206, 0, 284, 0]},\n",
       " {'count': [563, 275, 0, 268, 0, 20, 0]},\n",
       " {'count': [194, 59, 0, 41, 0, 94, 0]},\n",
       " {'count': [961, 425, 0, 209, 0, 327, 0]},\n",
       " {'count': [514, 4, 0, 509, 0, 1, 0]},\n",
       " {'count': [245, 46, 0, 118, 0, 81, 0]},\n",
       " {'count': [952, 161, 0, 449, 0, 342, 0]},\n",
       " {'count': [257, 0, 0, 0, 0, 257, 0]},\n",
       " {'count': [1000, 333, 0, 333, 0, 334, 0]},\n",
       " {'count': [473, 108, 0, 211, 0, 154, 0]},\n",
       " {'count': [892, 412, 0, 385, 0, 95, 0]},\n",
       " {'count': [120, 46, 0, 37, 0, 37, 0]},\n",
       " {'count': [743, 272, 0, 106, 0, 365, 0]},\n",
       " {'count': [14, 4, 0, 5, 0, 5, 0]},\n",
       " {'count': [987, 454, 0, 97, 0, 436, 0]},\n",
       " {'count': [524, 222, 0, 188, 0, 114, 0]},\n",
       " {'count': [216, 43, 0, 84, 0, 89, 0]},\n",
       " {'count': [4, 1, 0, 2, 0, 1, 0]},\n",
       " {'count': [711, 208, 0, 265, 0, 238, 0]},\n",
       " {'count': [3, 2, 0, 1, 0, 0, 0]},\n",
       " {'count': [826, 94, 0, 397, 0, 335, 0]},\n",
       " {'count': [766, 339, 0, 301, 0, 126, 0]},\n",
       " {'count': [4, 1, 0, 1, 0, 2, 0]},\n",
       " {'count': [12, 6, 0, 0, 0, 6, 0]},\n",
       " {'count': [290, 80, 0, 91, 0, 119, 0]},\n",
       " {'count': [999, 500, 0, 249, 0, 250, 0]},\n",
       " {'count': [898, 357, 0, 444, 0, 97, 0]},\n",
       " {'count': [962, 101, 0, 409, 0, 452, 0]},\n",
       " {'count': [647, 267, 0, 100, 0, 280, 0]},\n",
       " {'count': [312, 151, 0, 15, 0, 146, 0]},\n",
       " {'count': [400, 123, 0, 107, 0, 170, 0]},\n",
       " {'count': [552, 273, 0, 259, 0, 20, 0]},\n",
       " {'count': [229, 43, 0, 93, 0, 93, 0]},\n",
       " {'count': [4, 0, 0, 3, 0, 1, 0]},\n",
       " {'count': [568, 128, 0, 241, 0, 199, 0]},\n",
       " {'count': [830, 180, 0, 504, 0, 146, 0]},\n",
       " {'count': [680, 65, 0, 340, 0, 275, 0]},\n",
       " {'count': [1000, 0, 0, 501, 0, 499, 0]},\n",
       " {'count': [764, 256, 0, 129, 0, 379, 0]},\n",
       " {'count': [736, 309, 0, 98, 0, 329, 0]},\n",
       " {'count': [6, 2, 0, 1, 0, 3, 0]},\n",
       " {'count': [658, 19, 0, 75, 0, 564, 0]},\n",
       " {'count': [999, 499, 0, 250, 0, 250, 0]},\n",
       " {'count': [999, 500, 0, 0, 0, 499, 0]},\n",
       " {'count': [703, 287, 0, 103, 0, 313, 0]},\n",
       " {'count': [187, 78, 0, 42, 0, 67, 0]},\n",
       " {'count': [639, 208, 0, 164, 0, 267, 0]},\n",
       " {'count': [302, 151, 0, 30, 0, 121, 0]},\n",
       " {'count': [512, 137, 0, 166, 0, 209, 0]},\n",
       " {'count': [1000, 0, 0, 500, 0, 500, 0]},\n",
       " {'count': [820, 250, 0, 309, 0, 261, 0]},\n",
       " {'count': [177, 23, 0, 75, 0, 79, 0]},\n",
       " {'count': [999, 333, 0, 333, 0, 333, 0]},\n",
       " {'count': [400, 144, 0, 78, 0, 178, 0]},\n",
       " {'count': [146, 23, 0, 68, 0, 55, 0]},\n",
       " {'count': [6, 0, 0, 3, 0, 3, 0]},\n",
       " {'count': [382, 17, 0, 174, 0, 191, 0]},\n",
       " {'count': [236, 114, 0, 45, 0, 77, 0]},\n",
       " {'count': [963, 305, 0, 434, 0, 224, 0]},\n",
       " {'count': [984, 12, 0, 565, 0, 407, 0]},\n",
       " {'count': [218, 90, 0, 103, 0, 25, 0]},\n",
       " {'count': [752, 245, 0, 197, 0, 310, 0]},\n",
       " {'count': [376, 171, 0, 55, 0, 150, 0]},\n",
       " {'count': [1000, 250, 0, 500, 0, 250, 0]},\n",
       " {'count': [942, 146, 0, 414, 0, 382, 0]},\n",
       " {'count': [64, 25, 0, 19, 0, 20, 0]},\n",
       " {'count': [3, 1, 0, 1, 0, 1, 0]},\n",
       " {'count': [666, 313, 0, 236, 0, 117, 0]},\n",
       " {'count': [897, 328, 0, 131, 0, 438, 0]},\n",
       " {'count': [5, 3, 0, 0, 0, 2, 0]},\n",
       " {'count': [4, 2, 0, 1, 0, 1, 0]},\n",
       " {'count': [129, 56, 0, 21, 0, 52, 0]},\n",
       " {'count': [237, 34, 0, 110, 0, 93, 0]},\n",
       " {'count': [643, 557, 0, 51, 0, 35, 0]},\n",
       " {'count': [559, 164, 0, 122, 0, 273, 0]},\n",
       " {'count': [3, 3, 0, 0, 0, 0, 0]},\n",
       " {'count': [288, 30, 0, 9, 0, 249, 0]},\n",
       " {'count': [236, 9, 0, 118, 0, 109, 0]},\n",
       " {'count': [999, 1, 0, 499, 0, 499, 0]},\n",
       " {'count': [419, 85, 0, 163, 0, 171, 0]},\n",
       " {'count': [7, 2, 0, 2, 0, 3, 0]},\n",
       " {'count': [617, 251, 0, 129, 0, 237, 0]},\n",
       " {'count': [711, 282, 0, 109, 0, 320, 0]},\n",
       " {'count': [72, 36, 0, 31, 0, 5, 0]},\n",
       " {'count': [4, 2, 0, 0, 0, 2, 0]}]"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "datas"
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
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-22T13:34:56.698604-04:00",
     "start_time": "2017-04-22T13:34:56.567813"
    }
   },
   "outputs": [],
   "source": [
    "import copy\n",
    "\n",
    "\n",
    "def sub_solve(r):\n",
    "    r.sort(key=lambda _: -len(_))\n",
    "\n",
    "    line = []\n",
    "    line.extend([(0, _) for _ in r[0]])\n",
    "    line.extend([(2, _) for _ in r[2]])\n",
    "    line.extend([(1, _) for _ in r[1]])\n",
    "\n",
    "    # print('r = ', r)\n",
    "    # print('line = ', line)\n",
    "\n",
    "    res = []\n",
    "    n = (len(line) + 1) // 2\n",
    "    for i in range(n):\n",
    "        j = i + n\n",
    "        if j < len(line):\n",
    "            if line[i][0] == line[j][0]:\n",
    "                return \"IMPOSSIBLE\"\n",
    "            res.append(line[i])\n",
    "            res.append(line[j])\n",
    "        else:\n",
    "            res.append(line[i])\n",
    "            if res[-1][0] == res[0][0]:\n",
    "                return \"IMPOSSIBLE\"\n",
    "\n",
    "    for i in range(0, len(res)):\n",
    "        assert res[i][0] != res[(i + 1) % len(res)][0]\n",
    "\n",
    "    return ''.join(_[1] for _ in res)\n",
    "\n",
    "\n",
    "def solve(data):\n",
    "    count = data['count']\n",
    "    n, c0, c01, c1, c12, c2, c02 = count\n",
    "    p0, p01, p1, p12, p2, p02 = \"ROYGBV\"\n",
    "\n",
    "    if c0 + c12 == n:\n",
    "        if c0 == c12:\n",
    "            return ''.join([p0 + p12] * c0)\n",
    "        else:\n",
    "            return \"IMPOSSIBLE\"\n",
    "\n",
    "    if c1 + c02 == n:\n",
    "        if c1 == c02:\n",
    "            return ''.join([p1 + p02] * c1)\n",
    "        else:\n",
    "            return \"IMPOSSIBLE\"\n",
    "\n",
    "    if c2 + c01 == n:\n",
    "        if c2 == c01:\n",
    "            return ''.join([p1 + p02] * c2)\n",
    "        else:\n",
    "            return \"IMPOSSIBLE\"\n",
    "\n",
    "    if ((c0 == 0 or c0 >= c12 + 1) and (c1 == 0 or c1 >= c02 + 1) and\n",
    "        (c2 == 0 or c2 >= c01 + 1)):\n",
    "        r0, r1, r2 = [], [], []\n",
    "        if c0 > 0:\n",
    "            r0.extend([p12.join([p0] * (c12 + 1))])\n",
    "            r0.extend([p0] * (c0 - (c12 + 1)))\n",
    "            \n",
    "        if c1 > 0:\n",
    "            r1.extend([p02.join([p1] * (c02 + 1))])\n",
    "            r1.extend([p1] * (c1 - (c02 + 1)))\n",
    "            \n",
    "        if c2 > 0:\n",
    "            r2.extend([p01.join([p2] * (c01 + 1))])\n",
    "            r2.extend([p2] * (c2 - (c01 + 1)))\n",
    "        \n",
    "        r = [r0, r1, r2]\n",
    "        return sub_solve(r)\n",
    "    else:\n",
    "        return \"IMPOSSIBLE\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-22T13:34:57.638838-04:00",
     "start_time": "2017-04-22T13:34:57.634976"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'YBYBYB'"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solve({'count':[6, 0, 0, 3, 0, 3, 0]})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-22T13:34:58.513265-04:00",
     "start_time": "2017-04-22T13:34:58.475900"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'count': [3, 1, 0, 2, 0, 0, 0]}\n",
      "Case #2: IMPOSSIBLE\n",
      "{'count': [5, 3, 0, 1, 0, 1, 0]}\n",
      "Case #4: IMPOSSIBLE\n",
      "{'count': [564, 138, 0, 314, 0, 112, 0]}\n",
      "Case #6: IMPOSSIBLE\n",
      "{'count': [411, 155, 0, 226, 0, 30, 0]}\n",
      "Case #9: IMPOSSIBLE\n",
      "{'count': [21, 18, 0, 1, 0, 2, 0]}\n",
      "Case #14: IMPOSSIBLE\n",
      "{'count': [514, 4, 0, 509, 0, 1, 0]}\n",
      "Case #19: IMPOSSIBLE\n",
      "{'count': [257, 0, 0, 0, 0, 257, 0]}\n",
      "Case #22: IMPOSSIBLE\n",
      "{'count': [3, 2, 0, 1, 0, 0, 0]}\n",
      "Case #34: IMPOSSIBLE\n",
      "{'count': [999, 500, 0, 249, 0, 250, 0]}\n",
      "Case #40: IMPOSSIBLE\n",
      "{'count': [4, 0, 0, 3, 0, 1, 0]}\n",
      "Case #48: IMPOSSIBLE\n",
      "{'count': [830, 180, 0, 504, 0, 146, 0]}\n",
      "Case #50: IMPOSSIBLE\n",
      "{'count': [1000, 0, 0, 501, 0, 499, 0]}\n",
      "Case #52: IMPOSSIBLE\n",
      "{'count': [658, 19, 0, 75, 0, 564, 0]}\n",
      "Case #56: IMPOSSIBLE\n",
      "{'count': [999, 500, 0, 0, 0, 499, 0]}\n",
      "Case #58: IMPOSSIBLE\n",
      "{'count': [984, 12, 0, 565, 0, 407, 0]}\n",
      "Case #74: IMPOSSIBLE\n",
      "{'count': [5, 3, 0, 0, 0, 2, 0]}\n",
      "Case #84: IMPOSSIBLE\n",
      "{'count': [643, 557, 0, 51, 0, 35, 0]}\n",
      "Case #88: IMPOSSIBLE\n",
      "{'count': [3, 3, 0, 0, 0, 0, 0]}\n",
      "Case #90: IMPOSSIBLE\n",
      "{'count': [288, 30, 0, 9, 0, 249, 0]}\n",
      "Case #91: IMPOSSIBLE\n"
     ]
    }
   ],
   "source": [
    "\n",
    "with open(output_file, 'w') as fout: \n",
    "    for t, data in enumerate(datas):\n",
    "        res = solve(data)\n",
    "        if res == \"IMPOSSIBLE\":\n",
    "            print(data)\n",
    "            print('Case #%d: %s' % (t + 1, res))\n",
    "        print('Case #%d: %s' % (t + 1, res), file=fout)"
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
   "execution_count": 73,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2017-04-22T13:35:03.797153-04:00",
     "start_time": "2017-04-22T13:35:03.759470"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'count': [3, 1, 0, 2, 0, 0, 0]}\n",
      "Case #2: IMPOSSIBLE\n",
      "{'count': [5, 3, 0, 1, 0, 1, 0]}\n",
      "Case #4: IMPOSSIBLE\n",
      "{'count': [564, 138, 0, 314, 0, 112, 0]}\n",
      "Case #6: IMPOSSIBLE\n",
      "{'count': [411, 155, 0, 226, 0, 30, 0]}\n",
      "Case #9: IMPOSSIBLE\n",
      "{'count': [21, 18, 0, 1, 0, 2, 0]}\n",
      "Case #14: IMPOSSIBLE\n",
      "{'count': [514, 4, 0, 509, 0, 1, 0]}\n",
      "Case #19: IMPOSSIBLE\n",
      "{'count': [257, 0, 0, 0, 0, 257, 0]}\n",
      "Case #22: IMPOSSIBLE\n",
      "{'count': [3, 2, 0, 1, 0, 0, 0]}\n",
      "Case #34: IMPOSSIBLE\n",
      "{'count': [999, 500, 0, 249, 0, 250, 0]}\n",
      "Case #40: IMPOSSIBLE\n",
      "{'count': [4, 0, 0, 3, 0, 1, 0]}\n",
      "Case #48: IMPOSSIBLE\n",
      "{'count': [830, 180, 0, 504, 0, 146, 0]}\n",
      "Case #50: IMPOSSIBLE\n",
      "{'count': [1000, 0, 0, 501, 0, 499, 0]}\n",
      "Case #52: IMPOSSIBLE\n",
      "{'count': [658, 19, 0, 75, 0, 564, 0]}\n",
      "Case #56: IMPOSSIBLE\n",
      "{'count': [999, 500, 0, 0, 0, 499, 0]}\n",
      "Case #58: IMPOSSIBLE\n",
      "{'count': [984, 12, 0, 565, 0, 407, 0]}\n",
      "Case #74: IMPOSSIBLE\n",
      "{'count': [5, 3, 0, 0, 0, 2, 0]}\n",
      "Case #84: IMPOSSIBLE\n",
      "{'count': [643, 557, 0, 51, 0, 35, 0]}\n",
      "Case #88: IMPOSSIBLE\n",
      "{'count': [3, 3, 0, 0, 0, 0, 0]}\n",
      "Case #90: IMPOSSIBLE\n",
      "{'count': [288, 30, 0, 9, 0, 249, 0]}\n",
      "Case #91: IMPOSSIBLE\n"
     ]
    }
   ],
   "source": [
    "with open(output_file, 'w') as fout: \n",
    "    for t, data in enumerate(datas):\n",
    "        res = solve(data)\n",
    "        if res == \"IMPOSSIBLE\":\n",
    "            print(data)\n",
    "            print('Case #%d: %s' % (t + 1, res))\n",
    "        print('Case #%d: %s' % (t + 1, res), file=fout)"
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
