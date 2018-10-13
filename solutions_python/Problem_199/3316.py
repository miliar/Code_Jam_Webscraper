{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Problem A. Oversized Pancake Flipper"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# load the file\n",
    "fileDir = \"C:\\\\codejam2017\\\\\"\n",
    "fileName = \"A-small-attempt1.in\"\n",
    "\n",
    "with open(fileDir+fileName,'r') as f:\n",
    "    cases=int(f.readline())\n",
    "    lines=f.readlines()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "spy = False\n",
    "\n",
    "soluce = []\n",
    "currentRow = 0\n",
    "for case in range(cases):\n",
    "    if spy: print(\"\\t CASE#\"+str(case))\n",
    "    soluce.append(\"Case #\" + str(case+1) + \": \")\n",
    "    pancakes, K = lines[case].split()\n",
    "    pancakes=list(pancakes)\n",
    "    K = int(K)\n",
    "    \n",
    "    flip = 0\n",
    "    currentPancakes = len(pancakes)-1\n",
    "    keepGoing = True\n",
    "    while keepGoing:\n",
    "        if spy: print(\"before \\t\"+\"\".join(pancakes))\n",
    "        # looking for a pancake to flip\n",
    "        while (currentPancakes>=(K-1)) & (pancakes[currentPancakes]=='+'):\n",
    "            currentPancakes -= 1\n",
    "\n",
    "        if spy: print(\"\\t\"+str(currentPancakes))\n",
    "        if currentPancakes >=K-1:\n",
    "            # we flip K pancakes\n",
    "            flip +=1\n",
    "            for pk in range(currentPancakes-K+1,currentPancakes+1):\n",
    "                if spy:print(pk)\n",
    "                    \n",
    "                if pancakes[pk]=='+':\n",
    "                    pancakes[pk]='-'\n",
    "                else:\n",
    "                    pancakes[pk]='+'\n",
    "            if spy: print(\"after \\t\"+\"\".join(pancakes))\n",
    "            # previous pancake\n",
    "            currentPancakes -=1\n",
    "        else:\n",
    "            keepGoing = False\n",
    "    \n",
    "    if '-' in pancakes:\n",
    "        soluce.append(\"IMPOSSIBLE\")\n",
    "    else:\n",
    "        soluce.append(str(flip))\n",
    "    \n",
    "    soluce.append('\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1:3\n",
      "Case #2:0\n",
      "Case #3:IMPOSSIBLE\n",
      "Case #4:1\n",
      "Case #5:IMPOSSIBLE\n",
      "Case #6:1\n",
      "Case #7:IMPOSSIBLE\n",
      "Case #8:IMPOSSIBLE\n",
      "Case #9:0\n",
      "Case #10:IMPOSSIBLE\n",
      "Case #11:2\n",
      "Case #12:IMPOSSIBLE\n",
      "Case #13:IMPOSSIBLE\n",
      "Case #14:0\n",
      "Case #15:IMPOSSIBLE\n",
      "Case #16:1\n",
      "Case #17:2\n",
      "Case #18:0\n",
      "Case #19:0\n",
      "Case #20:2\n",
      "Case #21:IMPOSSIBLE\n",
      "Case #22:IMPOSSIBLE\n",
      "Case #23:1\n",
      "Case #24:2\n",
      "Case #25:1\n",
      "Case #26:8\n",
      "Case #27:1\n",
      "Case #28:IMPOSSIBLE\n",
      "Case #29:0\n",
      "Case #30:IMPOSSIBLE\n",
      "Case #31:3\n",
      "Case #32:2\n",
      "Case #33:IMPOSSIBLE\n",
      "Case #34:IMPOSSIBLE\n",
      "Case #35:IMPOSSIBLE\n",
      "Case #36:9\n",
      "Case #37:1\n",
      "Case #38:2\n",
      "Case #39:3\n",
      "Case #40:IMPOSSIBLE\n",
      "Case #41:2\n",
      "Case #42:5\n",
      "Case #43:IMPOSSIBLE\n",
      "Case #44:4\n",
      "Case #45:IMPOSSIBLE\n",
      "Case #46:IMPOSSIBLE\n",
      "Case #47:IMPOSSIBLE\n",
      "Case #48:IMPOSSIBLE\n",
      "Case #49:IMPOSSIBLE\n",
      "Case #50:IMPOSSIBLE\n",
      "Case #51:1\n",
      "Case #52:IMPOSSIBLE\n",
      "Case #53:IMPOSSIBLE\n",
      "Case #54:IMPOSSIBLE\n",
      "Case #55:1\n",
      "Case #56:2\n",
      "Case #57:5\n",
      "Case #58:IMPOSSIBLE\n",
      "Case #59:IMPOSSIBLE\n",
      "Case #60:0\n",
      "Case #61:1\n",
      "Case #62:IMPOSSIBLE\n",
      "Case #63:IMPOSSIBLE\n",
      "Case #64:IMPOSSIBLE\n",
      "Case #65:0\n",
      "Case #66:3\n",
      "Case #67:IMPOSSIBLE\n",
      "Case #68:IMPOSSIBLE\n",
      "Case #69:IMPOSSIBLE\n",
      "Case #70:2\n",
      "Case #71:1\n",
      "Case #72:IMPOSSIBLE\n",
      "Case #73:IMPOSSIBLE\n",
      "Case #74:1\n",
      "Case #75:IMPOSSIBLE\n",
      "Case #76:1\n",
      "Case #77:2\n",
      "Case #78:IMPOSSIBLE\n",
      "Case #79:IMPOSSIBLE\n",
      "Case #80:3\n",
      "Case #81:IMPOSSIBLE\n",
      "Case #82:IMPOSSIBLE\n",
      "Case #83:IMPOSSIBLE\n",
      "Case #84:1\n",
      "Case #85:IMPOSSIBLE\n",
      "Case #86:IMPOSSIBLE\n",
      "Case #87:IMPOSSIBLE\n",
      "Case #88:IMPOSSIBLE\n",
      "Case #89:1\n",
      "Case #90:IMPOSSIBLE\n",
      "Case #91:IMPOSSIBLE\n",
      "Case #92:IMPOSSIBLE\n",
      "Case #93:IMPOSSIBLE\n",
      "Case #94:1\n",
      "Case #95:IMPOSSIBLE\n",
      "Case #96:3\n",
      "Case #97:IMPOSSIBLE\n",
      "Case #98:IMPOSSIBLE\n",
      "Case #99:1\n",
      "Case #100:2\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"\".join(soluce))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# Copie la solution dans le fichier resultat.txt\n",
    "with open(fileDir+\"resultat.txt\",'w') as f:\n",
    "    f.write(\"\".join(soluce))"
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
       "'---+-++-'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pancakes"
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
