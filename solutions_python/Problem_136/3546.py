import java.io.File

object cookieclicker {
  val path = "/Users/andreimiclaus/Downloads/eclipse 2/workspace/MagicTrick/"
                                                  //> path  : String = /Users/andreimiclaus/Downloads/eclipse 2/workspace/MagicTri
                                                  //| ck/
  println("Read input")                           //> Read input
  new File(".").getAbsolutePath()                 //> res0: String = /Users/andreimiclaus/Downloads/eclipse 2/Eclipse.app/Contents
                                                  //| /MacOS/.
  val file = scala.io.Source.fromFile(path + "B-small-attempt0.in")
                                                  //> file  : scala.io.BufferedSource = non-empty iterator

  val iter = file.getLines                        //> iter  : Iterator[String] = non-empty iterator

  val rounds = Integer.parseInt(iter.next())      //> rounds  : Int = 100

  val res = new StringBuilder                     //> res  : StringBuilder = 

  "%.3f".format(0.714999999999).toString()        //> res1: String = 0.715

  for (i <- 1 to rounds) {
  	val values = iter.next().split(" ").map(_.toDouble)
  	val C = values(0)
  	val F = values(1)
  	val X = values(2)
 		
    solve(i, C,F,X, res)
    if (i < rounds) res ++= "\n"
  }                                               //> f1: 818.710685
                                                  //| f2: 446.1995613747016
                                                  //| f1: 446.1995613747016
                                                  //| f2: 386.9203085201948
                                                  //| f1: 386.9203085201948
                                                  //| f2: 370.41714361820465
                                                  //| f1: 370.41714361820465
                                                  //| f2: 366.44356748315334
                                                  //| f1: 366.44356748315334
                                                  //| f2: 367.2808515038283
                                                  //| f1: 20.0
                                                  //| f2: 20.0
                                                  //| f1: 20.0
                                                  //| f2: 21.666666666666668
                                                  //| f1: 977.9232
                                                  //| f2: 832.6866010555892
                                                  //| f1: 832.6866010555892
                                                  //| f2: 813.5536752542118
                                                  //| f1: 813.5536752542118
                                                  //| f2: 826.5877349051736
                                                  //| f1: 857.99182
                                                  //| f2: 645.2964648515189
                                                  //| f1: 645.2964648515189
                                                  //| f2: 587.9134002159108
                                                  //| f1: 587.9134002159108
                                                  //| f2: 571.6264008185439
                                                  //| f1: 571.6264008185439
                                                  //| f2: 570.515337448923
                                                  //| f1: 570.515337448923
                                                  //| f2: 575.9393856666302
                                                  //| f1: 0.5
                                                  //| f2: 136.46826150347255
                                                  //| f1: 953.85176
                                                  //| f2: 846.671446408479
                                                  //| f1: 846.671446408479
                                                  //| f2: 839.7319200613379
                                                  //| f1: 839.7319200613379
                                                  //| f2: 859.9189180135126
                                                  //| f1: 221.45
                                                  //| f2: 101.58428571428571
                                                  //| f1: 101.58428571428571
                                                  //| f2: 78.67023291925466

  //Print result to file
  printToFile(new File(path + "result"))(p => { p.println(res) })

  def computeC(C: Double, F: Double, X: Double, Nf: Int): Double = {
    (C) / (2 + F * Nf)
  }                                               //> computeC: (C: Double, F: Double, X: Double, Nf: Int)Double

  def computeX(C: Double, F: Double, X: Double, Nf: Int): Double = {
    (X) / (2 + F * Nf)
  }                                               //> computeX: (C: Double, F: Double, X: Double, Nf: Int)Double

  def computeAcc(C: Double, F: Double, X: Double, Nf: Int): Double = {
    var acc = 0.0
    for (i <- 0 to Nf - 1) {
      val x = computeC(C, F, X, i)
      acc += x
      //println("acc: " + acc + "," + x)
    }
    acc
  }                                               //> computeAcc: (C: Double, F: Double, X: Double, Nf: Int)Double

  def printToFile(f: java.io.File)(op: java.io.PrintWriter => Unit) {
    val p = new java.io.PrintWriter(f, "UTF-8")
    try { op(p) } finally { p.close() }
  }                                               //> printToFile: (f: java.io.File)(op: java.io.PrintWriter => Unit)Unit

  def solve(round: Int, C: Double, F: Double, X: Double, res: StringBuilder) {
  var formatted = ""
  	var optimum = false
  	var Nf = 0
   while (!optimum) {
    val f1 = computeAcc(C,F,X,Nf)+computeX(C, F, X, Nf)
    val f2 = computeAcc(C,F,X,Nf+1)+computeX(C, F, X, Nf+1)
    if (f1 < f2) {
      optimum = true
	   	formatted = "%.7f".format(f1).toString
    }
    println("f1: " + f1)
    println("f2: " + f2)
    Nf += 1
  }
    res ++= "Case #" + round + ": "+ formatted
  }                                               //> solve: (round: Int, C: Double, F: Double, X: Double, res: StringBuilder)Uni
                                                  //| t
}