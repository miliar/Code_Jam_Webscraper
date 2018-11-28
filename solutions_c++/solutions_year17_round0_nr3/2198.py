#include <algorithm>
#include <bitset>
#include <complex>
#include <cstdio>
#include <cstdint>
#include <cassert>
#include <cmath>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

using int64 = int64_t;

constexpr int64 MOD = 1000000007;

string fmt(const int64 width) {
    stringstream ss;
    ss << width/2 << " " << (width-1)/2;
    return ss.str();
}

void inc_mapf(map<int64, int64>& m, int64 key, int64 val) {
    if (m.find(key) == end(m)) {
        m[key] = val;
    } else {
        m[key] += val;
    }
}

string solve(const int64 N, const int64 K) {
    map<int64, int64> spaces;
    spaces[N] = 1;

    int64 count = 0;
    while (count < K) {
        auto entry = spaces.rbegin();
        int64 width = entry->first, num = entry->second;

        if (count + num >= K) {
            return fmt(width);
        }

        spaces.erase(width);
        count += num;
        inc_mapf(spaces, width/2, num);
        inc_mapf(spaces, (width-1)/2, num);
    }

    return "should not reach here";
}

int main() {
    int T; cin >> T;
    for (int j = 0; j < T; ++j) {
        int64 N, K; cin >> N >> K;

        cout << "Case #" << (j+1) << ": " << solve(N, K) << endl;
    }
    return 0;
}
