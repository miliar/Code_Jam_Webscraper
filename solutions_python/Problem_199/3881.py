import java.io.{BufferedWriter, File, FileWriter}

import scala.annotation.tailrec
import scala.io.Source

case class Task(state:String, size:Int)

case class Solution(steps:Option[Int])

@tailrec
def solve(task:Task, acc:Int):Solution = {
  def flip(x:Char): Char =
    if(x == '+')
      '-'
    else '+'

  if(task.state.forall(_ == '+'))
    Solution(Some(acc))
  else if(task.state.length < task.size)
    Solution(None)
  else if(task.state.head == '+')
    solve(task.copy(state = task.state.tail), acc)
  else
    solve(task.copy(state = task.state.take(task.size).map(flip) ++ task.state.drop(task.size)), acc + 1)
}


val in: String = "A-large.in"
val out: String = "e1.out"
val source = Source.fromFile(in).getLines().toSeq
val writer = new BufferedWriter(new FileWriter(out))


val N = source.head.toInt
for(i <- 0 until N) {
  val line = source(i + 1)
  val Array(state, size) = line.split(" ")
  val task = Task(state, size.toInt)
  val solution = solve(task, 0)
  writer.write(s"Case #${i+1}: ${solution.steps.getOrElse("IMPOSSIBLE")}\n")
}

writer.flush()


