#include <iostream>
#include <algorithm>
#include <cstdint>

using namespace std;

bool isTidy(uint64_t n) {
    string str = to_string(n);
    return is_sorted(str.begin(), str.end());
}

uint64_t largest_tidy_number(uint64_t n) {
    while (n >= 1) {
        if (isTidy(n)) {
            return n;
        }
        --n;
    }
    return -1;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        uint64_t N;
        cin >> N;
        cout << "Case #" << i << ": " << largest_tidy_number(N) << '\n';
    }
}
