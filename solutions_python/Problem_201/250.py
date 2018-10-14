package dfs.codingproblems.codejam.gcj2017.qualification

import java.io.BufferedReader
import java.io.BufferedWriter

fun bathroomStalls(reader: BufferedReader, writer: BufferedWriter) {
    val (n, k) = reader.readLine().split(" ").map(String::toLong)
    doIt(n, k, writer)
}

private fun doIt(n: Long, k: Long, writer: BufferedWriter) {
    val histo = mutableMapOf(n to 1L)
    var kLeft = k
    var toPlace = 1L
    while (toPlace < kLeft) {
        kLeft -= toPlace
        toPlace *= 2
        val oldHisto = histo.toMap()
        histo.clear()
        oldHisto.forEach { size, count ->
            histo.merge(size / 2, count, Long::plus)
            histo.merge((size - 1) / 2, count, Long::plus)
        }
    }

    // Last level
    histo.keys.sorted().reversed()
        .forEach {
            val count = histo[it]!!
            if (count < kLeft) {
                kLeft -= count
            }
            else {
                val max = it / 2
                val min = (it - 1) / 2
                writer.write("$max $min")
                return
            }
        }
}
