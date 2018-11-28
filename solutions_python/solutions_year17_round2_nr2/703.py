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
    "#naive"
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
   "execution_count": 52,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(case):\n",
    "    N,R,O,Y,G,B,V = case\n",
    "    N,R,O,Y,G,B,V = int(N),int(R),int(O),int(Y),int(G),int(B),int(V)\n",
    "    \n",
    "    #small set\n",
    "    pal = [R,Y,B]\n",
    "    \n",
    "    #check for impossibility -- \n",
    "    #if any color is greater than the sum of the remaining\n",
    "    if pal[0] > pal[1] + pal[2] or pal[1] > pal[0] + pal[2] or pal[2] > pal[1] + pal[0]:\n",
    "        return \"IMPOSSIBLE\"\n",
    "    \n",
    "    \n",
    "    print pal\n",
    "    print max(pal)\n",
    "    #construct answer\n",
    "    ans = []\n",
    "    ans.append(pal.index(max(pal)))\n",
    "    pal[pal.index(max(pal))] = max(pal)-1\n",
    "    for i in range(1,N):\n",
    "        highColor = pal.index(max(pal))\n",
    "        lowColor = pal.index(min(pal))\n",
    "        midColor = 0\n",
    "        if midColor == lowColor or midColor == highColor:\n",
    "            midColor+=1\n",
    "            \n",
    "        if midColor == lowColor or midColor == highColor:\n",
    "            midColor+=1\n",
    "        \n",
    "        #prefer to place the starting color\n",
    "        if ans[len(ans)-1] != ans[0] and pal[ans[0]] > 0:\n",
    "            ans.append(ans[0])\n",
    "            pal[ans[0]] = pal[ans[0]] - 1\n",
    "        elif ans[len(ans)-1] != highColor:\n",
    "            ans.append(highColor)\n",
    "            pal[highColor] = pal[highColor]-1\n",
    "        elif pal[midColor] > 0:\n",
    "            ans.append(midColor)\n",
    "            pal[midColor] = pal[midColor]-1\n",
    "        else:\n",
    "            ans.append(lowColor)\n",
    "            pal[lowColor] = pal[lowColor]-1\n",
    "            \n",
    "    #convert to letters\n",
    "    ansStr = \"\"\n",
    "    for i in range(0,N):\n",
    "        if ans[i] == 0:\n",
    "            ansStr += 'R'\n",
    "        elif ans[i] == 1:\n",
    "            ansStr += 'Y'\n",
    "        else:\n",
    "            ansStr += 'B'\n",
    "            \n",
    "    if ans[0] == ans[len(ans)-1]:\n",
    "        print \"WHAT\"\n",
    "        \n",
    "    return ansStr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def jam():\n",
    "    f = open(\"B-small-attempt1.in\")\n",
    "    answers = []\n",
    "    f.readline()\n",
    "    count = 1\n",
    "    for case in f:\n",
    "        ans = \"Case #\" + str(count) + \": \"\n",
    "        case = str(case.strip()).split(\" \")\n",
    "\n",
    "        ans = ans + solve(case) + \"\\n\"\n",
    "        count+=1\n",
    "        answers.append(ans)\n",
    "\n",
    "    q = open(\"B-small.out\",'w')\n",
    "    for ans in answers:\n",
    "        q.write(ans)\n",
    "    q.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "collapsed": false,
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 2, 2]\n",
      "2\n",
      "[1, 2, 3]\n",
      "3\n",
      "[8, 25, 23]\n",
      "25\n",
      "[250, 500, 250]\n",
      "500\n",
      "[297, 268, 170]\n",
      "297\n",
      "[134, 114, 220]\n",
      "220\n",
      "[284, 240, 263]\n",
      "284\n",
      "[24, 7, 25]\n",
      "25\n",
      "[49, 425, 408]\n",
      "425\n",
      "[19, 41, 39]\n",
      "41\n",
      "[333, 333, 333]\n",
      "333\n",
      "[106, 285, 341]\n",
      "341\n",
      "[53, 262, 311]\n",
      "311\n",
      "[255, 361, 349]\n",
      "361\n",
      "[49, 13, 41]\n",
      "49\n",
      "[249, 188, 373]\n",
      "373\n",
      "[131, 219, 205]\n",
      "219\n",
      "[71, 126, 120]\n",
      "126\n",
      "[19, 9, 13]\n",
      "19\n",
      "[499, 499, 1]\n",
      "499\n",
      "[500, 0, 500]\n",
      "500\n",
      "[145, 323, 325]\n",
      "325\n",
      "[0, 2, 2]\n",
      "2\n",
      "[61, 43, 42]\n",
      "61\n",
      "[2, 1, 1]\n",
      "2\n",
      "[83, 118, 154]\n",
      "154\n",
      "[465, 493, 38]\n",
      "493\n",
      "[9, 18, 11]\n",
      "18\n",
      "[59, 70, 123]\n",
      "123\n",
      "[1, 1, 1]\n",
      "1\n",
      "[1, 2, 1]\n",
      "2\n",
      "[499, 500, 1]\n",
      "500\n",
      "[24, 17, 39]\n",
      "39\n",
      "[340, 400, 186]\n",
      "400\n",
      "[2, 3, 2]\n",
      "3\n",
      "[316, 116, 364]\n",
      "364\n",
      "[95, 260, 330]\n",
      "330\n",
      "[157, 285, 128]\n",
      "285\n",
      "[95, 131, 82]\n",
      "131\n",
      "[333, 334, 333]\n",
      "334\n",
      "[76, 61, 99]\n",
      "99\n",
      "[67, 376, 394]\n",
      "394\n",
      "[1, 1, 2]\n",
      "2\n",
      "[192, 183, 257]\n",
      "257\n",
      "[284, 259, 258]\n",
      "284\n",
      "[34, 15, 32]\n",
      "34\n",
      "[2, 2, 1]\n",
      "2\n",
      "[82, 18, 69]\n",
      "82\n",
      "[285, 146, 241]\n",
      "285\n",
      "[211, 134, 185]\n",
      "211\n",
      "[370, 337, 69]\n",
      "370\n",
      "[442, 129, 396]\n",
      "442\n",
      "[226, 203, 260]\n",
      "260\n",
      "[2, 0, 2]\n",
      "2\n",
      "[12, 10, 12]\n",
      "12\n",
      "[3, 0, 3]\n",
      "3\n",
      "[122, 80, 147]\n",
      "147\n",
      "[59, 136, 96]\n",
      "136\n",
      "[109, 67, 90]\n",
      "109\n",
      "[33, 33, 42]\n",
      "42\n",
      "[49, 46, 15]\n",
      "49\n",
      "[210, 202, 20]\n",
      "210\n",
      "[48, 160, 123]\n",
      "160\n",
      "[95, 223, 145]\n",
      "223\n",
      "[283, 240, 43]\n",
      "283\n",
      "[172, 207, 51]\n",
      "207\n",
      "[317, 40, 357]\n",
      "357\n",
      "[157, 157, 139]\n",
      "157\n",
      "[277, 268, 231]\n",
      "277\n",
      "[228, 316, 109]\n",
      "316\n",
      "[250, 499, 250]\n",
      "499\n",
      "[316, 72, 370]\n",
      "370\n",
      "[207, 249, 218]\n",
      "249\n",
      "[127, 420, 397]\n",
      "420\n",
      "[127, 140, 76]\n",
      "140\n",
      "[150, 325, 295]\n",
      "325\n",
      "[184, 137, 170]\n",
      "184\n",
      "[245, 300, 84]\n",
      "300\n",
      "[327, 262, 336]\n",
      "336\n",
      "[125, 258, 382]\n",
      "382\n"
     ]
    }
   ],
   "source": [
    "jam()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "a,b,c = int(a),int(b),int(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "q = [a,b,c]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "q.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "q.reverse()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 2, 1]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "q"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "q.index(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'[3, 2, 1]'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str(q)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[184, 130, 292]\n",
      "292\n",
      "WHAT\n",
      "['606', '184', '0', '130', '0', '292', '0']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'BRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBYBRBRYBRYBRYBRYBRYBRYBRYBRYBRYBRYBRYBRYBRYBRYBRYBRYBRYBRYBRYBRYBRYBRYBRYB'"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solve(['606', '184', '0', '130', '0', '292', '0'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'IMPOSSIBLE'"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solve(['3','1','0','2','0','0','0'])"
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
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
