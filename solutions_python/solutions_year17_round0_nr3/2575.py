{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Problem C. Bathroom Stalls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# load the file\n",
    "fileDir = \"C:\\\\codejam2017\\\\\"\n",
    "fileName = \"C-small-1-attempt0.in\"\n",
    "\n",
    "with open(fileDir+fileName,'r') as f:\n",
    "    cases=int(f.readline())\n",
    "    lines=f.readlines()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "spy = False\n",
    "\n",
    "soluce = []\n",
    "\n",
    "for case in range(cases):\n",
    "    if spy: print(\"CASE#\"+str(case+1))\n",
    "    soluce.append(\"Case #\" + str(case+1) + \": \")\n",
    "    N, K = lines[case].split()\n",
    "    N = int(N)\n",
    "    K = int(K)\n",
    "    \n",
    "    if spy: print(\"\\t N, K\", N, K)\n",
    "    theList = [N]\n",
    "    \n",
    "    for it in range(K-1):\n",
    "        currentMax= max(theList)\n",
    "        idx = theList.index(currentMax)\n",
    "        if currentMax %2 == 0:\n",
    "            theList[idx]= (currentMax-1)//2+1\n",
    "        else:\n",
    "            theList[idx]= (currentMax-1)//2\n",
    "        theList.append((currentMax-1)//2)\n",
    "\n",
    "    currentMax= max(theList)\n",
    "\n",
    "    idx = theList.index(currentMax)\n",
    "    if currentMax %2 == 0:\n",
    "        y= (currentMax-1)//2+1\n",
    "    else:\n",
    "        y= (currentMax-1)//2\n",
    "        \n",
    "    z= (currentMax-1)//2\n",
    "    \n",
    "    if spy: print(\"\\t y, z\", y, z)\n",
    "    soluce.append(str(y))\n",
    "    soluce.append(' ')\n",
    "    soluce.append(str(z))\n",
    "\n",
    "    soluce.append('\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 1 0\n",
      "Case #2: 1 0\n",
      "Case #3: 1 1\n",
      "Case #4: 0 0\n",
      "Case #5: 500 499\n",
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
   "execution_count": 118,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# Copie la solution dans le fichier resultat.txt\n",
    "with open(fileDir+\"resultat.txt\",'w') as f:\n",
    "    f.write(\"\".join(soluce)[:-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1000]\n",
      "500 499\n"
     ]
    }
   ],
   "source": [
    "N=1000\n",
    "k=1\n",
    "\n",
    "theList = [N]\n",
    "for it in range(k-1):\n",
    "    currentMax= max(theList)\n",
    "    idx = theList.index(currentMax)\n",
    "    if currentMax %2 == 0:\n",
    "        theList[idx]= (currentMax-1)//2+1\n",
    "    else:\n",
    "        theList[idx]= (currentMax-1)//2\n",
    "    theList.append((currentMax-1)//2)\n",
    "\n",
    "currentMax= max(theList)\n",
    "\n",
    "idx = theList.index(currentMax)\n",
    "if currentMax %2 == 0:\n",
    "    y= (currentMax-1)//2+1\n",
    "else:\n",
    "    y= (currentMax-1)//2\n",
    "\n",
    "z= (currentMax-1)//2\n",
    "print(theList)\n",
    "print(y,z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "theList = [N]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "theList.index(max(theList))"
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
