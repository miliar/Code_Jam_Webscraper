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
      "import sys"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 1
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "file_name = 'a_test'\n",
      "\n",
      "fr = open(file_name + '_in')\n",
      "fw = open(file_name + '_out', 'w')\n",
      "\n",
      "testCount = int(fr.readline())\n",
      "for i in range(testCount):\n",
      "    args = fr.readline().split()\n",
      "    maxShyness = int(args[0])\n",
      "    shyness = [0] * (maxShyness + 1)\n",
      "    for j in range(maxShyness + 1):\n",
      "        shyness[j] = int(args[1][j])\n",
      "    \n",
      "    #start of calculation\n",
      "    haveStanding = shyness[0]\n",
      "    needStanding = 0\n",
      "    for j in range(1, maxShyness + 1):\n",
      "        if haveStanding < j and shyness[j] != 0:\n",
      "            needStanding += j - haveStanding\n",
      "            haveStanding = j\n",
      "        haveStanding += shyness[j]\n",
      "    \n",
      "    fw.write('Case #' + str(i + 1) + ': ' + str(needStanding) + '\\n')\n",
      "        \n",
      "    \n",
      "\n",
      "fr.close()\n",
      "fw.close()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 17
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