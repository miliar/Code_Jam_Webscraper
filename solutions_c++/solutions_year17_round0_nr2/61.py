#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

template<class T>
inline T read() {
    T value;
    std::cin >> value;
    return value;
}

int main() {
#if 0
    // at first I thought I need to find the Nth tidy number :(
    uint64_t counts[20][10];
    for (int j = 9; j > 0; --j) {
        // exactly 1 number for single digits
        counts[0][j] = 1;
    }
    counts[0][0] = 0; // lonely 0 is not counted!
    for (int i = 1; i < 20; ++i) {
        // when you start with 9 the next number must be 9
        counts[i][9] = counts[i-1][9];
        for (int j = 8; j >= 0; --j) {
            // when you start with j the next number must be >= j
            counts[i][j] = counts[i-1][j] + counts[i][j + 1];
        }
    }
#endif

    int T = read<int>();
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        auto N = read<std::string>();
        size_t all_nine_after = N.size();
        for (size_t i = 1; i < all_nine_after; ++i) {
            if (N[i] < N[i-1]) {
                //std::cerr << "before: " << N << std::endl;
                // we need make number at i and after after it a 9
                for (size_t j = i; j < all_nine_after; ++j) {
                    N[j] = '9';
                }
                all_nine_after = i;
                // decrement the earlier number
                // we are guaranteed that N[i-1] > '0'
                --N[i-1];
                //std::cerr << " after: " << N << std::endl;
                if (i == 1) {
                    break;
                }
                i -= 2;
            }
        }
        size_t non_zero_start = N.size();
        for (size_t i = 0; i < N.size(); ++i) {
            if (N[i] != '0') {
                non_zero_start = i;
                break;
            }
        }
        N = N.substr(non_zero_start);
        printf("Case #%d: %s\n", caseNum, N.c_str());
    }
    return 0;
}
