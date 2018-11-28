{
 "metadata": {
  "name": "",
  "signature": "sha256:154dca9ba62c8360c8b21f8718b7124d2acb7c70937c46ef0ba4f39442ea71ee"
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
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "!ls"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "A-sample.in              A-small-attempt1.in      Mushroom Monster.ipynb   mushroom1.out            pans_large.out\r\n",
        "A-small-attempt0.in      Inifinite Pancakes.ipynb mushroom.out             mushroom11.out\r\n"
       ]
      }
     ],
     "prompt_number": 99
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "lines = file('A-small-attempt3.in', \"r\").readlines()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 132
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "output = file('mushroom3.out', \"w\")\n",
      "for case, line in enumerate(lines[2::2]):\n",
      "    arr = [int(i) for i in line.strip().split()]\n",
      "    npm = np.array(arr)\n",
      "    meth1 = sum([i for i in (npm - np.roll(npm, -1))[:-1] if i>0])\n",
      "    #rate = -1* min((npm - np.roll(npm, 1))[1:])\n",
      "    rate = max([i for i in (npm - np.roll(npm, -1))[:-1] if i >= 0])\n",
      "    meth2 = sum([min(i, rate) for i in npm][:-1])\n",
      "    \n",
      "    text = \"Case #%i: %i %i\" % ( case + 1, meth1, meth2)\n",
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
        "Case #1: 15 25\n",
        "Case #2: 0 0\n",
        "Case #3: 81 567\n",
        "Case #4: 181 244\n",
        "Case #5: 0 0\n",
        "Case #6: 500 500\n",
        "Case #7: 100 900\n",
        "Case #8: 75 144\n",
        "Case #9: 74 207\n",
        "Case #10: 114 219\n",
        "Case #11: 82 254\n",
        "Case #12: 192 268\n",
        "Case #13: 141 327\n",
        "Case #14: 93 446\n",
        "Case #15: 91 402\n",
        "Case #16: 111 428\n",
        "Case #17: 194 353\n",
        "Case #18: 115 417\n",
        "Case #19: 167 321\n",
        "Case #20: 157 535\n",
        "Case #21: 124 343\n",
        "Case #22: 236 486\n",
        "Case #23: 139 394\n",
        "Case #24: 163 559\n",
        "Case #25: 189 338\n",
        "Case #26: 187 296\n",
        "Case #27: 142 364\n",
        "Case #28: 245 374\n",
        "Case #29: 198 556\n",
        "Case #30: 169 461\n",
        "Case #31: 76 169\n",
        "Case #32: 175 526\n",
        "Case #33: 193 401\n",
        "Case #34: 154 406\n",
        "Case #35: 128 349\n",
        "Case #36: 180 329\n",
        "Case #37: 177 528\n",
        "Case #38: 168 374\n",
        "Case #39: 179 375\n",
        "Case #40: 189 422\n",
        "Case #41: 144 388\n",
        "Case #42: 159 455\n",
        "Case #43: 130 404\n",
        "Case #44: 124 319\n",
        "Case #45: 138 376\n",
        "Case #46: 113 380\n",
        "Case #47: 126 363\n",
        "Case #48: 153 302\n",
        "Case #49: 92 232\n",
        "Case #50: 218 506\n",
        "Case #51: 153 419\n",
        "Case #52: 200 432\n",
        "Case #53: 173 362\n",
        "Case #54: 165 435\n",
        "Case #55: 193 420\n",
        "Case #56: 119 419\n",
        "Case #57: 169 299\n",
        "Case #58: 219 337\n",
        "Case #59: 206 329\n",
        "Case #60: 118 287\n",
        "Case #61: 105 350\n",
        "Case #62: 157 464\n",
        "Case #63: 199 354\n",
        "Case #64: 177 370\n",
        "Case #65: 163 403\n",
        "Case #66: 104 346\n",
        "Case #67: 143 350\n",
        "Case #68: 153 450\n",
        "Case #69: 115 524\n",
        "Case #70: 222 394\n",
        "Case #71: 85 177\n",
        "Case #72: 120 371\n",
        "Case #73: 204 349\n",
        "Case #74: 128 314\n",
        "Case #75: 243 563\n",
        "Case #76: 124 365\n",
        "Case #77: 109 444\n",
        "Case #78: 140 270\n",
        "Case #79: 106 397\n",
        "Case #80: 162 423\n",
        "Case #81: 129 456\n",
        "Case #82: 95 290\n",
        "Case #83: 154 396\n",
        "Case #84: 172 306\n",
        "Case #85: 189 438\n",
        "Case #86: 162 293\n",
        "Case #87: 251 443\n",
        "Case #88: 187 505\n",
        "Case #89: 141 468\n",
        "Case #90: 163 371\n",
        "Case #91: 123 527\n",
        "Case #92: 127 324\n",
        "Case #93: 259 458\n",
        "Case #94: 174 371\n",
        "Case #95: 230 361\n",
        "Case #96: 211 358\n",
        "Case #97: 150 408\n",
        "Case #98: 72 370\n",
        "Case #99: 185 359\n",
        "Case #100: 226 468\n"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "mushrooms =  [10, 5, 15, 5]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 59
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "npm = np.array(mushrooms)"
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
      "sum([i for i in (npm - np.roll(npm, 1))[:-1] if i>0])"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 61,
       "text": [
        "15"
       ]
      }
     ],
     "prompt_number": 61
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "rate = -1* min((npm - np.roll(npm, 1))[1:])"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "npm - np.roll(npm, 1)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 64,
       "text": [
        "array([  5,  -5,  10, -10])"
       ]
      }
     ],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "sum([min(i, rate) for i in npm][:-1])"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 66,
       "text": [
        "25"
       ]
      }
     ],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "line = \"45 83 51 23 0 0 13 73 46 78\"\n",
      "#line = \"81 81 81 81 81 81 81 0\"\n",
      "case = 0\n",
      "\n",
      "arr = [int(i) for i in line.strip().split()]\n",
      "npm = np.array(arr)\n",
      "meth1 = sum([i for i in (npm - np.roll(npm, -1))[:-1] if i>0])\n",
      "rate = max([i for i in (npm - np.roll(npm, -1))[:-1] if i >= 0])\n",
      "meth2 = sum([min(i, rate) for i in npm][:-1])\n",
      "\n",
      "text = \"Case #%i: %i %i\" % ( case + 1, meth1, meth2)\n",
      "print text"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "Case #1: 110 196\n"
       ]
      }
     ],
     "prompt_number": 130
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "(npm - np.roll(npm, -1))[:-1]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 128,
       "text": [
        "array([-45, -38,  32,  28,  23,   0, -13, -60,  27, -32])"
       ]
      }
     ],
     "prompt_number": 128
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "np.roll(npm, -1)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 88,
       "text": [
        "array([83, 51, 23,  0,  0, 13, 73, 46, 78, 45])"
       ]
      }
     ],
     "prompt_number": 88
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "(npm - np.roll(npm, -1))[:-1]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 94,
       "text": [
        "array([-38,  32,  28,  23,   0, -13, -60,  27, -32])"
       ]
      }
     ],
     "prompt_number": 94
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "max([i for i in (npm - np.roll(npm, -1))[:-1] if i >= 0])"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 95,
       "text": [
        "[32, 28, 23, 0, 27]"
       ]
      }
     ],
     "prompt_number": 95
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