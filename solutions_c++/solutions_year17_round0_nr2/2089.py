#include <iostream>
#include <cstdint>

using namespace std;

typedef std::uint64_t u64;

bool tidy(u64 n, u64 d = 9) {
    if (n == 0) return true;
    return (n % 10) <= d && tidy(n / 10, n % 10);
}

u64 prev_tidy(u64 n) {
    if (tidy(n)) return n;
    return prev_tidy(n / 10 - 1) * 10 + 9;
}

int main() {
    int T;
    cin >> T;
    for (int casen = 1; casen <= T; ++casen) {
        u64 in;
        cin >> in;
        std::cout << "Case #" << casen << ": " << prev_tidy(in) << endl;
    }
}
