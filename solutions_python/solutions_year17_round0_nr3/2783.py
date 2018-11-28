{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
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
       "  \u001b[32m\"4 2\"\u001b[0m,\n",
       "  \u001b[32m\"5 2\"\u001b[0m,\n",
       "  \u001b[32m\"6 2\"\u001b[0m,\n",
       "  \u001b[32m\"1000 1000\"\u001b[0m,\n",
       "  \u001b[32m\"1000 1\"\u001b[0m,\n",
       "  \u001b[32m\"999 498\"\u001b[0m,\n",
       "  \u001b[32m\"1000 128\"\u001b[0m,\n",
       "  \u001b[32m\"1000 256\"\u001b[0m,\n",
       "  \u001b[32m\"1000 2\"\u001b[0m,\n",
       "  \u001b[32m\"2 2\"\u001b[0m,\n",
       "  \u001b[32m\"281 235\"\u001b[0m,\n",
       "  \u001b[32m\"599 499\"\u001b[0m,\n",
       "  \u001b[32m\"1000 500\"\u001b[0m,\n",
       "  \u001b[32m\"999 1\"\u001b[0m,\n",
       "  \u001b[32m\"1000 442\"\u001b[0m,\n",
       "  \u001b[32m\"500 500\"\u001b[0m,\n",
       "  \u001b[32m\"999 998\"\u001b[0m,\n",
       "  \u001b[32m\"865 811\"\u001b[0m,\n",
       "  \u001b[32m\"500 1\"\u001b[0m,\n",
       "\u001b[33m...\u001b[0m\n",
       "\u001b[36minputs\u001b[0m: \u001b[32mList\u001b[0m[\u001b[32mArray\u001b[0m[\u001b[32mInt\u001b[0m]] = \u001b[33mList\u001b[0m(\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m4\u001b[0m, \u001b[32m2\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m5\u001b[0m, \u001b[32m2\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m6\u001b[0m, \u001b[32m2\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m1000\u001b[0m, \u001b[32m1000\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m1000\u001b[0m, \u001b[32m1\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m999\u001b[0m, \u001b[32m498\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m1000\u001b[0m, \u001b[32m128\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m1000\u001b[0m, \u001b[32m256\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m1000\u001b[0m, \u001b[32m2\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m2\u001b[0m, \u001b[32m2\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m281\u001b[0m, \u001b[32m235\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m599\u001b[0m, \u001b[32m499\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m1000\u001b[0m, \u001b[32m500\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m999\u001b[0m, \u001b[32m1\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m1000\u001b[0m, \u001b[32m442\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m500\u001b[0m, \u001b[32m500\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m999\u001b[0m, \u001b[32m998\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m865\u001b[0m, \u001b[32m811\u001b[0m),\n",
       "  \u001b[33mArray\u001b[0m(\u001b[32m500\u001b[0m, \u001b[32m1\u001b[0m),\n",
       "\u001b[33m...\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "val raw = scala.io.Source.fromFile(\"/Users/kmisiunas/Downloads/C-small-1-attempt1.in\")\n",
    "            .getLines.toList.tail;\n",
    "val inputs = raw.map(_.split(\" \").map(_.toInt))\n"
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
     "data": {
      "text/plain": [
       "defined \u001b[32mfunction \u001b[36mIntegerDigits\u001b[0m\n",
       "defined \u001b[32mfunction \u001b[36mLength\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def IntegerDigits(int: Long): Seq[Int] = int.toString.map(_.asDigit)\n",
    "def Length(n: Long): Int = n.toString.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[32mimport \u001b[36mscala.annotation.tailrec\u001b[0m\n",
       "defined \u001b[32mfunction \u001b[36moccupyNext\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import scala.annotation.tailrec\n",
    "\n",
    "\n",
    "def occupyNext(seats: Array[Boolean]): (Array[Boolean], (Int, Int)) = {\n",
    "    var y = -1\n",
    "    val left = for(x <- seats) yield {y = if(x) -1 else y+1; y}\n",
    "    y = -1\n",
    "    val right = (for(x <- seats.reverse) yield {y = if(x) -1 else y+1; y}).reverse\n",
    "    \n",
    "    val max = left.zip(right).map(x => math.max(x._1, x._2))\n",
    "    val min = left.zip(right).map(x => math.min(x._1, x._2))\n",
    "    \n",
    "    val minValue = min.max\n",
    "    val pos = min.zipWithIndex.filter(_._1==minValue).map(_._2)\n",
    "    \n",
    "    def evaluatePos(i: Int): (Int, Int) = (max(i), i)\n",
    "    val finPos = pos.map(evaluatePos).maxBy(_._1)._2\n",
    "    \n",
    "    val copy = seats\n",
    "    copy(finPos) = true\n",
    "    \n",
    "    (copy, (max(finPos), min(finPos)))\n",
    "}\n",
    "\n",
    "\n",
    "//@tailrec\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[36mseats\u001b[0m: \u001b[32mList\u001b[0m[\u001b[32mBoolean\u001b[0m] = \u001b[33mList\u001b[0m(\n",
       "  \u001b[32mtrue\u001b[0m,\n",
       "  \u001b[32mfalse\u001b[0m,\n",
       "  \u001b[32mfalse\u001b[0m,\n",
       "  \u001b[32mfalse\u001b[0m,\n",
       "  \u001b[32mfalse\u001b[0m,\n",
       "  \u001b[32mfalse\u001b[0m,\n",
       "  \u001b[32mfalse\u001b[0m,\n",
       "  \u001b[32mfalse\u001b[0m,\n",
       "  \u001b[32mfalse\u001b[0m,\n",
       "  \u001b[32mtrue\u001b[0m,\n",
       "  \u001b[32mfalse\u001b[0m,\n",
       "  \u001b[32mfalse\u001b[0m,\n",
       "  \u001b[32mfalse\u001b[0m\n",
       ")\n",
       "\u001b[36my\u001b[0m: \u001b[32mInt\u001b[0m = \u001b[32m-1\u001b[0m\n",
       "\u001b[36mleft\u001b[0m: \u001b[32mList\u001b[0m[\u001b[32mInt\u001b[0m] = \u001b[33mList\u001b[0m(\u001b[32m-1\u001b[0m, \u001b[32m0\u001b[0m, \u001b[32m1\u001b[0m, \u001b[32m2\u001b[0m, \u001b[32m3\u001b[0m, \u001b[32m4\u001b[0m, \u001b[32m5\u001b[0m, \u001b[32m6\u001b[0m, \u001b[32m7\u001b[0m, \u001b[32m-1\u001b[0m, \u001b[32m0\u001b[0m, \u001b[32m1\u001b[0m, \u001b[32m2\u001b[0m)\n",
       "\u001b[36mright\u001b[0m: \u001b[32mList\u001b[0m[\u001b[32mInt\u001b[0m] = \u001b[33mList\u001b[0m(\u001b[32m-1\u001b[0m, \u001b[32m7\u001b[0m, \u001b[32m6\u001b[0m, \u001b[32m5\u001b[0m, \u001b[32m4\u001b[0m, \u001b[32m3\u001b[0m, \u001b[32m2\u001b[0m, \u001b[32m1\u001b[0m, \u001b[32m0\u001b[0m, \u001b[32m-1\u001b[0m, \u001b[32m2\u001b[0m, \u001b[32m1\u001b[0m, \u001b[32m0\u001b[0m)\n",
       "\u001b[36mmax\u001b[0m: \u001b[32mList\u001b[0m[\u001b[32mInt\u001b[0m] = \u001b[33mList\u001b[0m(\u001b[32m-1\u001b[0m, \u001b[32m7\u001b[0m, \u001b[32m6\u001b[0m, \u001b[32m5\u001b[0m, \u001b[32m4\u001b[0m, \u001b[32m4\u001b[0m, \u001b[32m5\u001b[0m, \u001b[32m6\u001b[0m, \u001b[32m7\u001b[0m, \u001b[32m-1\u001b[0m, \u001b[32m2\u001b[0m, \u001b[32m1\u001b[0m, \u001b[32m2\u001b[0m)\n",
       "\u001b[36mmin\u001b[0m: \u001b[32mList\u001b[0m[\u001b[32mInt\u001b[0m] = \u001b[33mList\u001b[0m(\u001b[32m-1\u001b[0m, \u001b[32m0\u001b[0m, \u001b[32m1\u001b[0m, \u001b[32m2\u001b[0m, \u001b[32m3\u001b[0m, \u001b[32m3\u001b[0m, \u001b[32m2\u001b[0m, \u001b[32m1\u001b[0m, \u001b[32m0\u001b[0m, \u001b[32m-1\u001b[0m, \u001b[32m0\u001b[0m, \u001b[32m1\u001b[0m, \u001b[32m0\u001b[0m)\n",
       "\u001b[36mminValue\u001b[0m: \u001b[32mInt\u001b[0m = \u001b[32m3\u001b[0m\n",
       "\u001b[36mpos\u001b[0m: \u001b[32mList\u001b[0m[\u001b[32mInt\u001b[0m] = \u001b[33mList\u001b[0m(\u001b[32m4\u001b[0m, \u001b[32m5\u001b[0m)\n",
       "defined \u001b[32mfunction \u001b[36mevaluatePos\u001b[0m\n",
       "\u001b[36mfinPos\u001b[0m: \u001b[32mInt\u001b[0m = \u001b[32m4\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "val seats = List(true,false,false,false,false,false,false,false,false,true,false,false,false)\n",
    "\n",
    "    var y = -1\n",
    "    val left = for(x <- seats) yield {y = if(x) -1 else y+1; y}\n",
    "    y = -1\n",
    "    val right = (for(x <- seats.reverse) yield {y = if(x) -1 else y+1; y}).reverse\n",
    "    \n",
    "    val max = left.zip(right).map(x => math.max(x._1, x._2))\n",
    "    val min = left.zip(right).map(x => math.min(x._1, x._2))\n",
    "\n",
    "    val minValue = min.max\n",
    "    val pos = min.zipWithIndex.filter(_._1==minValue).map(_._2)\n",
    "\n",
    "    def evaluatePos(i: Int): (Int, Int) = (max(i), i)\n",
    "\n",
    "    val finPos = pos.map(evaluatePos).maxBy(_._1)._2"
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
       "\u001b[36mtmp1\u001b[0m: (\u001b[32mArray\u001b[0m[\u001b[32mBoolean\u001b[0m], (\u001b[32mInt\u001b[0m, \u001b[32mInt\u001b[0m)) = \u001b[33m\u001b[0m(\u001b[33mArray\u001b[0m(\u001b[32mtrue\u001b[0m, \u001b[32mfalse\u001b[0m, \u001b[32mtrue\u001b[0m, \u001b[32mfalse\u001b[0m, \u001b[32mtrue\u001b[0m, \u001b[32mfalse\u001b[0m), \u001b[33m\u001b[0m(\u001b[32m3\u001b[0m, \u001b[32m2\u001b[0m))\n",
       "\u001b[36mtmp2\u001b[0m: (\u001b[32mArray\u001b[0m[\u001b[32mBoolean\u001b[0m], (\u001b[32mInt\u001b[0m, \u001b[32mInt\u001b[0m)) = \u001b[33m\u001b[0m(\u001b[33mArray\u001b[0m(\u001b[32mtrue\u001b[0m, \u001b[32mfalse\u001b[0m, \u001b[32mtrue\u001b[0m, \u001b[32mfalse\u001b[0m, \u001b[32mtrue\u001b[0m, \u001b[32mfalse\u001b[0m), \u001b[33m\u001b[0m(\u001b[32m1\u001b[0m, \u001b[32m1\u001b[0m))\n",
       "\u001b[36mtmp3\u001b[0m: (\u001b[32mArray\u001b[0m[\u001b[32mBoolean\u001b[0m], (\u001b[32mInt\u001b[0m, \u001b[32mInt\u001b[0m)) = \u001b[33m\u001b[0m(\u001b[33mArray\u001b[0m(\u001b[32mtrue\u001b[0m, \u001b[32mfalse\u001b[0m, \u001b[32mtrue\u001b[0m, \u001b[32mfalse\u001b[0m, \u001b[32mtrue\u001b[0m, \u001b[32mfalse\u001b[0m), \u001b[33m\u001b[0m(\u001b[32m1\u001b[0m, \u001b[32m0\u001b[0m))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "// test \n",
    "\n",
    "val tmp1 = occupyNext(Array(false,false,false,false,false,false))\n",
    "val tmp2 = occupyNext(tmp1._1)\n",
    "val tmp3 = occupyNext(tmp2._1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "defined \u001b[32mfunction \u001b[36mprocessSeating\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def processSeating(m: Int, k: Int): (Int, Int) = {\n",
    "    if (k > m/2) return (0,0)\n",
    "    else {\n",
    "        var stalls = (Array.fill[Boolean](m)(false), (-1,-1))\n",
    "        var i = 0;\n",
    "        while(i < k){\n",
    "            i = i+1;\n",
    "            stalls = occupyNext(stalls._1)\n",
    "        }\n",
    "        //println(stalls._1)\n",
    "        stalls._2\n",
    "    }\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[Z@6c3672bd\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "\u001b[36mres35\u001b[0m: (\u001b[32mInt\u001b[0m, \u001b[32mInt\u001b[0m) = \u001b[33m\u001b[0m(\u001b[32m500\u001b[0m, \u001b[32m499\u001b[0m)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "processSeating(1000,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[36mres\u001b[0m: \u001b[32mList\u001b[0m[(\u001b[32mInt\u001b[0m, \u001b[32mInt\u001b[0m)] = \u001b[33mList\u001b[0m(\n",
       "  \u001b[33m\u001b[0m(\u001b[32m1\u001b[0m, \u001b[32m0\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m1\u001b[0m, \u001b[32m0\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m1\u001b[0m, \u001b[32m1\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m0\u001b[0m, \u001b[32m0\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m500\u001b[0m, \u001b[32m499\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m1\u001b[0m, \u001b[32m0\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m3\u001b[0m, \u001b[32m3\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m1\u001b[0m, \u001b[32m1\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m250\u001b[0m, \u001b[32m249\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m0\u001b[0m, \u001b[32m0\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m0\u001b[0m, \u001b[32m0\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m0\u001b[0m, \u001b[32m0\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m1\u001b[0m, \u001b[32m0\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m499\u001b[0m, \u001b[32m499\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m1\u001b[0m, \u001b[32m1\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m0\u001b[0m, \u001b[32m0\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m0\u001b[0m, \u001b[32m0\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m0\u001b[0m, \u001b[32m0\u001b[0m),\n",
       "  \u001b[33m\u001b[0m(\u001b[32m250\u001b[0m, \u001b[32m249\u001b[0m),\n",
       "\u001b[33m...\u001b[0m"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "val res = inputs.map(in => processSeating(in(0), in(1)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
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
    "import java.io.File\n",
    "import java.io.PrintWriter\n",
    "\n",
    "def writeToFile(path: String, text: String): Unit = {\n",
    "    val pw = new PrintWriter(new File(path))\n",
    "    try pw.write(text) finally pw.close()\n",
    "  }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": []
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "writeToFile(\n",
    "    \"/Users/kmisiunas/Desktop/out.txt\",\n",
    "    res.zipWithIndex.map( x => \"Case #\"+(x._2+1)+\": \"+ x._1._1 +\" \"+ x._1._2).mkString(\"\\n\")\n",
    "    \n",
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
