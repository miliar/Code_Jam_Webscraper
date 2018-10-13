package aprokh.gcj2017_1b


import java.util.ArrayList
import java.util.StringTokenizer
//import scala.reflect.io.File
import java.io.BufferedReader
import java.io.BufferedInputStream
import java.io.InputStreamReader
import java.io.ByteArrayInputStream
import java.io.InputStream

object GCJ2017_1b_B {   var br = createBufferedReader(); var debugV = false 
    
    //COMMENT ME !
//    runTest(Test.sa0)
//    debugV = true
//    file = File("C:\\temp\\google cj\\2014q\\c-small.res")
  
  def main(args: Array[String]): Unit = {
    //---------------------------- parameters reading 
     val cases = readLine.int
     
    for (ca <- 1 to cases) {
      val line = readLine
      val N = line.long
      val R = "R" -> line.int
      val O = "O" -> line.int
      val Y = "Y" -> line.int
      val G = "G" -> line.int
      val B = "B" -> line.int
      val V = "V" -> line.int
      
//      val arr = Array(R,O,Y,G,B,V).sortBy(_._2)
      val arr = Array(R,Y,B).sortBy(_._2).reverse
      debug(arr.mkString(","))
      
      var res = "IMPOSSIBLE"
      var rr = new ArrayList[String]()
      if (arr(0)._2 > arr(1)._2 + arr(2)._2) {
       //imp 
      } else {
        for (i <- 0 until arr(0)._2) {
          rr.add(arr(0)._1)
        }
        var step = 1
        var index = rr.size - step
        for (i <- 0 until arr(1)._2) {
          put(arr(1)._1)
        }
        
        for (i <- 0 until arr(2)._2) {
          put(arr(2)._1)
        }

        def put(symb: String) = {
//          debug(s"put $symb $index $step")
          rr.add(index, symb)
          index -= step
          if (index == -1) {
            index = rr.size - 1
            step = 2
          }
        }
        
        res = rr.toArray().mkString("")
        debug(ca +" verify=" + verify(rr.toArray().map(_.toString)))
      }
      
      outLn(s"Case #$ca: " + res)
      
    }
    
    //---------------------------- parameters reading :end 
   
    finish
  }

  def verify(al: Array[String]): Boolean = {
    if (al(0) == al.last) {
      false
    } else {
      for (i <- 0 until al.length - 1) {
        if (al(i) == al(i+1)) return false
      }
      true
    }
  }
  
  
  //============================ service code ======================

//  var file:File = null
  val resultStr = new StringBuilder
  def outLn(str:String) = resultStr.append(str).append("\n")
  def outLn(number:Integer) = resultStr.append(number+"").append("\n")
  def finish() {
//    if (file == null || !devEnv) {
      println(resultStr.toString())
//    } else {
//      file.writeAll(resultStr.toString())
//    }
  }
  
  def readLine() = new Line  
  class Line {
    val fullLine = br.readLine()
    val tok = new StringTokenizer(fullLine, " ")
    def int = tok.nextToken().toInt
    def long = tok.nextToken().toLong
    def double = tok.nextToken().toDouble
    def string = tok.nextToken()
  }
  
  def createBufferedReader(inst:InputStream = System.in): BufferedReader = {
    val bis = if (inst == null) new BufferedInputStream(System.in) else new BufferedInputStream(inst);
    new BufferedReader(new InputStreamReader(bis));
  }
  
  def runTest(str:String) = if (devEnv) { 
    br = createBufferedReader(new ByteArrayInputStream(str.trim.getBytes("ISO-8859-1")))
  }
  
  def debug(x: => String) = if (debugV && devEnv) println(x) // nullary function
  
  lazy val devEnv = this.getClass.getCanonicalName.contains(".")
  
//============================================================================================
object Test {
  
val sa0 = """
4
6 2 0 2 0 2 0
3 1 0 2 0 0 0
6 2 0 1 1 2 0
4 0 0 2 0 0 2
"""

val sa2 = """
1
3 1 0 2 0 0 0
"""

val sa3 = """
"""
}

}

