import scala.io.BufferedSource

val INPUT: BufferedSource = io.Source.fromFile(
  "/Users/alexc/IdeaProjects/CodeJam2015/resources/D-small-attempt1.in")
val LINES: Iterator[String] = INPUT.getLines()
val cases: Int = LINES.next().toInt

def parse_args(line: String): (Int, (Int, Int)) = {
  val split: Array[String] = line.split(" ")
  val X: Int = split(0).toInt
  val R: Int = split(1).toInt
  val C: Int = split(2).toInt
  (X, (R, C))
}

def check_plays(X: Int, grid: (Int, Int)): Boolean = {
  val R = grid._1
  val C = grid._2
  for (y <- 1 to X-1) {
    if (y > R || y > C) {
      // Richard picks a piece larger than either side!
      return true
    }
  }
  if (((R * C) - X) % X != 0) {
    // Check mod of remainder
    true
  } else {
    false
  }
}

for ((l, idx) <- LINES.zipWithIndex) {
  val args: (Int, (Int, Int)) = parse_args(l)
  val X: Int = args._1
  val grid: (Int, Int) = args._2
  val richardWins: Boolean = check_plays(X, grid)
  var out: String = "GABRIEL"
  if (richardWins)
    out = "RICHARD"
  println(s"Case #${idx+1}: $out")
}
