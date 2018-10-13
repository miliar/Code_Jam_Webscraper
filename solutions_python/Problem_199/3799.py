#! env amm

import scala.annotation.tailrec
import scala.io.Source
import scala.util.Try

val invert = (_: Char) match {
    case '-' => '+'
    case '+' => '-'
}

@tailrec
val solve: (Stream[Char], Int, Int) => Int = {
    case (Stream.Empty, k, acc) => acc
    case ('-' #:: Stream.Empty, k, _) if k > 1 => throw new IllegalStateException
    case ('+' #:: t, k, acc) => solve(t, k, acc)
    case ('-' #:: t, k, acc) =>
        if (t.take(k - 1).size < k - 1) {
            throw new IllegalStateException
        } else {
            solve(t.take(k - 1).map(invert) #::: t.drop(k - 1), k, 1 + acc)
        }
}

def parse(line: String) = {
    val parts = line.split(" ")
    (parts(0).toStream, parts(1).toInt, 0)
}

@main
def main(): Unit = {
    Source
        .stdin
        .getLines()
        .drop(1)
        .map(line => Try(solve.tupled(parse(line))).getOrElse("IMPOSSIBLE"))
        .zipWithIndex
        .foreach { case (s, i) =>
            println(s"Case #${i + 1}: $s")
        }
}