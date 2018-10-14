{
 "metadata": {
  "name": "",
  "signature": "sha256:71851a9c4851cbddff2b4bc78a20db09ffa77583a9f4a4ae24aee40a780b6566"
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
      "import numpy as np"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 3
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "lines = file('B-small-attempt1.in', \"r\").readlines()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 2
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "output = file('s-barbers.out', \"w\")\n",
      "\n",
      "for case, vals in enumerate(zip(lines[1::2], lines[2::2])):\n",
      "    #print vals\n",
      "    your_start = int(vals[0].strip().split()[1])\n",
      "    speed = [int(i) for i in vals[1].strip().split()]\n",
      "    #print your_start\n",
      "    #print speed\n",
      "    seat = simulate(your_start, speed)\n",
      "    \n",
      "    text = \"Case #%i: %i\" % ( case + 1, seat)\n",
      "    print text\n",
      "    output.write(text)\n",
      "    output.write('\\n')\n",
      "output.close()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "Case #1: 1\n",
        "Case #2: 3\n",
        "Case #3: 2\n",
        "Case #4: 5\n",
        "Case #5: 2\n",
        "Case #6: 5\n",
        "Case #7: 1\n",
        "Case #8: 4"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #9: 1\n",
        "Case #10: 3\n",
        "Case #11: 4\n",
        "Case #12: 1\n",
        "Case #13: 1\n",
        "Case #14: 2\n",
        "Case #15: 2\n",
        "Case #16: 1\n",
        "Case #17: 5\n",
        "Case #18: 4\n",
        "Case #19: 3\n",
        "Case #20: 2\n",
        "Case #21: 2\n",
        "Case #22: 3\n",
        "Case #23: 3\n",
        "Case #24: 1\n",
        "Case #25: 5\n",
        "Case #26: 2\n",
        "Case #27: 3\n",
        "Case #28: 2\n",
        "Case #29: 3\n",
        "Case #30: 1\n",
        "Case #31: 2\n",
        "Case #32: 1\n",
        "Case #33: 2\n",
        "Case #34: 2\n",
        "Case #35: 2\n",
        "Case #36: 5\n",
        "Case #37: 1\n",
        "Case #38: 1\n",
        "Case #39: 4\n",
        "Case #40: 1\n",
        "Case #41: 2\n",
        "Case #42: 1\n",
        "Case #43: 3\n",
        "Case #44: 3\n",
        "Case #45: 1\n",
        "Case #46: 1\n",
        "Case #47: 1\n",
        "Case #48: 4\n",
        "Case #49: 2\n",
        "Case #50: 1\n",
        "Case #51: 3\n",
        "Case #52: 2\n",
        "Case #53: 1\n",
        "Case #54: 5\n",
        "Case #55: 1\n",
        "Case #56: 1\n",
        "Case #57: 4\n",
        "Case #58: 2\n",
        "Case #59: 2"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #60: 2\n",
        "Case #61: 2"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #62: 5\n",
        "Case #63: 1"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #64: 3"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #65: 5"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #66: 5\n",
        "Case #67: 1"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #68: 3\n",
        "Case #69: 5"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #70: 5\n",
        "Case #71: 1"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #72: 1\n",
        "Case #73: 1"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #74: 3"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #75: 2\n",
        "Case #76: 2"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #77: 1"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #78: 2"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #79: 3"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #80: 4\n",
        "Case #81: 5\n",
        "Case #82: 4"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #83: 2"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #84: 2\n",
        "Case #85: 4\n",
        "Case #86: 5\n",
        "Case #87: 1\n",
        "Case #88: 3\n",
        "Case #89: 1"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #90: 1"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #91: 5\n",
        "Case #92: 3"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #93: 5\n",
        "Case #94: 4"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #95: 1\n",
        "Case #96: 4"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #97: 3"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n",
        "Case #98: 2\n",
        "Case #99: 5\n",
        "Case #100: 4"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n"
       ]
      }
     ],
     "prompt_number": 6
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "your_start = 4\n",
      "speed = [10, 5]\n",
      "your_start = 448257424\n",
      "speed = [1, 2, 3, 4, 5]\n",
      "\n",
      "your_start = 8\n",
      "speed = [4, 2, 1]\n",
      "barbers = len(speed)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def bigleap(your_start, speed):\n",
      "    nscd = np.product(np.unique(speed))\n",
      "    bigstep = sum(nscd / speed)\n",
      "    rem = your_start % bigstep\n",
      "    if rem ==0:\n",
      "        return bigstep\n",
      "    else:\n",
      "        return rem\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 5
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "bigstep = sum(nscd / speed)"
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
      "np.product(np.unique(speed))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 41,
       "text": [
        "8"
       ]
      }
     ],
     "prompt_number": 41
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "bigleap(your_start, speed)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 40,
       "text": [
        "11"
       ]
      }
     ],
     "prompt_number": 40
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ahead = your_start\n",
      "progress = np.array([0]* barbers)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 17
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def simulate(your_start, speed):\n",
      "    \n",
      "    barbers = len(speed)\n",
      "    ahead = bigleap(your_start, speed) - 1\n",
      "    #print ahead\n",
      "    progress = np.array([0]* barbers)\n",
      "    \n",
      "    mine = None\n",
      "    while ahead >= 0:\n",
      "        #sit new customers\n",
      "        \n",
      "        for i in xrange(barbers):\n",
      "            if progress[i] == 0:\n",
      "                if ahead > 0:\n",
      "                    #print \"%s sits in seat %s\" % (your_start-ahead, i)\n",
      "                    ahead -= 1\n",
      "                    progress[i]=speed[i]\n",
      "                else:\n",
      "                    #print \"you sits in seat %s\" % ( i)\n",
      "                    mine = i+1\n",
      "                    break\n",
      "        if mine != None:\n",
      "            break\n",
      "        #print \"after sitting\"\n",
      "        #print progress\n",
      "        #eject customers\n",
      "        advancement = min(progress)\n",
      "        progress = progress - advancement\n",
      "        #print \"after progress\"\n",
      "        #print progress\n",
      "    return mine"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 4
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "np.array([1,2,3,0]) - 2"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 3,
       "text": [
        "array([-1,  0,  1, -2])"
       ]
      }
     ],
     "prompt_number": 3
    }
   ],
   "metadata": {}
  }
 ]
}