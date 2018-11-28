#include <algorithm>
#include <iostream>
#include <map>
#include <tuple>
#include <utility>

using namespace std;

pair<long long, long long> split_gap(long long gap) {
    if (gap & 1) {
        return make_pair(gap / 2, gap / 2);
    } else {
        return make_pair(gap / 2 - 1, gap / 2);
    }
}

int main() {
    int num_cases;
    cin >> num_cases;
    for (int case_index = 1; case_index <= num_cases; ++case_index) {
        long long N, K;
        cin >> N >> K;
        map<long long, long long> gap_count;
        gap_count[N] = 1;
        while (K > 0) {
            // Take the biggest gap.
            long long gap, c;
            tie(gap, c) = *gap_count.rbegin();
            gap_count.erase(gap);
            long long small, big;
            tie(small, big) = split_gap(gap);
            if (c >= K) {
                // This is the gap!
                cout << "Case #" << case_index << ": " << big << ' ' << small << endl;
                K = 0;
            } else {
                // This is not the gap yet, but we are closer.
                K -= c;
                gap_count[small] += c;
                gap_count[big] += c;
            }
        }
    }
    return 0;
}
