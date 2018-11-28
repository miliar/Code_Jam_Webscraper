#include <iostream>

typedef unsigned long long ull;
typedef long long ll;

bool flip(std::string& s, ull pos, ull k) {
    if (pos + k > s.size()) {
        return false;
    }
    for (ull i = pos; i < pos + k; ++i) {
        if (s[i] == '+') {
            s[i] = '-';
        } else {
            s[i] = '+';
        }
    }
    return true;
}

int main() {
    ull t;
    std::cin >> t;
    for (ull i = 1; i <= t; ++i) {
        std::string s;
        ull k;
        std::cin >> s >> k;
        ull flips = 0;
        bool fail = false;
        for (ull pos = 0; pos < s.length(); ++pos) {
            if (s[pos] == '-') {
                if (flip(s, pos, k)) {
                    ++flips;
                } else {
                    fail = true;
                    break;
                }
            }
        }
        if (fail) {
            std::cout << "Case #" << i << ": IMPOSSIBLE" << std::endl;
        } else {
            std::cout << "Case #" << i << ": " << flips << std::endl;
        }
    }
    return 0;
}