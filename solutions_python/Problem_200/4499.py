{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of cases 100\n",
      "\n",
      "Last case 132\n"
     ]
    }
   ],
   "source": [
    "input_raw = open(\"02-simple.in\")\n",
    "input = input_raw.readlines()\n",
    "\n",
    "nb_cases = input[0]\n",
    "cases = [s.strip(\"\\n\") for s in input[1:]]\n",
    "\n",
    "print \"Number of cases\", nb_cases\n",
    "# print \"Cases: \", cases\n",
    "\n",
    "num = cases[0]\n",
    "print \"Last case\", num"
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
    "def list_to_int(l):\n",
    "    \n",
    "    s = ''\n",
    "    \n",
    "    for i in l:\n",
    "        \n",
    "        s = s + str(i)\n",
    "        \n",
    "    return int(s)"
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
    "def int_to_list(integer):\n",
    "    \n",
    "    b = []\n",
    "    \n",
    "    for i in str(integer):\n",
    "        \n",
    "        b.append(i)\n",
    "        \n",
    "    return b\n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def ordered(number):\n",
    "    \n",
    "    for i, j in zip(str(number)[:-1], str(number)[1:]):\n",
    "        if int(i) > int(j):\n",
    "            return False\n",
    "    \n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def last_ordered(number):\n",
    "    \n",
    "    pos = 0\n",
    "    \n",
    "    if len(str(number)) == 1:\n",
    "        return number\n",
    "    \n",
    "    while ordered(number) == False:\n",
    "        \n",
    "        \n",
    "        if pos == len(str(number)) - 1:\n",
    "            \n",
    "            if ordered(number) == False:\n",
    "                \n",
    "                pos = 0\n",
    "        \n",
    "        elif int(str(number)[pos]) > int(str(number)[pos + 1]):\n",
    "            \n",
    "            number = int_to_list(number)\n",
    "            \n",
    "            number[pos] = str(int(number[pos]) - 1)\n",
    "            \n",
    "            for i, _ in enumerate(number[pos + 1:]):\n",
    "                \n",
    "                number[pos + i + 1] = \"9\"\n",
    "                \n",
    "            number = list_to_int(number)\n",
    "        \n",
    "        else:\n",
    "            \n",
    "            pos = pos + 1\n",
    "\n",
    "    return number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false,
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "199"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "last_ordered(214)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "out = open(\"02-out-simple.txt\", \"w\")\n",
    "\n",
    "for i, c in enumerate(cases):\n",
    "    \n",
    "    if i < len(cases) - 1:\n",
    "        out.write(\"Case #{}: {}\\n\".format(i + 1, last_ordered(c)))\n",
    "        \n",
    "    else:\n",
    "        out.write(\"Case #{}: {}\".format(i + 1, last_ordered(c)))\n",
    "        \n",
    "out.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def last_ordered_old(number):\n",
    "    \n",
    "    pos = -1 \n",
    "    \n",
    "    if len(str(number)) == 1:\n",
    "        return number\n",
    "    \n",
    "    while ordered_old(number) == False:\n",
    "        \n",
    "        number = number - 1\n",
    "        \n",
    "    return number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "last_ordered(214)"
   ]
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
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
