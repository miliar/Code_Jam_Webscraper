{
 "metadata": {
  "name": "",
  "signature": "sha256:cb7a856b177ecc961c44a1b1e64efd45cf06baf3c91128dc084c00d26dc74e45"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Question: what is the minimum number of people to invite for a full ovation?"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def sol(input_string):\n",
      "    s_max, people_string = input_string.split(' ')\n",
      "    people = [int(digit) for digit in people_string]\n",
      "    s_i = np.arange(int(s_max) + 1)\n",
      "    people_standing = 0\n",
      "    invited_friends = []\n",
      "    for group, shyness in zip(people, s_i):\n",
      "        if people_standing < shyness:\n",
      "            friends_needed = shyness - people_standing\n",
      "            invited_friends.append(friends_needed)\n",
      "            people_standing += friends_needed\n",
      "        people_standing += group\n",
      "\n",
      "    return sum(invited_friends)\n",
      "    "
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
      "sol(\"4 11111\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 16,
       "text": [
        "0"
       ]
      }
     ],
     "prompt_number": 16
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "sol(\"1 09\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 17,
       "text": [
        "1"
       ]
      }
     ],
     "prompt_number": 17
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "sol(\"5 110011\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 18,
       "text": [
        "2"
       ]
      }
     ],
     "prompt_number": 18
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "sol(\"0 1\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "0"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "%%file probA_example.in\n",
      "4\n",
      "4 11111\n",
      "1 09\n",
      "5 110011\n",
      "0 1"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "Overwriting probA_example.in\n"
       ]
      }
     ],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def handle_input_file(in_filename, out_filename):\n",
      "    lines = open(in_filename).readlines()\n",
      "    with open(out_filename, 'w') as f:\n",
      "        for i, line in zip(range(int(lines[0].strip())), lines[1:]):\n",
      "            print(\"Case #{0}: {1}\".format(i + 1, sol(line.strip())), file=f)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 38
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "handle_input_file(\"probA_example.in\", \"probA_example.out\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 39
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "!cat probA_example.out"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "Case #1: 0\r\n",
        "Case #2: 1\r\n",
        "Case #3: 2\r\n",
        "Case #4: 0\r\n"
       ]
      }
     ],
     "prompt_number": 40
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "handle_input_file(\"probA-small-attempt0.in.txt\", \"probA-small-attempt0.out\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 41
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "!cat probA-small-attempt0.out"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "Case #1: 0\r\n",
        "Case #2: 0\r\n",
        "Case #3: 4\r\n",
        "Case #4: 0\r\n",
        "Case #5: 1\r\n",
        "Case #6: 1\r\n",
        "Case #7: 6\r\n",
        "Case #8: 1\r\n",
        "Case #9: 0\r\n",
        "Case #10: 4\r\n",
        "Case #11: 0\r\n",
        "Case #12: 0\r\n",
        "Case #13: 0\r\n",
        "Case #14: 1\r\n",
        "Case #15: 0\r\n",
        "Case #16: 0\r\n",
        "Case #17: 0\r\n",
        "Case #18: 0\r\n",
        "Case #19: 0\r\n",
        "Case #20: 1\r\n",
        "Case #21: 0\r\n",
        "Case #22: 1\r\n",
        "Case #23: 0\r\n",
        "Case #24: 3\r\n",
        "Case #25: 0\r\n",
        "Case #26: 0\r\n",
        "Case #27: 2\r\n",
        "Case #28: 0\r\n",
        "Case #29: 0\r\n",
        "Case #30: 6\r\n",
        "Case #31: 6\r\n",
        "Case #32: 0\r\n",
        "Case #33: 2\r\n",
        "Case #34: 0\r\n",
        "Case #35: 0\r\n",
        "Case #36: 0\r\n",
        "Case #37: 5\r\n",
        "Case #38: 0\r\n",
        "Case #39: 0\r\n",
        "Case #40: 0\r\n",
        "Case #41: 0\r\n",
        "Case #42: 4\r\n",
        "Case #43: 2\r\n",
        "Case #44: 0\r\n",
        "Case #45: 4\r\n",
        "Case #46: 2\r\n",
        "Case #47: 0\r\n",
        "Case #48: 3\r\n",
        "Case #49: 1\r\n",
        "Case #50: 0\r\n",
        "Case #51: 0\r\n",
        "Case #52: 0\r\n",
        "Case #53: 2\r\n",
        "Case #54: 6\r\n",
        "Case #55: 0\r\n",
        "Case #56: 0\r\n",
        "Case #57: 4\r\n",
        "Case #58: 5\r\n",
        "Case #59: 5\r\n",
        "Case #60: 0\r\n",
        "Case #61: 0\r\n",
        "Case #62: 2\r\n",
        "Case #63: 3\r\n",
        "Case #64: 6\r\n",
        "Case #65: 1\r\n",
        "Case #66: 0\r\n",
        "Case #67: 0\r\n",
        "Case #68: 0\r\n",
        "Case #69: 0\r\n",
        "Case #70: 0\r\n",
        "Case #71: 0\r\n",
        "Case #72: 0\r\n",
        "Case #73: 0\r\n",
        "Case #74: 1\r\n",
        "Case #75: 1\r\n",
        "Case #76: 0\r\n",
        "Case #77: 0\r\n",
        "Case #78: 0\r\n",
        "Case #79: 0\r\n",
        "Case #80: 1\r\n",
        "Case #81: 0\r\n",
        "Case #82: 0\r\n",
        "Case #83: 0\r\n",
        "Case #84: 0\r\n",
        "Case #85: 0\r\n",
        "Case #86: 0\r\n",
        "Case #87: 2\r\n",
        "Case #88: 0\r\n",
        "Case #89: 0\r\n",
        "Case #90: 1\r\n",
        "Case #91: 6\r\n",
        "Case #92: 0\r\n",
        "Case #93: 1\r\n",
        "Case #94: 4\r\n",
        "Case #95: 0\r\n",
        "Case #96: 0\r\n",
        "Case #97: 0\r\n",
        "Case #98: 0\r\n",
        "Case #99: 0\r\n",
        "Case #100: 0\r\n"
       ]
      }
     ],
     "prompt_number": 42
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Large input:"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "handle_input_file(\"probA-large.in.txt\", \"probA-large.out\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 43
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