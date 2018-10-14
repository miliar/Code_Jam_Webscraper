{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# imports\n",
    "import numpy as np # http://www.numpy.org/\n",
    "import math # https://docs.python.org/2/library/math.html\n",
    "import itertools as it # https://docs.python.org/2/library/itertools.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "basepath = '/home/epg/halde/codejam/2017/1B/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "testset = 'A-large'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def do_solve(D, N, KS):\n",
    "    min_durations = [float(D-Ki)/Si for Ki, Si in KS]\n",
    "    \n",
    "    return D/max(min_durations)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 101.000000\n",
      "Case #2: 100.000000\n",
      "Case #3: 20000.000000\n",
      "Case #4: 321.576670\n",
      "Case #5: 25192.779222\n",
      "Case #6: 1000000000.000000\n",
      "Case #7: 1.025646\n",
      "Case #8: 10714.658287\n",
      "Case #9: 6884.257083\n",
      "Case #10: 1946.708888\n",
      "Case #11: 14284.024942\n",
      "Case #12: 33060.198809\n",
      "Case #13: 34599.492483\n",
      "Case #14: 25444.826870\n",
      "Case #15: 3650.916064\n",
      "Case #16: 1000000000.000000\n",
      "Case #17: 9349.420463\n",
      "Case #18: 7236.773423\n",
      "Case #19: 3125.116124\n",
      "Case #20: 3949.554512\n",
      "Case #21: 17180.659780\n",
      "Case #22: 7565.736095\n",
      "Case #23: 10953.397857\n",
      "Case #24: 1991.400173\n",
      "Case #25: 3072.788290\n",
      "Case #26: 428779.942490\n",
      "Case #27: 39825.027297\n",
      "Case #28: 3326.924238\n",
      "Case #29: 500.000000\n",
      "Case #30: 4751.697745\n",
      "Case #31: 11293.780484\n",
      "Case #32: 2.025000\n",
      "Case #33: 1014.708683\n",
      "Case #34: 2.000000\n",
      "Case #35: 12635.710476\n",
      "Case #36: 1457.278787\n",
      "Case #37: 4988.899702\n",
      "Case #38: 4342.187973\n",
      "Case #39: 9963.908966\n",
      "Case #40: 111440.659552\n",
      "Case #41: 30163.549817\n",
      "Case #42: 2016.030645\n",
      "Case #43: 3543.209909\n",
      "Case #44: 15942.893982\n",
      "Case #45: 10000.001000\n",
      "Case #46: 206760.535536\n",
      "Case #47: 276.265894\n",
      "Case #48: 31188.535518\n",
      "Case #49: 9221.647319\n",
      "Case #50: 8261.337702\n",
      "Case #51: 2998.626909\n",
      "Case #52: 17971.033082\n",
      "Case #53: 1.000000\n",
      "Case #54: 5639.607472\n",
      "Case #55: 14272.607843\n",
      "Case #56: 55653.686989\n",
      "Case #57: 13069.986637\n",
      "Case #58: 5066.492067\n",
      "Case #59: 2.000000\n",
      "Case #60: 27305.726806\n",
      "Case #61: 2899.114343\n",
      "Case #62: 43439.335597\n",
      "Case #63: 4694.991102\n",
      "Case #64: 54994.098052\n",
      "Case #65: 10000.000010\n",
      "Case #66: 6075.814161\n",
      "Case #67: 1659.764715\n",
      "Case #68: 5000000.000000\n",
      "Case #69: 10585.787581\n",
      "Case #70: 5900.698912\n",
      "Case #71: 9936.437805\n",
      "Case #72: 95309.041474\n",
      "Case #73: 3476.071765\n",
      "Case #74: 1500000000.000000\n",
      "Case #75: 8315.601198\n",
      "Case #76: 656.462171\n",
      "Case #77: 2684.974757\n",
      "Case #78: 1966.687341\n",
      "Case #79: 365707.878198\n",
      "Case #80: 8049.828862\n",
      "Case #81: 4503.632085\n",
      "Case #82: 8118.117618\n",
      "Case #83: 181007.643945\n",
      "Case #84: 27693.842787\n",
      "Case #85: 26034.464991\n",
      "Case #86: 15370.412942\n",
      "Case #87: 10227.130954\n",
      "Case #88: 13526.409486\n",
      "Case #89: 29218.087993\n",
      "Case #90: 8399.016655\n",
      "Case #91: 7474.735805\n",
      "Case #92: 8708.687144\n",
      "Case #93: 10000000000000.000000\n",
      "Case #94: 6488.848698\n",
      "Case #95: 666666666.666667\n",
      "Case #96: 7690.675820\n",
      "Case #97: 41920.561593\n",
      "Case #98: 3640.462294\n",
      "Case #99: 21735.337555\n"
     ]
    }
   ],
   "source": [
    "with open(basepath + testset + '.in') as fin, open(basepath + testset + '.out', 'w') as fout:\n",
    "    T = int(fin.readline().rstrip('\\r\\n'))\n",
    "    for i in range(T):\n",
    "        D, N = tuple(map(int, fin.readline().rstrip('\\r\\n').split(' ')))\n",
    "        KS = []\n",
    "        for j in range(N):\n",
    "            Ki, Si = tuple(map(float, fin.readline().rstrip('\\r\\n').split(' ')))\n",
    "            KS.append((Ki, Si))\n",
    "            \n",
    "        sol = do_solve(D, N, KS)\n",
    "        \n",
    "        sol_string = 'Case #{}: {}'.format(i+1, '{0:.6f}'.format(sol))\n",
    "        fout.write(sol_string + '\\n')\n",
    "        print(sol_string)"
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
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
