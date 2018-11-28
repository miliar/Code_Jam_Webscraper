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
    string S;
    int K;
    cin >> S >> K;
    int ans = 0;
    for (int i = 0; i < S.size() - K + 1; i++) {
        if (S[i] == '-') {
            for (int j = 0; j < K; j++) S[i + j] = S[i + j] == '-' ? '+' : '-';
            ans++;
        }
    }

    for (int i = 0; i < S.size(); i++) {
        if (S[i] == '-') {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << ans << endl;
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
