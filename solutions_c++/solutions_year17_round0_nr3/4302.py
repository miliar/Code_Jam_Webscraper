#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>

using namespace std;

int main() {
    int T = 0;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        uint64_t N = 0;
        cin >> N;
        map<uint64_t, uint64_t, std::greater<uint64_t>> counts;
        counts[N] = 1;
        uint64_t K = 0;
        cin >> K;
        int res = 0;
        int mn_res = 0;
        while (K > 0) {
            auto cur = counts.begin();
            uint64_t t = min(K, cur->second);
            K -= t;
            cur->second -= t;
            auto val = cur->first;
            if (cur->second == 0)
                counts.erase(cur);
            if (val % 2 > 0) {
                res = val/2;
                mn_res = val/2;
                counts[val/2] += t * 2;
            } else {
                res = val/2;
                mn_res = val/2 - 1;
                counts[val/2] += t;
                counts[val/2 - 1] += t;
            }
        }
        cout << res << " " << mn_res;
        cout << endl;
    }
}

