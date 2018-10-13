{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "with open('A-large.in') as f:\n",
    "    data = f.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 101.000000\n",
      "Case #2: 100.000000\n",
      "Case #3: 51.593355\n",
      "Case #4: 401.021296\n",
      "Case #5: 201.719490\n",
      "Case #6: 1.052504\n",
      "Case #7: 297.624639\n",
      "Case #8: 1.000000\n",
      "Case #9: 8178.412004\n",
      "Case #10: 78.002569\n",
      "Case #11: 6615.111419\n",
      "Case #12: 20000.000000\n",
      "Case #13: 4209.945134\n",
      "Case #14: 142.073930\n",
      "Case #15: 1.052382\n",
      "Case #16: 1.052548\n",
      "Case #17: 1.052554\n",
      "Case #18: 2535.043317\n",
      "Case #19: 746.158959\n",
      "Case #20: 311.606744\n",
      "Case #21: 10.000000\n",
      "Case #22: 21.645965\n",
      "Case #23: 125.537370\n",
      "Case #24: 11418.923136\n",
      "Case #25: 1.052632\n",
      "Case #26: 1838.487403\n",
      "Case #27: 412.422644\n",
      "Case #28: 1010000000.000000\n",
      "Case #29: 9188.529571\n",
      "Case #30: 1.052172\n",
      "Case #31: 1651.497222\n",
      "Case #32: 559.115043\n",
      "Case #33: 2.025000\n",
      "Case #34: 409.218776\n",
      "Case #35: 2634.963878\n",
      "Case #36: 40.683938\n",
      "Case #37: 1002.663197\n",
      "Case #38: 2.000000\n",
      "Case #39: 2083.991982\n",
      "Case #40: 33848.367340\n",
      "Case #41: 78.112948\n",
      "Case #42: 500.783442\n",
      "Case #43: 180.466393\n",
      "Case #44: 227.561736\n",
      "Case #45: 424.905907\n",
      "Case #46: 294.612816\n",
      "Case #47: 269.356471\n",
      "Case #48: 403.523221\n",
      "Case #49: 410.510795\n",
      "Case #50: 1000000000.000000\n",
      "Case #51: 52.258113\n",
      "Case #52: 1262.608170\n",
      "Case #53: 827.041416\n",
      "Case #54: 1378.542172\n",
      "Case #55: 286.854947\n",
      "Case #56: 666666666.666667\n",
      "Case #57: 2065.398335\n",
      "Case #58: 48.879456\n",
      "Case #59: 417.969592\n",
      "Case #60: 303.691082\n",
      "Case #61: 251.388070\n",
      "Case #62: 233.733364\n",
      "Case #63: 353.343804\n",
      "Case #64: 137.092797\n",
      "Case #65: 458.164008\n",
      "Case #66: 1319.997119\n",
      "Case #67: 6217.474114\n",
      "Case #68: 1.052249\n",
      "Case #69: 386.833434\n",
      "Case #70: 3824.528352\n",
      "Case #71: 8325.870385\n",
      "Case #72: 1.052576\n",
      "Case #73: 2.000000\n",
      "Case #74: 10000.000010\n",
      "Case #75: 10276.121909\n",
      "Case #76: 839.710232\n",
      "Case #77: 1000000000.000000\n",
      "Case #78: 735.878570\n",
      "Case #79: 731.329519\n",
      "Case #80: 164.785582\n",
      "Case #81: 296.829541\n",
      "Case #82: 10000000000000.000000\n",
      "Case #83: 1.052593\n",
      "Case #84: 1048.917143\n",
      "Case #85: 22100.109669\n",
      "Case #86: 971.561481\n",
      "Case #87: 8430.143341\n",
      "Case #88: 100000.000000\n",
      "Case #89: 1.052476\n",
      "Case #90: 7045.367097\n",
      "Case #91: 1.050525\n",
      "Case #92: 855.955808\n",
      "Case #93: 7228.405367\n",
      "Case #94: 83.152784\n",
      "Case #95: 533.722724\n",
      "Case #96: 3448.729646\n",
      "Case #97: 471.195589\n",
      "Case #98: 2754.240470\n",
      "Case #99: 250.213210\n",
      "Case #100: 200.002000\n",
      "\n"
     ]
    }
   ],
   "source": [
    "lines = data.split('\\n')\n",
    "N = int(lines[0])\n",
    "output = ''\n",
    "ln = 1\n",
    "for i in range(1, N+1):\n",
    "    #print(lines[ln])\n",
    "    d, n = lines[ln].split(' ')\n",
    "    horses = []\n",
    "    for hor in range(int(n)):\n",
    "        #print( ln, hor)\n",
    "        #print(lines[ln+hor+1])\n",
    "        d_loc, sp = lines[ln+hor+1].split(' ')\n",
    "        time = (float(d)-float(d_loc))/float(sp)\n",
    "        horses.append(time)\n",
    "    final = float(d)/max(horses)\n",
    "        #print(\"%.6f\" % final)\n",
    "    ln += int(n) + 1\n",
    "    output += 'Case #' + str(i) + ': ' + str((\"%.6f\" % final)) + '\\n'\n",
    "    #print('Case #' + str(i) + ': ' + ' '.join(res) + '\\n')\n",
    "print(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "out_file = 'B_case_1_large.txt'\n",
    "\n",
    "with open(out_file, 'w') as f:\n",
    "    f.write(output)"
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
 "nbformat_minor": 2
}
