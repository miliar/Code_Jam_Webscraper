#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <unordered_map>

template<class T>
inline T read() {
    T value;
    std::cin >> value;
    return value;
}

int main() {
    int T = read<int>();
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        uint64_t N = read<uint64_t>();
        uint64_t K = read<uint64_t>();
        std::priority_queue<uint64_t> order;
        std::unordered_map<uint64_t, uint64_t> counts;
        order.push(N);
        counts[N] = 1;
        uint64_t Smax = 0;
        uint64_t Smin = 0;
        while (!order.empty()) {
            auto size = order.top();
            order.pop();
            auto count = counts[size];
            counts.erase(size);
            uint64_t a, b;
            if (size & 1) {
                a = b = size >> 1;
            } else {
                a = size >> 1;
                b = a - 1;
            }
            if (count >= K) {
                Smax = a;
                Smin = b;
                break;
            }
            K -= count;
            if (a > 0) {
                auto& acount = counts[a];
                if (acount == 0) {
                    order.push(a);
                }
                acount += count;
            }
            if (b > 0) {
                auto& bcount = counts[b];
                if (bcount == 0) {
                    order.push(b);
                }
                bcount += count;
            }
        }
        printf("Case #%d: %llu %llu\n", caseNum, Smax, Smin);
    }
    return 0;
}
