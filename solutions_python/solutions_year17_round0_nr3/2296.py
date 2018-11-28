import java.io.{File, PrintWriter}

import scala.collection.mutable
import scala.io.Source

def minMax(a: Long): (Long, Long) = {
  val t = (a - 1) / 2
  val (l, r) = if ((a - 1) % 2 == 0) (t, t) else (t, t + 1)
  (math.min(l, r), math.max(l, r))
}

def findRes(n: Long, k: Long): (Long, Long) = {
  val priorityQueue = mutable.PriorityQueue.empty[(Long, Long)]
  priorityQueue.enqueue(minMax(n))
  for (kk <- (2.toLong to k)) {
    val curr = priorityQueue.dequeue()
    if (curr._1 > 0) priorityQueue.enqueue(minMax(curr._1))
    if (curr._2 > 0) priorityQueue.enqueue(minMax(curr._2))
  }
  val r = priorityQueue.dequeue()
  (r._2, r._1)
}

val fileName = "/Users/inna/scala/Study/Spark_Scala/untitled/C-small2.txt"
val pw = new PrintWriter(new File("/Users/inna/scala/Study/Spark_Scala/untitled/out3.txt" ))


val lines =  Source.fromFile(fileName).getLines().toList
for (t <- (1 to lines.size-1)) {
    val Array(n,k) = lines(t).split(" ").map(_.toLong)
  val res = findRes(n,k)
  pw.write(s"Case #${t}: ${res._1} ${res._2}\n")

}
pw.close

















