#include <iostream>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;
    for (int i = 0; i < T; ++i) {
        std::string S;
        int K;
        int counter(0);
        std::cin >> S >> K;
        for (size_t j = 0; j < (S.size() - K + 1); ++j) {
            if (S[j] == '-') {
                for (int k = 0; k < K; ++k) {
                    S[j + k] = ((S[j + k] == '-') ? '+' : '-');
                }
                counter++;
            }
        }
        bool possible(true);
        for (int k = 0; k < K; ++k) {
            if (S[S.size() - 1 - k] == '-') {
                possible = false;
            }
        }
        std::cout << "Case #" << (i + 1) << ": ";
        if (possible)
            std::cout << counter << std::endl;
        else
            std::cout << "IMPOSSIBLE" << std::endl;
    }
}
