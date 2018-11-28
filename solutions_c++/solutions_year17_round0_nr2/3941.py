#include <iostream>

typedef unsigned long long ull;
typedef long long ll;

int main() {
    ull t;
    std::cin >> t;
    for (ull i = 1; i <= t; ++i) {
        std::string n;
        std::cin >> n;
        n = '0' + n;
        bool tidy = true;
        ull bad;
        for (ull pos = 1; pos + 1 < n.size(); ++pos) {
            if (n[pos] > n[pos + 1]) {
                tidy = false;
                bad = pos;
                break;
            }
        }
        if (!tidy) {
            while (n[bad] == n[bad - 1]) {
                --bad;
            }
            --n[bad];
            for (ull pos = bad + 1; pos < n.size(); ++pos) {
                n[pos] = '9';
            }
        }
        std::cout << "Case #" << i << ": " << std::stoull(n) << std::endl;
    }
    return 0;
}