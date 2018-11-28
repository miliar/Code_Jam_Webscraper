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

void flip(char& ch) {
    // + => 43
    // - => 45
    ch = 45 - (ch - 43);
}

int main() {
    int T = read<int>();
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        std::string S = read<std::string>();
        size_t K = read<size_t>();
        int flips = 0;
        for (size_t i = 0; i < S.size(); ++i) {
            if (S[i] == '-') {
                if (S.size() - i < K) {
                    flips = -1;
                    break;
                }
                for (size_t j = 0; j < K; ++j) {
                    flip(S[i + j]);
                }
                ++flips;
            }
        }
        if (flips < 0) {
            printf("Case #%d: IMPOSSIBLE\n", caseNum);
        } else {
            printf("Case #%d: %d\n", caseNum, flips);
        }
    }
    return 0;
}
