#include <iostream>
#include <map>
int main() {
    int T; std::cin >> T; int test_id = 0;
    while (T > 0) { T--; test_id += 1; std::cout << "Case #" << test_id << ": ";
        long long N, K; std::cin >> N >> K; K--;
        std::map<long long, long long> counts; counts[N] = 1;
        std::map<long long, long long> ::iterator it;
        while (K > 0) {
            it = counts.end(); it--;
            long long value = it->first;
            long long cnt = it->second;
            counts.erase(it);
            long long nvalue_left = (value - 1) / 2;
            long long nvalue_right = (value - 1) / 2 + (value - 1) % 2;
            if (nvalue_left > 0) {
                counts[nvalue_left] += std::min(cnt, K);
            }
            if (nvalue_right > 0) {
                counts[nvalue_right] += std::min(cnt, K);
            }
            if (cnt > K) {
                counts[value] = cnt - K;
            }
            K -= std::min(cnt, K);
        }

        it = counts.end(); it--; int value = it->first;
        std::cout << (value - 1) / 2 + (value - 1) % 2 << ' ' << (value - 1) / 2 << std::endl;
    }
}
