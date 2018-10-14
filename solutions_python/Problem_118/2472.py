object worksheet {

  val data = io.Source.fromFile("/Users/jamesbunch4/Documents/workspace/GoogleCodeJam/C-small-attempt1.in.txt")
                                                  //> data  : scala.io.BufferedSource = non-empty iterator
  val lines = data.getLines.toList                //> lines  : List[String] = List(100, 414 724, 1 5, 50 807, 9 65, 412 782, 1 100
                                                  //| 0, 3 742, 15 396, 425 509, 7 122, 89 536, 174 634, 455 931, 3 109, 100 1000,
                                                  //|  3 65, 122 1000, 1 104, 94 140, 15 855, 221 480, 487 859, 3 9, 1 485, 180 22
                                                  //| 9, 495 797, 513 872, 1 6, 9 675, 3 6, 21 302, 361 721, 1 221, 179 486, 384 5
                                                  //| 84, 156 574, 613 784, 4 109, 618 811, 1 122, 483 484, 21 742, 3 5, 24 636, 9
                                                  //|  221, 1 4, 8 9, 18 870, 87 766, 121 484, 121 742, 484 742, 121 485, 7 9, 4 9
                                                  //| , 27 235, 9 109, 52 845, 1 65, 64 614, 10 120, 1 584, 7 10, 121 122, 709 922
                                                  //| , 555 655, 415 902, 721 965, 65 221, 21 485, 1 1, 770 944, 121 121, 1 121, 1
                                                  //|  302, 177 272, 534 676, 1 2, 295 749, 122 483, 8 121, 484 485, 120 484, 121 
                                                  //| 221, 4 5, 46 78, 378 556, 1 109, 21 584, 303 584, 198 936, 8 584, 3 104, 9 4
                                                  //| 85, 3 4, 175 472, 270 686, 9 302, 3 302, 3 10)
  val numberOfCases = lines.head.toInt            //> numberOfCases  : Int = 100
  val caseEntries = lines.tail                    //> caseEntries  : List[String] = List(414 724, 1 5, 50 807, 9 65, 412 782, 1 10
                                                  //| 00, 3 742, 15 396, 425 509, 7 122, 89 536, 174 634, 455 931, 3 109, 100 1000
                                                  //| , 3 65, 122 1000, 1 104, 94 140, 15 855, 221 480, 487 859, 3 9, 1 485, 180 2
                                                  //| 29, 495 797, 513 872, 1 6, 9 675, 3 6, 21 302, 361 721, 1 221, 179 486, 384 
                                                  //| 584, 156 574, 613 784, 4 109, 618 811, 1 122, 483 484, 21 742, 3 5, 24 636, 
                                                  //| 9 221, 1 4, 8 9, 18 870, 87 766, 121 484, 121 742, 484 742, 121 485, 7 9, 4 
                                                  //| 9, 27 235, 9 109, 52 845, 1 65, 64 614, 10 120, 1 584, 7 10, 121 122, 709 92
                                                  //| 2, 555 655, 415 902, 721 965, 65 221, 21 485, 1 1, 770 944, 121 121, 1 121, 
                                                  //| 1 302, 177 272, 534 676, 1 2, 295 749, 122 483, 8 121, 484 485, 120 484, 121
                                                  //|  221, 4 5, 46 78, 378 556, 1 109, 21 584, 303 584, 198 936, 8 584, 3 104, 9 
                                                  //| 485, 3 4, 175 472, 270 686, 9 302, 3 302, 3 10)

  def isPal(i:Int) : Boolean= i.toString == i.toString.reverse
                                                  //> isPal: (i: Int)Boolean
  
  def calc(min: Int, max: Int): Int = {
    val palindromes = min.to(max).filter(isPal(_))
    //println(palindromes)
    val fairAndSquareNumbers = palindromes.filter(i => scala.math.sqrt(i).isValidInt && isPal(scala.math.sqrt(i).toInt))
    //println(fairAndSquareNumbers)

    fairAndSquareNumbers.size
  }                                               //> calc: (min: Int, max: Int)Int

  import java.io.PrintWriter
  import java.io.File
  val pw = new PrintWriter(new File("/Users/jamesbunch4/Documents/workspace/GoogleCodeJam/qcsmall.out.txt"))
                                                  //> pw  : java.io.PrintWriter = java.io.PrintWriter@2f833eca
  var i=1                                         //> i  : Int = 1
  for (entry <- caseEntries) {
    val min = entry.split(" ")(0).toInt
    val max = entry.split(" ")(1).toInt
    val res = calc(min, max)
    pw.println("Case #" + i + ": " + res)
    i=i+1
  }
  pw.close
  
  calc(100,1000)                                  //> res0: Int = 2

}