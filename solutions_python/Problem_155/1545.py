{
 "metadata": {
  "name": ""
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "with open(\"input_A.txt\") as iFile:\n",
      "    T = int(next(iFile).strip())\n",
      "    res = []\n",
      "    for i in range(T):\n",
      "        line = next(iFile).strip()\n",
      "        digits = map(int,line.split(' ')[1])\n",
      "        res.append(added_people(digits))\n",
      "with open(\"output_A.txt\",'w') as oFile:\n",
      "    for i, val in enumerate(res):\n",
      "        oFile.write(\"Case #{}: {}\\n\".format(i+1,val))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def added_people(digits):\n",
      "    sum = 0\n",
      "    added = 0\n",
      "    for i,n in enumerate(digits):\n",
      "        if sum < i:\n",
      "            added += i-sum\n",
      "            sum += i-sum\n",
      "        sum += n\n",
      "    return added        "
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}