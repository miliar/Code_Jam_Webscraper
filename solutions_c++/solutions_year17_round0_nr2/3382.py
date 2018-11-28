//
//  main.cpp
//  codejam
//
//  Created by Hyunjun Kim on 2017. 4. 8..
//  Copyright © 2017년 Hyunjun Kim. All rights reserved.
//

#include <iostream>
#include <string>
#include <cassert>

namespace ProblemB {

//#define trace(msg) std::cout << msg << std::endl
#define trace(msg) void()

bool isTidyNumber(int64_t number) {
    assert(number > 0 && number <= 1e18);
    int prev_digit = 9;
    while (number > 0) {
        int digit = number % 10;
        if (digit > prev_digit)
            return false;
        prev_digit = digit;
        number = number / 10;
    }
    return true;
}

const int64_t solve(int64_t number) {
    assert(number > 0 && number <= 1e18);
    
    int64_t digits = 1;
    
    while (number > 9) {
        if (isTidyNumber(number))
            break;
    
        // make last digit as 9
        number = (number / 10) - 1;
        digits *= 10;
        trace(number);
    }

    return number * digits + (digits - 1); // return XXX9999
}

void test() {
    assert(INT64_MAX > 1e18);
    assert(isTidyNumber(1233));
    assert(!isTidyNumber(12332));
    assert(!isTidyNumber(132));
    assert(!isTidyNumber(1000));
    assert(isTidyNumber(7));
    trace("Test OK");
}

}  // namespace ProblemB


int main(int argc, const char* argv[]) {
    ProblemB::test();
    
    trace(ProblemB::solve(132));
    trace(ProblemB::solve(1000));
    trace(ProblemB::solve(7));
    trace(ProblemB::solve(111111111111111110));
    
    int t;
    int64_t n;
    
    std::cin >> t;
    for (int tc = 0; tc < t; ++tc) {
        std::cin >> n;
        
        int64_t result = ProblemB::solve(n);
        
        std::cout << "Case #" << (tc + 1) << ": " << result;
        std::cout << std::endl;
    }
    
    return 0;
}
