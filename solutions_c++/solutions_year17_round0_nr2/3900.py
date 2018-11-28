#include <iostream>
#include <sstream>
#include <iomanip>

int64_t intPow(int64_t a, int64_t  b) {
    int64_t result(1);
    for (int i = 0; i < b; ++i) {
        result *= a;
    }
    return result;
}

int main(int argc, char** argv) {
    int T;
    std::cin >> T;
    for (int i = 0; i < T; ++i) {
        int64_t N;
        std::cin >> N;
        int64_t n = N;
        std::stringstream ss;
        ss << std::setfill('0') << std::setw(20) << n;
        std::string s = ss.str();
        for (int j = 0; j + 1 < 20; ++j) {
            if (s[j] > s[j + 1]) {
                for (int k = j + 1; k < 20; ++k) {
                    s[k] = '9';
                }
                s[j]--;
                for (int k = j; k > 0; --k) {
                    if (s[k - 1] > s[k]) {
                        s[k - 1]--;
                        for (int l = k; l < 20; ++l) {
                            s[l] = '9';
                        }
                    }
                }
                break;
            }
        }
        ss.str(s);
        ss >> n;
        
        std::cout << "Case #" << (i + 1) << ": ";
        std::cout << (n) << std::endl;
    }
}
