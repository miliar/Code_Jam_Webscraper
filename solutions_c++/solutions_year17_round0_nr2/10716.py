//
//  main.cpp
//  TidyNumbers
//
//  Created by Jack Devlin on 08/04/2017.
//  Copyright © 2017 Jack Devlin. All rights reserved.
//

#include <iostream>
#include <vector>

class TestCase {
public:
    TestCase() = default;
    
    size_t maxVal;
    
    size_t solve() const {
        size_t retVal {0};

        // search from highest to lowest
        for (size_t number {maxVal}; number > 0; number--) {
            
            bool isTidy {true};
            std::string numberStr {std::to_string(number)};

            
            // single digit numbers are always tidy - no need to check those
            if (numberStr.size() > 1) {
                for (int iii {1}; iii < numberStr.size() && isTidy; iii++) {
                    if (numberStr[iii] < numberStr[iii - 1]) {
                        isTidy = false;
                    }
                }
            }
            
            // if it is tidy, set the value and stop searching
            if (isTidy) {
                retVal = number;
                break;
            }
        }
        
        return retVal;
    }
};




std::vector<TestCase> parseInput() {
    std::vector<TestCase> retVal;
    int numCases {0};
    
    std::cin >> numCases;
    
    for (size_t iii {0}; iii < numCases; iii++) {
        
        size_t val {0};
        std::cin >> val;
        
        TestCase tempCase;
        tempCase.maxVal = val;
        
        retVal.push_back(tempCase);
    }
    
    return retVal;
}



int main(int argc, const char * argv[]) {
    
    std::vector<TestCase> cases {parseInput()};
    
    for (size_t iii {0}; iii < cases.size(); iii++) {
        size_t solution {cases[iii].solve()};
        
        std::cout << "Case #" << iii+1 << ": " << solution << std::endl;
    }
    
    return 0;
}