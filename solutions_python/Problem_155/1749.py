import scala.io.BufferedSource

val INPUT: BufferedSource = io.Source.fromFile(
  "/Users/alexc/Downloads/A-large.in")
val LINES: Iterator[String] = INPUT.getLines()
val cases: Int = LINES.next().toInt

def caseAnalyzer(shynessCount: String) = {
  val split: Array[String] = shynessCount.split(" ")
  val maxShy: Int = split(0).toInt
  val allShyness: String = split(1)

  // map shyness to counts
  val shynessCounts: IndexedSeq[Int] = allShyness.map(x => x.asDigit)

  var runningCount: Int = 0
  var needed: Int = 0
  for ((count, idx) <- shynessCounts.zipWithIndex) {
    var toAdd: Int = 0

    // add ppl according to count until now
    if (runningCount < idx) {
      toAdd += idx - runningCount
      runningCount += toAdd
      needed += toAdd
    }

    // increment for next pass
    runningCount += count
  }

  needed
}

for ((l, idx) <- LINES.zipWithIndex) {
  val res: Int = caseAnalyzer(l)
  println(s"Case #${idx+1}: $res")
}
