package dfs.codingproblems.codejam.gcj2017.round1a

import java.io.BufferedReader
import java.io.BufferedWriter

fun alphabetCake(reader: BufferedReader, writer: BufferedWriter) {
    val (r, c) = reader.readLine().split(" ").map(String::toInt)
    val cake = Array(r) { Array<Char?>(c) { null } }
    (0..r - 1).forEach { row ->
        val line = reader.readLine()
        line.forEachIndexed { col, char ->
            if (char != '?') cake[row][col] = char
        }
    }

    val newCake = Array(r) { row -> Array(c) { col -> cake[row][col] } }

    (0..c - 1).forEach { col ->
        (0..r - 1).forEach { row ->
            val curr = cake[row][col]
            var topR = row
            var botR = row
            if (curr != null) {
                for (newR in row + 1..r - 1) {
                    if (newCake[newR][col] != null && newCake[newR][col] != curr) break
                    newCake[newR][col] = curr
                    botR = newR
                }
                for (newR in row - 1 downTo 0) {
                    if (newCake[newR][col] != null && newCake[newR][col] != curr) break
                    newCake[newR][col] = curr
                    topR = newR
                }
                for (newC in col + 1..c - 1) {
                    if ((topR..botR).any { newCake[it][newC] != null && newCake[it][newC] != curr }) break
                    (topR..botR).forEach { newCake[it][newC] = curr }
                }
                for (newC in col - 1 downTo 0) {
                    if ((topR..botR).any { newCake[it][newC] != null && newCake[it][newC] != curr }) break
                    (topR..botR).forEach { newCake[it][newC] = curr }
                }
            }
        }
    }

    newCake.forEach { row ->
        writer.newLine()
        writer.write(row.joinToString(""))
    }
}
