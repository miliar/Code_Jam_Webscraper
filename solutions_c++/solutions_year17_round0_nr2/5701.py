#include <iostream>

std::string solve(std::string val) {
    char prev = '9';
    for (int j = val.length() - 1; j >= 0; --j) {
        if (val[j] > prev) {
            --val[j];
            for (int k = j+1; k < val.length(); ++k) {
                val[k] = '9';
            }
        }
        prev = val[j];
    }
    while (val.length() > 1 && val[0] == '0') {
        val.erase(0, 1);
    }
    return val;
}

int main() {
    int testcases;
    std::cin >> testcases;
    for (int i = 0; i < testcases; ++i) {
        std::string val;
        std::cin >> val;
        std::string result = solve(val);
        std::cout << "Case #" << (i+1) << ": " << result << std::endl;
    }
}
