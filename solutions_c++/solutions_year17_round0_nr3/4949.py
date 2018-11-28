#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <deque>

using namespace std;

long long get_max_power2(long long val) {
    long long power = 1;

    int temp_val = val;

    while(val > 0) {
        power *= 2;
        val /= 2;
    }

    if ((temp_val % power) == 0) power *= 2;

    return power;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(2);
    cout << fixed;

    int T;

    cin >> T;

    for(int cs = 1;cs <= T;++cs) {
        long long N, K;

        cin >> N;
        cin >> K;

        pair<long long, long long> res = {0, 0};

        vector<int> bath(N);
        fill(bath.begin(), bath.end(), 0);

        if (K < N) {
            long long power = get_max_power2(K);
            res.first = (N - K) / power;
            res.second = (N - K + (power/2)) / power;
        }

        cout << "Case #" << cs << ": " << res.second << ' ' << res.first << '\n';
    }

    return 0;
}
