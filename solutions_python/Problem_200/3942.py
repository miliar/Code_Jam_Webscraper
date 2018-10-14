{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[36mraw\u001b[0m: \u001b[32mList\u001b[0m[\u001b[32mString\u001b[0m] = \u001b[33mList\u001b[0m(\n",
       "  \u001b[32m\"---+-++- 3\"\u001b[0m,\n",
       "  \u001b[32m\"+++++ 4\"\u001b[0m,\n",
       "  \u001b[32m\"-+-+- 4\"\u001b[0m,\n",
       "  \u001b[32m\"-++---+-+ 2\"\u001b[0m,\n",
       "  \u001b[32m\"-++ 2\"\u001b[0m,\n",
       "  \u001b[32m\"+-++++- 5\"\u001b[0m,\n",
       "  \u001b[32m\"-+-+ 2\"\u001b[0m,\n",
       "  \u001b[32m\"-+++-- 2\"\u001b[0m,\n",
       "  \u001b[32m\"+-+-+-+-+- 2\"\u001b[0m,\n",
       "  \u001b[32m\"--+- 3\"\u001b[0m,\n",
       "  \u001b[32m\"+----++ 4\"\u001b[0m,\n",
       "  \u001b[32m\"--+ 3\"\u001b[0m,\n",
       "  \u001b[32m\"--++ 2\"\u001b[0m,\n",
       "  \u001b[32m\"+++- 2\"\u001b[0m,\n",
       "  \u001b[32m\"+++- 3\"\u001b[0m,\n",
       "  \u001b[32m\"++-+--++ 3\"\u001b[0m,\n",
       "  \u001b[32m\"--- 2\"\u001b[0m,\n",
       "  \u001b[32m\"---+ 3\"\u001b[0m,\n",
       "  \u001b[32m\"++-- 2\"\u001b[0m,\n",
       "\u001b[33m...\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "val raw = scala.io.Source.fromFile(\"/Users/kmisiunas/Downloads/A-small-attempt1.in\").getLines.toList.tail"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "defined \u001b[32mfunction \u001b[36mIntegerDigits\u001b[0m\n",
       "defined \u001b[32mfunction \u001b[36mLength\u001b[0m\n",
       "defined \u001b[32mfunction \u001b[36mtidyQ\u001b[0m\n",
       "\u001b[36mres0_3\u001b[0m: \u001b[32mBoolean\u001b[0m = \u001b[32mtrue\u001b[0m\n",
       "\u001b[36mres0_4\u001b[0m: \u001b[32mBoolean\u001b[0m = \u001b[32mfalse\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def IntegerDigits(int: Long): Seq[Int] = int.toString.map(_.asDigit)\n",
    "def Length(n: Long): Int = n.toString.size\n",
    "\n",
    "def tidyQ(n: Long): Boolean = {val tmp = IntegerDigits(n); tmp.sorted == tmp}\n",
    "// test\n",
    "tidyQ(2223)\n",
    "tidyQ(221)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "defined \u001b[32mfunction \u001b[36mreduceOrder\u001b[0m\n",
       "\u001b[36mres1_1\u001b[0m: \u001b[32mLong\u001b[0m = \u001b[32m10201L\u001b[0m\n",
       "\u001b[36mres1_2\u001b[0m: \u001b[32mLong\u001b[0m = \u001b[32m1999L\u001b[0m\n",
       "\u001b[36mres1_3\u001b[0m: \u001b[32mLong\u001b[0m = \u001b[32m1999L\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def reduceOrder(n: Long, i: Int): Long = {\n",
    "    val order = scala.math.pow(10, Length(n) - i)\n",
    "    val x = n - order\n",
    "    (x - x % order + order -1).toLong \n",
    "}\n",
    "reduceOrder(10202, 5)\n",
    "reduceOrder(2022, 1)\n",
    "reduceOrder(2022, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "defined \u001b[32mfunction \u001b[36mtidyAtQ\u001b[0m\n",
       "\u001b[36mres2_1\u001b[0m: \u001b[32mBoolean\u001b[0m = \u001b[32mtrue\u001b[0m\n",
       "\u001b[36mres2_2\u001b[0m: \u001b[32mBoolean\u001b[0m = \u001b[32mtrue\u001b[0m\n",
       "\u001b[36mres2_3\u001b[0m: \u001b[32mBoolean\u001b[0m = \u001b[32mtrue\u001b[0m\n",
       "\u001b[36mres2_4\u001b[0m: \u001b[32mBoolean\u001b[0m = \u001b[32mfalse\u001b[0m\n",
       "\u001b[36mres2_5\u001b[0m: \u001b[32mBoolean\u001b[0m = \u001b[32mfalse\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def tidyAtQ(n: Long, pos: Int): Boolean = {\n",
    "    val tmp = IntegerDigits(n).drop(pos-1)\n",
    "    tmp.sorted == tmp\n",
    "}\n",
    "tidyAtQ(111111, 3)\n",
    "tidyAtQ(101111, 3)\n",
    "tidyAtQ(110111, 3)\n",
    "tidyAtQ(111011, 3)\n",
    "tidyAtQ(111101, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[32mimport \u001b[36mscala.annotation.tailrec\u001b[0m\n",
       "defined \u001b[32mfunction \u001b[36mfindTidySmallerThan\u001b[0m\n",
       "defined \u001b[32mfunction \u001b[36mfindTidySmallerThan\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import scala.annotation.tailrec\n",
    "\n",
    "@tailrec\n",
    "final def findTidySmallerThan(n: Long, pos: Int): Long = {\n",
    "    if(pos == 0) return n\n",
    "    else {\n",
    "        if(tidyAtQ(n, pos)){\n",
    "            findTidySmallerThan(n, pos - 1)\n",
    "        } else {\n",
    "            findTidySmallerThan(reduceOrder(n, pos), pos)\n",
    "        }\n",
    "    }\n",
    "}\n",
    "\n",
    "def findTidySmallerThan(n: Long): Long = findTidySmallerThan(n, Length(n))"
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
       "\u001b[36mres4_0\u001b[0m: \u001b[32mBoolean\u001b[0m = \u001b[32mtrue\u001b[0m\n",
       "\u001b[36mres4_1\u001b[0m: \u001b[32mBoolean\u001b[0m = \u001b[32mtrue\u001b[0m\n",
       "\u001b[36mres4_2\u001b[0m: \u001b[32mBoolean\u001b[0m = \u001b[32mtrue\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "// test\n",
    "findTidySmallerThan(132) == 129L\n",
    "findTidySmallerThan(1000) == 999L\n",
    "findTidySmallerThan(7) == 7L\n",
    "//findTidySmallerThan(111111111111111110L) == 99999999999999999L"
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
   "display_name": "Scala 2.11",
   "language": "scala211",
   "name": "scala211"
  },
  "language_info": {
   "codemirror_mode": "text/x-scala",
   "file_extension": ".scala",
   "mimetype": "text/x-scala",
   "name": "scala211",
   "pygments_lexer": "scala",
   "version": "2.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
