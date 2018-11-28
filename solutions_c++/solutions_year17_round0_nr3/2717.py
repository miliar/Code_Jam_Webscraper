#include <iostream>
#include <deque>
#include <utility>
#include <cstdint>

typedef std::pair<uint64_t, uint64_t> pair64;

int main()
{
    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t) {
        uint64_t N, K;
        std::cin >> N >> K;
        std::deque<pair64> queue;
        queue.push_back(pair64(N, 1));

        for (; ; ) {
            pair64& cur = queue.front();

            if (K <= cur.second) {
                std::cout << "Case #" << t << ": " << (cur.first / 2) << " " << ((cur.first - 1) / 2) << std::endl;
                break;
            } else {
                K -= cur.second;
            }

            if (cur.first % 2 == 1) {
                pair64 new_pair(cur.first / 2, cur.second * 2);
                if (queue.back().first == new_pair.first) {
                    queue.back().second += new_pair.second;
                } else {
                    queue.push_back(new_pair);
                }
            } else {
                pair64 new_pair(cur.first / 2, cur.second);
                if (queue.back().first == new_pair.first) {
                    queue.back().second += new_pair.second;
                } else {
                    queue.push_back(new_pair);
                }
                new_pair.first -= 1;
                queue.push_back(new_pair);
            }

            queue.pop_front();
        }
    }
}
