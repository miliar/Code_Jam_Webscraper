{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import heapq"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "l = [4,33,44,11]\n",
    "s = heapq.heappush(l, 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "a = heapq.heappop(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5, 11, 44, 33]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
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
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# IO"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'raw_input' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-13-d885e73a5b2c>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mt\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mraw_input\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mxrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mt\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m     \u001b[0mD\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mN\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mele\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mele\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mraw_input\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m' '\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0mtimes\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mj\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mxrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mN\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'raw_input' is not defined"
     ]
    }
   ],
   "source": [
    "t = int(raw_input())\n",
    "for i in xrange(1, t+1):\n",
    "    D,N = [int(ele) for ele in raw_input().split(' ')]\n",
    "    times = []\n",
    "    for j in xrange(N):\n",
    "        k_j, s_j = [int(ele) for ele in raw_input().split(' ')]\n",
    "        t_j = (D-k_j)/s_j\n",
    "        times.append(t_j)\n",
    "    max_time = max(times)\n",
    "    speed = D/max_time\n",
    "    print('Case #{}: {}'.format(i, speed))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def speed(D,N,K,S):\n",
    "    \n",
    "    t = []\n",
    "    for i in range(N):\n",
    "        t.append((D-K[i]) / S[i])\n",
    "    return round(D/max(t),6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 101.0\n",
      "Case #2: 100.0\n",
      "Case #3: 379.742031\n",
      "Case #4: 1000000000.0\n",
      "Case #5: 3712.912817\n",
      "Case #6: 564.37431\n",
      "Case #7: 159.429959\n",
      "Case #8: 200.002\n",
      "Case #9: 121.476575\n",
      "Case #10: 911.920048\n",
      "Case #11: 2.0\n",
      "Case #12: 1021.430526\n",
      "Case #13: 144.44365\n",
      "Case #14: 840.821311\n",
      "Case #15: 10000.00001\n",
      "Case #16: 1953.699343\n",
      "Case #17: 1098.770442\n",
      "Case #18: 2.0\n",
      "Case #19: 1.051364\n",
      "Case #20: 258.288468\n",
      "Case #21: 24.763869\n",
      "Case #22: 1.051364\n",
      "Case #23: 1.052421\n",
      "Case #24: 56.367074\n",
      "Case #25: 403.122078\n",
      "Case #26: 20000.0\n",
      "Case #27: 1665.711402\n",
      "Case #28: 1.051486\n",
      "Case #29: 666666666.666667\n",
      "Case #30: 149.545706\n",
      "Case #31: 5841.453913\n",
      "Case #32: 2250.310481\n",
      "Case #33: 27.615852\n",
      "Case #34: 7267.397519\n",
      "Case #35: 1256.932927\n",
      "Case #36: 144.040253\n",
      "Case #37: 8287.911462\n",
      "Case #38: 10.0\n",
      "Case #39: 50.86828\n",
      "Case #40: 39941.562477\n",
      "Case #41: 1205.82958\n",
      "Case #42: 304298.226993\n",
      "Case #43: 2381.58268\n",
      "Case #44: 22.40405\n",
      "Case #45: 3000.617498\n",
      "Case #46: 859.612281\n",
      "Case #47: 10000000000000.0\n",
      "Case #48: 100000.0\n",
      "Case #49: 1000000000.0\n",
      "Case #50: 4821.340727\n",
      "Case #51: 272.513744\n",
      "Case #52: 32640.40248\n",
      "Case #53: 480.82146\n",
      "Case #54: 251.259906\n",
      "Case #55: 1.052609\n",
      "Case #56: 2466.023734\n",
      "Case #57: 17.904796\n",
      "Case #58: 1010000000.0\n",
      "Case #59: 1639.736\n",
      "Case #60: 16.593336\n",
      "Case #61: 2062.717902\n",
      "Case #62: 1.05215\n",
      "Case #63: 26.24573\n",
      "Case #64: 449.477657\n",
      "Case #65: 2.025\n",
      "Case #66: 1.052299\n",
      "Case #67: 305.046732\n",
      "Case #68: 542.686138\n",
      "Case #69: 226.833604\n",
      "Case #70: 1025.830819\n",
      "Case #71: 1.052133\n",
      "Case #72: 219.8806\n",
      "Case #73: 1.051707\n",
      "Case #74: 97.50838\n",
      "Case #75: 31.415102\n",
      "Case #76: 302.69419\n",
      "Case #77: 1.051685\n",
      "Case #78: 368.570687\n",
      "Case #79: 3028.215652\n",
      "Case #80: 1.0\n",
      "Case #81: 299.593183\n",
      "Case #82: 27.789532\n",
      "Case #83: 97.686007\n",
      "Case #84: 45.777997\n",
      "Case #85: 3545.799452\n",
      "Case #86: 1543.897678\n",
      "Case #87: 326.987776\n",
      "Case #88: 764.776597\n",
      "Case #89: 3113.56485\n",
      "Case #90: 5923.189049\n",
      "Case #91: 734.261201\n",
      "Case #92: 118.159784\n",
      "Case #93: 133.927799\n",
      "Case #94: 8.268848\n",
      "Case #95: 470.710347\n",
      "Case #96: 77.815838\n",
      "Case #97: 44.336082\n",
      "Case #98: 2485.910229\n",
      "Case #99: 47.268746\n",
      "Case #100: 1.052576\n"
     ]
    }
   ],
   "source": [
    "\n",
    "f = open('A-large (1).in','r')\n",
    "sol = open('Solxx_big.out','w')\n",
    "\n",
    "t = int(f.readline()) # read a line with a single integer\n",
    "for i in range(1, t + 1):\n",
    "    D,N = [int(x) for x in f.readline().split(' ')]\n",
    "    K,S = [], []\n",
    "    for en in range(N):\n",
    "        l = [int(x) for x in f.readline().split(' ')]\n",
    "        #print(l)\n",
    "        k,s = l\n",
    "        K.append(k)\n",
    "        S.append(s)\n",
    "    res = speed(D,N,K,S)\n",
    "    print(\"Case #{}: {}\".format(i, res))\n",
    "    sol.writelines(\"Case #{}: {}\\n\".format(i,res))\n",
    "    \n",
    "sol.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [default]",
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
   "version": "3.5.2"
  },
  "nav_menu": {},
  "toc": {
   "navigate_menu": true,
   "number_sections": true,
   "sideBar": true,
   "threshold": 6,
   "toc_cell": false,
   "toc_section_display": "block",
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
