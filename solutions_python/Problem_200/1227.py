package aprokh.gcj2017q


import java.util.ArrayList
import java.util.StringTokenizer
//import scala.reflect.io.File
import java.io.BufferedReader
import java.io.BufferedInputStream
import java.io.InputStreamReader
import java.io.ByteArrayInputStream
import java.io.InputStream

object GCJ2017_B {   var br = createBufferedReader(); var debugV = false 
    
    //COMMENT ME !
//    runTest(Test.large)
//    debugV = true
//    file = File("C:\\temp\\google cj\\2014q\\c-small.res")
  
  def isTidy(str: Array[Int]): Boolean = {
    var prev = 0
    var res = true
    for (i <- 0 until str.size) {
      if (prev > str(i).toInt) res = false
      prev = str(i)
    }
    res
  }

 def findFistBad(str: Array[Int]): Int = {
    var prev = 0
    for (i <- 0 until str.size) {
      if (prev > str(i).toInt) return i-1
      prev = str(i)
    }
    return -1
  }

  def main(args: Array[String]): Unit = {
    //---------------------------- parameters reading 
    val cases = readLine.int
    
    for (i <- 1 to cases) {
      var num = toArray(readLine.long)
      debug(toLong(num)+"")
      
      num = findTidy2(num)
      
//      val check = findTidy(num)
//      assert(toLong(check) == toLong(num))
      
      val res = toLong(num) 
      outLn(s"Case #$i: $res")
    }
    
    finish
  }
  
  def findTidy(nn: Array[Int]): Array[Int] = {
    var num = nn
    while (!isTidy(num)) {
      num = toArray((toLong(num) - 1))
    }
    num
  }
  
  def toLong(nn: Array[Int]): Long = {
    nn.foldLeft("")(_+_).toLong
  }
  
  def toArray(nn: Long): Array[Int] = {
    nn.toString().map(x => x.toString.toInt).toArray
  }
  
  def findTidy2(nn: Array[Int]): Array[Int] = {
    var ind = findFistBad(nn)
    while (ind != -1) {
      nn(ind) = nn(ind) -1
      for (i <- ind+1 until nn.length) nn(i) = 9
      ind = findFistBad(nn)
    }
    nn
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
  
val sa1 = """
4
132
1000
7
111111111111111110
"""

val sa2 = """

"""

val sa3 = """
"""

val large = """
1
""" + Long.MaxValue

val gen1 = """
100
796536
629116
10347
282922
262934
36193
770827
851812
353225
260687
521489
925036
999171
331692
772354
739833
914128
416499
958158
520595
44898
717944
770282
888106
380153
682505
301260
69058
101743
464816
355714
797388
804253
259414
242864
78225
930222
230786
619172
196551
800894
573886
858008
386374
634030
488730
792195
276628
958599
290186
408668
228252
556808
785642
451756
42942
809485
670626
322894
824128
308766
522789
106374
898081
303570
914451
351484
156942
449950
469439
392532
911470
918271
314890
981482
635928
915839
758894
860911
94436
339622
871575
972187
366815
117761
889131
666830
978648
534024
132459
44871
418071
614830
588913
867839
680429
862090
25305
508579
293863
"""

}

}

