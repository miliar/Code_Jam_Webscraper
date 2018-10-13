{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(case):\n",
    "    s, K = case.split(\" \")\n",
    "    K = int(K)\n",
    "    count = 0\n",
    "    for i in range(0,len(s)-K+1):\n",
    "        if s[i] == '-':\n",
    "            s = flipChunk(s,i,K)\n",
    "            count+=1\n",
    "    if '-' in s:\n",
    "        return \"IMPOSSIBLE\"\n",
    "    return str(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def flipChunk(s,i,K):\n",
    "    return s[0:i] + s[i:i+K].replace('-','*').replace('+','-').replace('*','+') + s[i+K:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'---+---+'"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "flipChunk(\"---+-++-\",5,3)"
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
      "---+-++-\n",
      "++++-++-\n",
      "+++++---\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'3'"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solve(\"---+-++- 3\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'x'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "Input\n",
    "  \t\n",
    "Output\n",
    " \n",
    "\n",
    "3\n",
    "---+-++- 3\n",
    "+++++ 4\n",
    "-+-+- 4\n",
    "\n",
    "Case #1: 3\n",
    "Case #2: 0\n",
    "Case #3: IMPOSSIBLE\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "---+-++- 3\n",
      "+++++ 4\n",
      "-+-+- 4\n",
      "-+-+-+--- 3\n",
      "---------- 2\n",
      "--------- 3\n",
      "+++ 3\n",
      "-+ 2\n",
      "++- 2\n",
      "---- 2\n",
      "-+++ 3\n",
      "+++ 2\n",
      "-----++++ 5\n",
      "+--+ 2\n",
      "+-+- 2\n",
      "+-+-+-+-+- 2\n",
      "-+-- 2\n",
      "++-+ 2\n",
      "--+- 2\n",
      "+-++ 3\n",
      "+- 2\n",
      "+--+ 3\n",
      "+--- 2\n",
      "+------ 6\n",
      "-++++++++- 2\n",
      "--++ 3\n",
      "-+++++++-+ 2\n",
      "---------- 10\n",
      "+-+ 3\n",
      "+-+-+-+- 3\n",
      "+-+-+-+-+ 4\n",
      "-+++++++-- 2\n",
      "-++-+ 2\n",
      "+-++--++ 4\n",
      "-++++ 2\n",
      "-+++--+ 2\n",
      "-+++++++++ 2\n",
      "++ 2\n",
      "+-+- 3\n",
      "++++++++ 5\n",
      "--+++ 2\n",
      "++++ 3\n",
      "--- 2\n",
      "--+ 2\n",
      "+++++++ 7\n",
      "-++++++++- 10\n",
      "+-+-+-+ 3\n",
      "--------+ 8\n",
      "++-- 3\n",
      "+-- 2\n",
      "-++++++++- 8\n",
      "---+ 2\n",
      "+++-+ 5\n",
      "-+-+-+-+-+ 2\n",
      "-++ 3\n",
      "+++++ 5\n",
      "-+-++--- 2\n",
      "++-- 2\n",
      "+--- 3\n",
      "---------- 3\n",
      "++------+ 6\n",
      "+-+ 2\n",
      "---+ 3\n",
      "-+---- 6\n",
      "-+-+ 2\n",
      "-+-+ 3\n",
      "++- 3\n",
      "--++ 2\n",
      "-++- 2\n",
      "+++- 2\n",
      "-+-- 3\n",
      "-- 2\n",
      "-----+-+ 7\n",
      "++++++++++ 9\n",
      "-----+ 5\n",
      "+-++ 2\n",
      "+-+-+-+-+ 3\n",
      "-+++- 4\n",
      "+-+-+-+-+- 3\n",
      "+++-++ 6\n",
      "++-+ 3\n",
      "-------- 2\n",
      "-++++++++- 9\n",
      "--- 3\n",
      "+++- 3\n",
      "--+ 3\n",
      "-+++ 2\n",
      "---- 3\n",
      "++++++++++ 10\n",
      "---------- 5\n",
      "-++ 2\n",
      "+-++-+++- 4\n",
      "-+- 2\n",
      "-+-++- 3\n",
      "+-+++++- 6\n",
      "--+- 3\n",
      "+-- 3\n",
      "++++ 2\n",
      "-++- 3\n",
      "-+- 3\n"
     ]
    }
   ],
   "source": [
    "f = open(\"A-small.in\")\n",
    "answers = []\n",
    "f.readline()\n",
    "count = 1\n",
    "for case in f:\n",
    "    ans = \"Case #\" + str(count) + \": \"\n",
    "    case = case.strip()\n",
    "    print case\n",
    "    ans += solve(case) + \"\\n\"\n",
    "    count += 1\n",
    "    answers.append(ans)\n",
    "    \n",
    "q = open(\"A-small.out\", 'w')\n",
    "for ans in answers:\n",
    "    q.write(ans)\n",
    "q.close()"
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
