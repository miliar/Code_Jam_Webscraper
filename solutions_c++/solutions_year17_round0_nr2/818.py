#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int first_i(const std::vector<int> &digits) {
    for(int i = 1; i < digits.size(); i ++) {
        if(digits[i-1] < digits[i]) return i;
    }
    return -1;
}

int main() {
    int T;
    std::cin >> T;
    for(int C = 1; C <= T; C ++) {
        unsigned long N;
        std::cin >> N;

        std::vector<int> digits;
        while(N > 0) {
            digits.push_back(N % 10);
            N /= 10;
        }

        // 110

        // check if nonincreasing
        while(true) {
            //std::cout << "Digits: ";
            //for(auto d : digits) std::cout << d;
            //std::cout << std::endl;
            int fi = first_i(digits);
            if(fi == -1) break;

            digits[fi] --;
            for(int j = 0; j < fi; j ++) digits[j] = 9;

            int j = fi;
            while(digits[j] < 0 && j+1 < digits.size()) {
                digits[j] += 10;
                digits[j+1] --;
            }
        }
        while(digits.size() && digits.back() == 0) digits.pop_back();
        std::reverse(digits.begin(), digits.end());
        if(digits.size() == 0) digits.push_back(0);
        //while(digits.size() && digits.begin() == 0) digits.pop_

        std::cout << "Case #" << C << ": ";
        for(auto d : digits) std::cout << d;
        std::cout << std::endl;
    }
    return 0;
}
