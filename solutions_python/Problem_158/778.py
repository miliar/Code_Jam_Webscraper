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
      "with open(\"D-small-attempt1.in\") as iFile:\n",
      "    T = int(next(iFile).strip())\n",
      "    res = []\n",
      "    for _ in range(T):\n",
      "        X,R,C = map(int,next(iFile).strip().split(' '))\n",
      "        res.append(winner(X,R,C))\n",
      "with open(\"output_D.txt\",'w') as oFile:\n",
      "    for i,r in enumerate(res):\n",
      "        oFile.write(\"Case #{}: {}\\n\".format(i+1,r))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def winner(X,R,C):\n",
      "    R,C = min(R,C), max(R,C)\n",
      "    solvable = (R*C) % X == 0 and X <= R*C\n",
      "    if R == 1:\n",
      "        forceOverlap = (X >= 3)\n",
      "        return \"RICHARD\" if forceOverlap or not solvable else \"GABRIEL\"\n",
      "    else:\n",
      "        forceOverlap = (X >= R+R) # l-shaped omino with edges of length R and R+1\n",
      "        Hole = (7 <= X) # 7pc+ x-omino can form a o -> Hole\n",
      "        return \"RICHARD\" if forceOverlap or Hole or not solvable else \"GABRIEL\""
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 27
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