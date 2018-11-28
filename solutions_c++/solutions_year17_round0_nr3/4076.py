#include <iostream>
#include <queue>

typedef unsigned long long ull;
typedef long long ll;

int main() {
    ull t;
    std::cin >> t;
    for (ull i = 1; i <= t; ++i) {
        ull n, k;
        std::cin >> n >> k;
        std::priority_queue<std::pair<ull, ull>> windows;
        windows.emplace(n, 1);
        std::pair<ull, ull> result;
        while (true) {
            auto& pair = windows.top();
            if (pair.second < k) {
                k -= pair.second;
                if (pair.first % 2 == 1) {
                    windows.emplace(pair.first / 2, pair.second * 2);
                } else {
                    windows.emplace((pair.first - 1) / 2, pair.second);
                    windows.emplace(pair.first / 2, pair.second);
                }
                windows.pop();
            } else {
                result.first = pair.first / 2;
                result.second = (pair.first - 1) / 2;
                break;
            }
        }
        std::cout << "Case #" << i << ": " << result.first << ' ' << result.second << std::endl;
    }
    return 0;
}