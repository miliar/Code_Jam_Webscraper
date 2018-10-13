package dfs.codingproblems.codejam.gcj2017.round1b

import java.io.BufferedReader
import java.io.BufferedWriter
import java.math.BigDecimal
import java.math.RoundingMode

fun cruiseControl(reader: BufferedReader, writer: BufferedWriter) {
    val (d, n) = reader.readLine().split(" ").map(String::toInt)
    val horses = Array(n) {
        val (pos, speed) = reader.readLine().split(" ").map(String::toInt)
        Horse(pos, speed)
    }
    val result = cruiseControl(d, horses)
    writer.write(result.toString())
}

private fun cruiseControl(d: Int, horses: Array<Horse>): BigDecimal {
    val maxTime = horses.map { divide(decimal(d - it.pos), (decimal(it.speed))) }.max()!!
    return divide(decimal(d), maxTime)
}

private data class Horse(val pos: Int, val speed: Int)

private fun decimal(x: Int): BigDecimal {
    return BigDecimal.valueOf(x.toLong())
}

private fun divide(x: BigDecimal, y: BigDecimal): BigDecimal {
    return x.divide(y, 10, RoundingMode.DOWN)
}
