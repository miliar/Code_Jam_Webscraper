{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[36mraw\u001b[0m: \u001b[32mList\u001b[0m[\u001b[32mString\u001b[0m] = \u001b[33mList\u001b[0m(\n",
       "  \u001b[32m\"2525 1\"\u001b[0m,\n",
       "  \u001b[32m\"2400 5\"\u001b[0m,\n",
       "  \u001b[32m\"300 2\"\u001b[0m,\n",
       "  \u001b[32m\"120 60\"\u001b[0m,\n",
       "  \u001b[32m\"60 90\"\u001b[0m,\n",
       "  \u001b[32m\"136233808 38\"\u001b[0m,\n",
       "  \u001b[32m\"87458713 3067\"\u001b[0m,\n",
       "  \u001b[32m\"36284210 2744\"\u001b[0m,\n",
       "  \u001b[32m\"115973179 5076\"\u001b[0m,\n",
       "  \u001b[32m\"135916824 4011\"\u001b[0m,\n",
       "  \u001b[32m\"110374927 1584\"\u001b[0m,\n",
       "  \u001b[32m\"104132860 5067\"\u001b[0m,\n",
       "  \u001b[32m\"5221369 9356\"\u001b[0m,\n",
       "  \u001b[32m\"36795225 9548\"\u001b[0m,\n",
       "  \u001b[32m\"83433443 7536\"\u001b[0m,\n",
       "  \u001b[32m\"122269921 7006\"\u001b[0m,\n",
       "  \u001b[32m\"42143126 4177\"\u001b[0m,\n",
       "  \u001b[32m\"75357856 1335\"\u001b[0m,\n",
       "  \u001b[32m\"113632339 6014\"\u001b[0m,\n",
       "\u001b[33m...\u001b[0m\n",
       "\u001b[36mraw2\u001b[0m: \u001b[32mList\u001b[0m[\u001b[32mArray\u001b[0m[\u001b[32mInt\u001b[0m]] = \u001b[33mList\u001b[0m(\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m2525\u001b[0m, \u001b[32m1\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m2400\u001b[0m, \u001b[32m5\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m300\u001b[0m, \u001b[32m2\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m120\u001b[0m, \u001b[32m60\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m60\u001b[0m, \u001b[32m90\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m136233808\u001b[0m, \u001b[32m38\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m87458713\u001b[0m, \u001b[32m3067\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m36284210\u001b[0m, \u001b[32m2744\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m115973179\u001b[0m, \u001b[32m5076\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m135916824\u001b[0m, \u001b[32m4011\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m110374927\u001b[0m, \u001b[32m1584\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m104132860\u001b[0m, \u001b[32m5067\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m5221369\u001b[0m, \u001b[32m9356\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m36795225\u001b[0m, \u001b[32m9548\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m83433443\u001b[0m, \u001b[32m7536\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m122269921\u001b[0m, \u001b[32m7006\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m42143126\u001b[0m, \u001b[32m4177\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m75357856\u001b[0m, \u001b[32m1335\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m113632339\u001b[0m, \u001b[32m6014\u001b[0m),\n",
       "\u001b[33m...\u001b[0m\n",
       "defined \u001b[32mfunction \u001b[36mformatInput\u001b[0m\n",
       "\u001b[36minputs\u001b[0m: \u001b[32mList\u001b[0m[(\u001b[32mArray\u001b[0m[\u001b[32mInt\u001b[0m], \u001b[32mList\u001b[0m[\u001b[32mArray\u001b[0m[\u001b[32mInt\u001b[0m]])] = \u001b[33mList\u001b[0m(\n",
       "  \u001b[33m\u001b[0m(\u001b[33mArray\u001b[0m(\u001b[32m2525\u001b[0m, \u001b[32m1\u001b[0m), \u001b[33mList\u001b[0m(\u001b[33mArray\u001b[0m(\u001b[32m2400\u001b[0m, \u001b[32m5\u001b[0m))),\n",
       "  \u001b[33m\u001b[0m(\u001b[33mArray\u001b[0m(\u001b[32m300\u001b[0m, \u001b[32m2\u001b[0m), \u001b[33mList\u001b[0m(\u001b[33mArray\u001b[0m(\u001b[32m120\u001b[0m, \u001b[32m60\u001b[0m), \u001b[33mArray\u001b[0m(\u001b[32m60\u001b[0m, \u001b[32m90\u001b[0m))),\n",
       "  \u001b[33m\u001b[0m(\n",
       "    \u001b[33mArray\u001b[0m(\u001b[32m136233808\u001b[0m, \u001b[32m38\u001b[0m),\n",
       "    \u001b[33mList\u001b[0m(\n",
       "      \u001b[33mArray\u001b[0m(\u001b[32m87458713\u001b[0m, \u001b[32m3067\u001b[0m),\n",
       "      \u001b[33mArray\u001b[0m(\u001b[32m36284210\u001b[0m, \u001b[32m2744\u001b[0m),\n",
       "      \u001b[33mArray\u001b[0m(\u001b[32m115973179\u001b[0m, \u001b[32m5076\u001b[0m),\n",
       "      \u001b[33mArray\u001b[0m(\u001b[32m135916824\u001b[0m, \u001b[32m4011\u001b[0m),\n",
       "      \u001b[33mArray\u001b[0m(\u001b[32m110374927\u001b[0m, \u001b[32m1584\u001b[0m),\n",
       "      \u001b[33mArray\u001b[0m(\u001b[32m104132860\u001b[0m, \u001b[32m5067\u001b[0m),\n",
       "      \u001b[33mArray\u001b[0m(\u001b[32m5221369\u001b[0m, \u001b[32m9356\u001b[0m),\n",
       "      \u001b[33mArray\u001b[0m(\u001b[32m36795225\u001b[0m, \u001b[32m9548\u001b[0m),\n",
       "      \u001b[33mArray\u001b[0m(\u001b[32m83433443\u001b[0m, \u001b[32m7536\u001b[0m),\n",
       "      \u001b[33mArray\u001b[0m(\u001b[32m122269921\u001b[0m, \u001b[32m7006\u001b[0m),\n",
       "      \u001b[33mArray\u001b[0m(\u001b[32m42143126\u001b[0m, \u001b[32m4177\u001b[0m),\n",
       "      \u001b[33mArray\u001b[0m(\u001b[32m75357856\u001b[0m, \u001b[32m1335\u001b[0m),\n",
       "      \u001b[33mArray\u001b[0m(\u001b[32m113632339\u001b[0m, \u001b[32m6014\u001b[0m),\n",
       "      \u001b[33mArray\u001b[0m(\u001b[32m78508228\u001b[0m, \u001b[32m6084\u001b[0m),\n",
       "\u001b[33m...\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "val raw = scala.io.Source.fromFile(\"/Users/kmisiunas/Downloads/A-large.in\")\n",
    "            .getLines.toList.tail;\n",
    "val raw2 = raw.map(_.split(\" \").map(_.toInt))\n",
    "\n",
    "def formatInput(rest: List[Array[Int]], out: List[(Array[Int], List[Array[Int]])]): List[(Array[Int], List[Array[Int]])] = {\n",
    "    if(rest.isEmpty) return out\n",
    "    else {\n",
    "        val prob = rest.head\n",
    "        val n = prob(1)\n",
    "        val form = (prob, rest.tail.take(n)) \n",
    "        return formatInput(rest.drop(n+1), out :+ form )\n",
    "    }\n",
    "}\n",
    "\n",
    "val inputs = formatInput(raw2, Nil)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[36mproblem\u001b[0m: (\u001b[32mArray\u001b[0m[\u001b[32mInt\u001b[0m], \u001b[32mList\u001b[0m[\u001b[32mArray\u001b[0m[\u001b[32mInt\u001b[0m]]) = \u001b[33m\u001b[0m(\u001b[33mArray\u001b[0m(\u001b[32m300\u001b[0m, \u001b[32m2\u001b[0m), \u001b[33mList\u001b[0m(\u001b[33mArray\u001b[0m(\u001b[32m120\u001b[0m, \u001b[32m60\u001b[0m), \u001b[33mArray\u001b[0m(\u001b[32m60\u001b[0m, \u001b[32m90\u001b[0m)))\n",
       "\u001b[36md\u001b[0m: \u001b[32mInt\u001b[0m = \u001b[32m300\u001b[0m\n",
       "\u001b[36mn\u001b[0m: \u001b[32mInt\u001b[0m = \u001b[32m2\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "val problem = inputs(1)\n",
    "\n",
    "val d = problem._1(0)\n",
    "val n = problem._1(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[36msorted\u001b[0m: \u001b[32mList\u001b[0m[\u001b[32mArray\u001b[0m[\u001b[32mInt\u001b[0m]] = \u001b[33mList\u001b[0m(\u001b[33mArray\u001b[0m(\u001b[32m120\u001b[0m, \u001b[32m60\u001b[0m), \u001b[33mArray\u001b[0m(\u001b[32m60\u001b[0m, \u001b[32m90\u001b[0m))\n",
       "\u001b[36mt\u001b[0m: \u001b[32mList\u001b[0m[\u001b[32mDouble\u001b[0m] = \u001b[33mList\u001b[0m(\u001b[32m3.0\u001b[0m, \u001b[32m2.6666666666666665\u001b[0m)\n",
       "\u001b[36mk\u001b[0m: \u001b[32mList\u001b[0m[\u001b[32mDouble\u001b[0m] = \u001b[33mList\u001b[0m(\u001b[32m120.0\u001b[0m, \u001b[32m60.0\u001b[0m)\n",
       "\u001b[36ms\u001b[0m: \u001b[32mList\u001b[0m[\u001b[32mDouble\u001b[0m] = \u001b[33mList\u001b[0m(\u001b[32m60.0\u001b[0m, \u001b[32m90.0\u001b[0m)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "val sorted = problem._2.sortBy(_(0)).reverse\n",
    "\n",
    "val t = sorted.map(x => (d-x(0)).toDouble/x(1))\n",
    "val k = sorted.map(_(0).toDouble)\n",
    "val s = sorted.map(_(1).toDouble)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "defined \u001b[32mfunction \u001b[36mestimateDt\u001b[0m\n",
       "\u001b[36mdt\u001b[0m: \u001b[32mcollection\u001b[0m.\u001b[32mimmutable\u001b[0m.\u001b[32mIndexedSeq\u001b[0m[\u001b[32mDouble\u001b[0m] = \u001b[33mVector\u001b[0m(\u001b[32m1.7976931348623157E308\u001b[0m, \u001b[32m2.0\u001b[0m)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def estimateDt(i: Int): Double = {\n",
    "    if(i==0) return Double.MaxValue // at the end\n",
    "    else return -  (k(i) - k(i-1))/(s(i)-s(i-1))\n",
    "}\n",
    "val dt = (0 until k.size).map(estimateDt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "defined \u001b[32mfunction \u001b[36mestimateTMax\u001b[0m\n",
       "\u001b[36mtMax\u001b[0m: \u001b[32mcollection\u001b[0m.\u001b[32mimmutable\u001b[0m.\u001b[32mIndexedSeq\u001b[0m[\u001b[32mDouble\u001b[0m] = \u001b[33mVector\u001b[0m(\u001b[32m3.0\u001b[0m, \u001b[32m2.0\u001b[0m)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def estimateTMax(i: Int): Double = {\n",
    "    if(i==0) return t(i) // at the end\n",
    "    else if( dt(i) <0 ) return t(i).toDouble // this one is slower\n",
    "    else if( dt(i) > t(i-1) ) return t(i).toDouble // does not catch up\n",
    "    else dt(i) // time it takes to cath previous one\n",
    "}\n",
    "val tMax = (0 until k.size).map(estimateTMax)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "defined \u001b[32mfunction \u001b[36mestimateKMax\u001b[0m\n",
       "\u001b[36mkMax\u001b[0m: \u001b[32mcollection\u001b[0m.\u001b[32mimmutable\u001b[0m.\u001b[32mIndexedSeq\u001b[0m[\u001b[32mDouble\u001b[0m] = \u001b[33mVector\u001b[0m(\u001b[32m300.0\u001b[0m, \u001b[32m240.0\u001b[0m)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def estimateKMax(i: Int): Double = { k(i).toDouble + tMax(i)*s(i)}\n",
    "val kMax = (0 until k.size).map(estimateKMax)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "defined \u001b[32mfunction \u001b[36mestimateSMax\u001b[0m\n",
       "\u001b[36msMax\u001b[0m: \u001b[32mcollection\u001b[0m.\u001b[32mimmutable\u001b[0m.\u001b[32mIndexedSeq\u001b[0m[\u001b[32mDouble\u001b[0m] = \u001b[33mVector\u001b[0m(\u001b[32m100.0\u001b[0m, \u001b[32m120.0\u001b[0m)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def estimateSMax(i: Int): Double = {kMax(i)/tMax(i)}\n",
    "val sMax = (0 until k.size).map(estimateSMax)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "defined \u001b[32mfunction \u001b[36msolve\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def solve(idx: Int): Double = {\n",
    "    val problem: (Array[Int], List[Array[Int]]) = inputs(idx)\n",
    "    val d = problem._1(0)\n",
    "    val n = problem._1(1)\n",
    "    \n",
    "    val sorted = problem._2.sortBy(_(0)).reverse\n",
    "\n",
    "    val t = sorted.map(x => (d-x(0)).toDouble/x(1))\n",
    "    val k = sorted.map(_(0).toDouble)\n",
    "    val s = sorted.map(_(1).toDouble)\n",
    "    \n",
    "    def estimateDt(i: Int): Double = {\n",
    "    if(i==0) return Double.MaxValue // at the end\n",
    "    else return -  (k(i) - k(i-1))/(s(i)-s(i-1))\n",
    "    }\n",
    "    val dt = (0 until k.size).map(estimateDt)\n",
    "    \n",
    "    def estimateTMax(i: Int): Double = {\n",
    "    if(i==0) return t(i).toDouble // at the end\n",
    "    else if( dt(i) <0 ) return t(i).toDouble // this one is slower\n",
    "    else if( dt(i) > t(i-1) ) return t(i).toDouble // does not catch up\n",
    "    else dt(i) // time it takes to cath previous one\n",
    "    }\n",
    "    val tMax = (0 until k.size).map(estimateTMax)\n",
    "    \n",
    "    def estimateKMax(i: Int): Double = { k(i).toDouble + tMax(i)*s(i)}\n",
    "    val kMax = (0 until k.size).map(estimateKMax)\n",
    "    \n",
    "    if (kMax.distinct.toList != List(d)) println(idx)\n",
    "    \n",
    "    def estimateSMax(i: Int): Double = {kMax(i).toDouble/tMax(i)}\n",
    "    val sMax = (0 until k.size).map(estimateSMax)\n",
    "    \n",
    "    sMax.min\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "7\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n",
      "16\n",
      "18\n",
      "19\n",
      "20\n",
      "22\n",
      "23\n",
      "24\n",
      "26\n",
      "28\n",
      "29\n",
      "30\n",
      "31\n",
      "32\n",
      "33\n",
      "34\n",
      "36\n",
      "37\n",
      "38\n",
      "39\n",
      "40\n",
      "41\n",
      "42\n",
      "43\n",
      "44\n",
      "45\n",
      "46\n",
      "47\n",
      "48\n",
      "49\n",
      "52\n",
      "55\n",
      "56\n",
      "57\n",
      "58\n",
      "59\n",
      "61\n",
      "62\n",
      "64\n",
      "65\n",
      "66\n",
      "67\n",
      "69\n",
      "70\n",
      "71\n",
      "72\n",
      "74\n",
      "75\n",
      "76\n",
      "77\n",
      "78\n",
      "79\n",
      "80\n",
      "81\n",
      "83\n",
      "84\n",
      "86\n",
      "87\n",
      "88\n",
      "89\n",
      "90\n",
      "91\n",
      "92\n",
      "93\n",
      "94\n",
      "95\n",
      "96\n",
      "97\n",
      "98\n",
      "99\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "\u001b[36mres\u001b[0m: \u001b[32mcollection\u001b[0m.\u001b[32mimmutable\u001b[0m.\u001b[32mIndexedSeq\u001b[0m[\u001b[32mDouble\u001b[0m] = \u001b[33mVector\u001b[0m(\n",
       "  \u001b[32m101.0\u001b[0m,\n",
       "  \u001b[32m100.0\u001b[0m,\n",
       "  \u001b[32m1191.019510295134\u001b[0m,\n",
       "  \u001b[32m132.46437588416345\u001b[0m,\n",
       "  \u001b[32m112.81094742037342\u001b[0m,\n",
       "  \u001b[32m1.01E9\u001b[0m,\n",
       "  \u001b[32m20000.0\u001b[0m,\n",
       "  \u001b[32m462.0984010346021\u001b[0m,\n",
       "  \u001b[32m4946.854732086053\u001b[0m,\n",
       "  \u001b[32m1.0516961229222428\u001b[0m,\n",
       "  \u001b[32m3685.8627806884747\u001b[0m,\n",
       "  \u001b[32m326.3268568562486\u001b[0m,\n",
       "  \u001b[32m40.33944481009311\u001b[0m,\n",
       "  \u001b[32m972.4437932724627\u001b[0m,\n",
       "  \u001b[32m4.457803997608491\u001b[0m,\n",
       "  \u001b[32m56.50950561199834\u001b[0m,\n",
       "  \u001b[32m158.77868998823575\u001b[0m,\n",
       "  \u001b[32m10000.00001\u001b[0m,\n",
       "  \u001b[32m1505.035525313007\u001b[0m,\n",
       "\u001b[33m...\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "val res = (0 until inputs.size).map(solve)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[32mimport \u001b[36mjava.io.File\u001b[0m\n",
       "\u001b[32mimport \u001b[36mjava.io.PrintWriter\u001b[0m\n",
       "defined \u001b[32mfunction \u001b[36mwriteToFile\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "import java.io.File\n",
    "import java.io.PrintWriter\n",
    "\n",
    "def writeToFile(path: String, text: String): Unit = {\n",
    "    val pw = new PrintWriter(new File(path))\n",
    "    try pw.write(text) finally pw.close()\n",
    "  }\n",
    "  \n",
    "writeToFile(\n",
    "    \"/Users/kmisiunas/Desktop/out.txt\",\n",
    "    res.zipWithIndex.map( x => \"Case #\"+(x._2+1)+\": \"+ x._1).mkString(\"\\n\")\n",
    ")"
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
