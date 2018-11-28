#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::ifstream input("A-large.in");
    std::ofstream output("output.txt");

    size_t test_size;
    input >> test_size;
    for (size_t test_num = 1; test_num <= test_size; ++test_num) {
        std::string state;
        size_t k_num;
        input >> state >> k_num;
        size_t answer = 0;
        for (size_t i = 0; i + k_num <= state.length(); ++i) {
            if (state[i] == '+') continue;
            ++answer;
            for (size_t j = 0; j < k_num; ++j) {
                state[i + j] = state[i + j] == '-' ? '+' : '-';
            }
        }
        output << "Case #" << test_num << ": ";
        if (state.find('-') != std::string::npos) {
            output << "IMPOSSIBLE" << std::endl;
        } else {
            output << answer << std::endl;
        }
    }
    return 0;
}
