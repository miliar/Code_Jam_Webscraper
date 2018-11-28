#include <iostream>
#include <map>
#include <cassert>
using namespace std;

int main(int argc, const char *argv[]) {
    size_t T;
    cin >> T;
    for (size_t t = 0; t < T; ++t) {
        size_t N, K;
        cin >> N >> K;
        
        // Interval sizes => number of each type of interval
        map<size_t, size_t, std::greater<size_t>> intervals;
        intervals.emplace(N, 1);

        auto addInterval = [&](size_t len, size_t num) {
            if (len == 0) return;
            auto result = intervals.emplace(len, num);
            if (result.second) return;
            // If intervals of the same size already exist, increment counts.
            result.first->second += num;
        };

        size_t size;
        while (K > 0) {
            size_t count;
            assert(intervals.size() > 0);
            auto front_it = intervals.begin();
            std::tie(size, count) = *front_it;
            intervals.erase(front_it);
            assert(size > 0);

            if (count >= K) break; // last person enters an interval of length "size"
            size_t leftSize = (size - 1) / 2;
            size_t rightSize = size / 2;
            // std::cout << "leftSize, rightSize: " << leftSize << ", " << rightSize << std::endl;
            addInterval(leftSize, count);
            addInterval(rightSize, count);

            K -= count;
        }

        // Last person enters an interval of length "size"
        // std::cout << "Last person entering interval of length " << size << std::endl;
        assert(size > 0);
        size_t y =  size      / 2,
               z = (size - 1) / 2;
        std::cout << "Case #" << t + 1 << ": " << y << " " << z << std::endl;
    }
    return 0;
}
