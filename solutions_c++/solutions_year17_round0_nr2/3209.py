//
//  main.cpp
//  B. Tidy Numbers
//
//  Created by Jason Naldi on 08.04.17.
//  Copyright © 2017 jasonnaldi. All rights reserved.
//

#include <fstream>
#include <iostream>
#include <iomanip>
#include <vector>

#define READ_IN in
#define PRINT_OUT out

using namespace std;

namespace Path {
    string path = "/Users/jason/Documents/School/Uni/CS/Bachelor/2nd semester/Computer Challenges Lab/Google Codejam/2017/";
    string round = "1. Qualification Round/";
    string problemName = "B. Tidy Numbers/";
    string file_name = path + round + problemName + "/tests/large";
    string file_in = file_name + "_input.txt";
    string file_out = file_name + "_output.txt";
}

typedef uint64_t number_t;
typedef vector<int> digits_t;

int getDigitsCount(number_t n) {
    int digits = 0;
    while (n > 0) {
        n /= 10;
        ++digits;
    }
    
    return digits;
}

digits_t getDigits(number_t n) {
    digits_t digits(getDigitsCount(n));
    
    ssize_t i = digits.size() - 1;
    while (n > 0) {
        digits[i] = n % 10;
        n /= 10;
        --i;
    }
    
    return digits;
}

number_t getNumber(const digits_t &digits) {
    number_t n = 0;
    number_t power = 1;
    for (auto it = digits.rbegin(); it != digits.rend(); ++it) {
        n += (*it) * power;
        power *= 10;
    }
    
    return n;
}

void reduce(number_t &N, ssize_t digitIdx) {
    
}

int main(int argc, const char * argv[]) {
    // Speeds up input reading and output printing.
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    ifstream in(Path::file_in);
    ofstream out(Path::file_out);
    
    int T = 0;
    READ_IN >> T;
    
    for (int test = 1; test <= T; ++test) {
        number_t N = 0;
        
        READ_IN >> N;

        auto digits = getDigits(N);
        ssize_t i = digits.size() - 1;
        while (i > 0) {
            if (digits[i] < digits[i-1]) {
                // No digit will be < 0
                --digits[i-1];
                
                while (i < digits.size()) {
                    digits[i] = 9;
                    ++i;
                }
                
                // here `i` = digits.size(). Go back one to avoid outOfBounds.
                --i;
            } else {
                --i;
            }
        }
        
        PRINT_OUT << "Case #" << test << ": " << getNumber(digits) << "\n";
        cout << test << "\n";
    }
    
    return 0;
}
