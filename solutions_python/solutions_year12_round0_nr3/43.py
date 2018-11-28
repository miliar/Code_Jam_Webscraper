{
 "metadata": {
  "name": "C"
 },
 "nbformat": 3,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": true,
     "input": [
      "def readline_ints():",
      "    return [int(num) for num in fin.readline().strip().split()]"
     ],
     "language": "python",
     "outputs": [],
     "prompt_number": 1
    },
    {
     "cell_type": "code",
     "collapsed": true,
     "input": [
      "def count_recycled_pairs(A, B):",
      "    allnums = {str(i) for i in range(A, B+1)}",
      "    digitpos = list(range(len(str(A))))",
      "    pairs = 0",
      "    while allnums:",
      "        base = allnums.pop()",
      "        group = {base[i:]+base[:i] for i in digitpos}",
      "        ngroup = len(group & allnums) + 1  # +1 because we already popped one number",
      "        pairs += (ngroup*(ngroup-1))//2",
      "        allnums -= group",
      "    ",
      "    return pairs"
     ],
     "language": "python",
     "outputs": [],
     "prompt_number": 4
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "# Update this with the filename",
      "fname = \"C-large\"",
      "with open(fname+\".in\",\"r\") as fin, open(fname+\".out\",\"w\") as fout:",
      "",
      "    numcases = readline_ints()[0]",
      "    print(numcases, \"cases\")",
      "    ",
      "    for caseno in range(1, numcases+1):",
      "        # Code goes here",
      "        A, B = readline_ints()",
      "        print(A, B)",
      "        result = count_recycled_pairs(A, B)",
      "        ",
      "        outstr = \"Case #%d: %d\" % (caseno, result)",
      "        fout.write(outstr + \"\\n\")",
      "        print(outstr)"
     ],
     "language": "python",
     "outputs": [],
     "prompt_number": 8
    }
   ]
  }
 ]
}