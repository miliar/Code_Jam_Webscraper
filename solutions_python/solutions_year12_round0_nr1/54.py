{
 "metadata": {
  "name": "GCJ Template"
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
     "prompt_number": 3
    },
    {
     "cell_type": "code",
     "collapsed": true,
     "input": [
      "goog2plain = {' ': ' ',",
      "              'y': 'a',",
      "              'n': 'b',",
      "              'f': 'c',",
      "              'i': 'd',",
      "              'c': 'e',",
      "              'w': 'f',",
      "              'l': 'g',",
      "              'b': 'h',",
      "              'k': 'i',",
      "              'u': 'j',",
      "              'o': 'k',",
      "              'm': 'l',",
      "              'x': 'm',",
      "              's': 'n',",
      "              'e': 'o',",
      "              'v': 'p',",
      "              'z': 'q',",
      "              'p': 'r',",
      "              'd': 's',",
      "              'r': 't',",
      "              'j': 'u',",
      "              'g': 'v',",
      "              't': 'w',",
      "              'h': 'x',",
      "              'a': 'y',",
      "              'q': 'z',",
      "              }"
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
      "fname = \"A-small-attempt0\"",
      "with open(fname+\".in\",\"r\") as fin, open(fname+\".out\",\"w\") as fout:",
      "",
      "    numcases = readline_ints()[0]",
      "    print(numcases, \"cases\")",
      "    ",
      "    for caseno in range(1, numcases+1):",
      "        # Code goes here",
      "        googlerese = fin.readline().strip()",
      "        result = \"\".join(goog2plain[c] for c in googlerese)",
      "        outstr = \"Case #%d: %s\" % (caseno, result)",
      "        fout.write(outstr + \"\\n\")",
      "        print(outstr)"
     ],
     "language": "python",
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "3 cases",
        "Case #1: our language is impossible to understand",
        "Case #2: there are twenty six factorial possibilities",
        "Case #3: so it is okay if you want to just give up"
       ]
      }
     ],
     "prompt_number": 5
    },
    {
     "cell_type": "code",
     "collapsed": true,
     "input": [],
     "language": "python",
     "outputs": []
    }
   ]
  }
 ]
}