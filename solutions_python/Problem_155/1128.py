import java.io.FileWriter

import scala.io.Source
val in = "/Users/daria/Downloads/A-large.in"
val out = new FileWriter("/Users/daria/Downloads/out.txt")
val lines = Source.fromFile(in).getLines().toList

var T = lines(0).toInt
for (i <- 1 to T) {
  val t = lines(i).split(" ")
  val Smax = t(0).toInt
  val S = t(1).toArray.map(e => e.toString.toInt)
  val r = "Case #%d: %d\n".format(i, process(Smax, S))
  out.write(r)
  println(r)
}
out.close()
def process(Smax: Int, S: Array[Int]): Int = {
  var j = 0
  while (!areClapping(Smax, S)) {
    S(0) += 1
    j += 1
  }
  return j
}
def areClapping(Smax:Int, S: Array[Int]): Boolean = {
  println(S.deep.mkString("!"))
  var i = 1
  var sum = S(0)
  while (i < S.length) {
    if (i <= sum) {
      sum += S(i)
    }
    i += 1
  }
  Smax <= sum
}