import java.io.FileWriter

import scala.io.Source
val in = "/Users/daria/Downloads/C-small-attempt3.in"
//val in = "/Users/daria/Downloads/in.txt"
val out = new FileWriter("/Users/daria/Downloads/out.txt")
val lines = Source.fromFile(in).getLines().toList

var T = lines(0).toInt
for (i <- 1 to T) {
  val offset = 1 + (i - 1) * 2
  val t = lines(offset).split(" ")
  val L = t(0).toInt
  val X = t(1).toInt
  val ch = lines(offset+1).toArray.map(c => c.toString)
  val r = "\nCase #%d: %s\n".format(i, if (process(L, X, ch)) "YES" else "NO")
  out.write(r)
  println(r)
}
out.close()
val step = Map(
  "1" -> Map("1" -> "1", "i" -> "i", "j" -> "j", "k" -> "k"),
  "i" -> Map("1" -> "i", "i" -> "-1", "j" -> "k", "k" -> "-j"),
  "j" -> Map("1" -> "j", "i" -> "-k", "j" -> "-1", "k" -> "i"),
  "k" -> Map("1" -> "k", "i" -> "j", "j" -> "-i", "k" -> "-1"),
  "-1" -> Map("1" -> "-1", "i" -> "-i", "j" -> "-j", "k" -> "-k"),
  "-i" -> Map("1" -> "-i", "i" -> "1", "j" -> "-k", "k" -> "j"),
  "-j" -> Map("1" -> "-j", "i" -> "k", "j" -> "1", "k" -> "-i"),
  "-k" -> Map("1" -> "-k", "i" -> "-j", "j" -> "i", "k" -> "1")
)
def process(L:Int, X: Int, ch: Array[String]): Boolean = {
  val s = Seq.fill(X)(ch).flatten.toArray
  println(s.deep.mkString("!"))
  val n = s.length
  var i = search(0, s, "i")
  if (i >= n - 1) {
    return false
  }
  print(".")

  var j = search(i+1, s, "j")
  if (j >= n - 1) {
    return false
  }
  print(".")
  return search_to_end(j+1, s, "k")
}

def search(pos: Int, s: Array[String], g: String): Int = {
  var ii = pos
  var n = s.length
  var p = s(ii)
  print(p)
  while (ii < n-1  && p != g) {
    p = step(p)(s(ii+1))
    print(p)
    ii += 1
  }
  ii
}

def search_to_end(pos: Int, s: Array[String], g: String): Boolean = {
  var ii = pos
  var n = s.length
  var p = s(ii)
  print(p)
  while (ii < n-1) {
    p = step(p)(s(ii+1))
    print(p)
    ii += 1
  }
  p == g
}

step("j")("i")
step("-k")("j")
step("i")("j")
step("k")("i")
