
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

string solve() {
    int64_t n, k;
    cin >> n >> k;

    // 0: n
    // 1: (n-1)/2 larger one on right
    map <int64_t, int64_t> m;
    m[n] = 1;
    for (int iter = 0;; iter++) {
        map <int64_t, int64_t> mnext;
        for (auto it = m.rbegin(); it != m.rend(); it++) {
            // cout << iter << " " << it->first << " " << it->second << endl;
            int64_t block = it->first - 1;
            k -= it->second;
            if (k <= 0)
                return to_string(block - block / 2) + " " + to_string(block / 2);
            mnext[block / 2] += it->second;
            mnext[block - block / 2] += it->second;
        }
        m = mnext;
    }
    return "";
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": " << solve() << endl;
    }
}
