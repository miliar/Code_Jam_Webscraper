//
//  Solver.swift
//  Gode-Jam
//
//  Created by Rafal on 08/04/2017.
//  Copyright © 2017 Rafal Szastok. All rights reserved.
//

import Foundation

class Solver {
    private static func onlyDigits(text: String) -> [Int8] {
        return text.characters.map {
            return Int8(String($0))!
        }
    }
    private static func toString(inputDigits: [Int8]) -> String {
        var digits = inputDigits
        if digits.first == 0 && inputDigits.count > 1 {
            digits = Array(digits.dropFirst())
        }
        return digits.reduce("", {
            $0 + String($1)
        })
    }
    static func solve(text: String) -> String {
        var arrayOfDigits = onlyDigits(text: text)

        for index in stride(from: 0, through: arrayOfDigits.count-2, by: 1) {
            if arrayOfDigits[index] > arrayOfDigits[index+1] {
                for fixingForwardIterator in stride(from: index+1, through: arrayOfDigits.count-1, by:1) {
                    arrayOfDigits[fixingForwardIterator] = 9
                }
                for fixingIterator in stride(from:index, through: 0, by: -1) {
                    if fixingIterator == 0 {
                        arrayOfDigits[fixingIterator] = arrayOfDigits[fixingIterator] - 1
                        break
                    }
                    if arrayOfDigits[fixingIterator]-1 >= arrayOfDigits[fixingIterator-1] {
                        arrayOfDigits[fixingIterator] = arrayOfDigits[fixingIterator] - 1
                        break
                    }
                    arrayOfDigits[fixingIterator] = 9
                }
                break
            }
        }
        return toString(inputDigits: arrayOfDigits)
    }
}
