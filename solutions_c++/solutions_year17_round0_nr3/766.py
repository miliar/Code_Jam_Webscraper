#include <cstdint>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

void solve() {
    uint64_t N, K;
    cin >> N >> K;

    map<uint64_t, uint64_t> m;
    m[N] = 1;
    while (true) {
        auto iter = m.rbegin();
        uint64_t len = iter->first;
        uint64_t count = iter->second;
        m.erase(len);
        if (count >= K) {
            cout << (len / 2) << ' ' << ((len - 1) / 2) << endl;
            return;
        }
        K -= count;
        m[(len - 1) / 2] += count;
        m[len / 2] += count;
    }
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cout << "Case #" << testcase << ": ";
        solve();
    }
    return 0;
}
