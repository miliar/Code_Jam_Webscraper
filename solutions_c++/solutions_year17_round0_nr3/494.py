#include <iostream>
#include <queue>
#include <map>

int main() {
    int T;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        long long N, K;
        std::cin >> N >> K;
        // std::cout << std::endl <<  "N: " << N << ", K: " << K << std::endl;

        std::map<long long,long long> m;
        // Initialize the queue
        m[N] = 1;

        long long min_segment = N;
        long long max_segment = N;
        long long num_left = K;

        while (num_left > 0) {
            std::map<long long,long long>::reverse_iterator rit = m.rbegin();
            long long segment_size = rit->first;
            long long num_slot = rit->second;
            // std::cout << segment_size << " " << num_slot << " " << num_left << std::endl;
            min_segment = (segment_size - 1)/2;
            max_segment = (segment_size - 1) - min_segment;
            num_left -= num_slot;
            if (m.find(min_segment) != m.end()) {
                m[min_segment] += num_slot;
            }
            else {
                m[min_segment] = num_slot;
            }

            if (m.find(max_segment) != m.end()) {
                m[max_segment] += num_slot;
            }
            else {
                m[max_segment] = num_slot;
            }
            m.erase(segment_size);
        }


        std::cout << "Case #" << t << ": " << max_segment << " " << min_segment << std::endl;

    }
    //std::cout << "Finished!" << std::endl;
    return 0;
}
