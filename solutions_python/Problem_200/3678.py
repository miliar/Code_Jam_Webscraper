{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Problem B. Tidy Numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# load the file\n",
    "fileDir = \"C:\\\\codejam2017\\\\\"\n",
    "fileName = \"B-small-attempt0.in\"\n",
    "\n",
    "with open(fileDir+fileName,'r') as f:\n",
    "    cases=int(f.readline())\n",
    "    lines=f.readlines()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def recursiveLoop(aList, theMin, maxValue, currentSoluce, iteration):\n",
    "    spy = False\n",
    "    if spy: print(\"ITERATION \\t\", str(iteration), aList, theMin, maxValue, currentSoluce)\n",
    "    \n",
    "    #maxValue = int(aList[0])\n",
    "    # sortie de la boucle min > max\n",
    "    if maxValue<theMin:\n",
    "        if spy: print(\"\\t Sortie sur min>max\")\n",
    "        return None\n",
    "\n",
    "    # sortie de la boucle si il ne reste qu'un element\n",
    "    if len(aList)==1:\n",
    "        #currentSoluce.append(aList[0])\n",
    "        currentSoluce.append(str(maxValue))\n",
    "        if spy: print(\"\\t Sortie sur seul element\", currentSoluce)\n",
    "        return currentSoluce\n",
    "    \n",
    "    \n",
    "    for plausible in range(maxValue, theMin-1, -1):\n",
    "        currentSoluce.append(str(plausible))\n",
    "        if plausible == maxValue:\n",
    "            itMaxValue = int(aList[1])\n",
    "        else:\n",
    "            itMaxValue = 9\n",
    "            \n",
    "        analyse = recursiveLoop(aList[1:], plausible, itMaxValue, currentSoluce, iteration+1)\n",
    "        if spy: print(\"\\t resultat analyse : \", iteration, analyse)\n",
    "            \n",
    "        if analyse is None:\n",
    "            currentSoluce= currentSoluce[:-1]\n",
    "        else:\n",
    "            # solution trouvee\n",
    "            return analyse"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "soluce = []\n",
    "\n",
    "for case in range(cases):\n",
    "    N=list(lines[case].strip(\"\\n\"))\n",
    "    soluce.append(\"Case #\" + str(case+1) + \": \")\n",
    "    \n",
    "    analyse = recursiveLoop(N, int(N[0]), int(N[0]), [], 0)\n",
    "    \n",
    "    if analyse is None:\n",
    "        resultat = ['0']*(len(N)-1)\n",
    "        resultat.insert(0,N[0])\n",
    "        resultat = int(''.join(resultat))-1\n",
    "    else:\n",
    "        resultat = int(''.join(analyse))\n",
    "    \n",
    "    soluce.append(str(resultat))\n",
    "    soluce.append('\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 129\n",
      "Case #2: 999\n",
      "Case #3: 7\n",
      "Case #4: 99999999999999999\n",
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
   "execution_count": 168,
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
