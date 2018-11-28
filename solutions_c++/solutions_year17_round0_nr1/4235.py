#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <cstdio>
#include <cmath>
#include <queue>

using namespace std;


int solve(string s, int k) {
    int ans = 0;
    int n = s.size();
    for (int i = 0; i < n - k + 1; i++) {
        if (s[i] == '-') {
            ans++;
            for (int j = 0; j < k; j++) {
                s[i + j] = s[i + j] == '-' ? '+' : '-';
            }
        }
    }
    for (int i = 0; i < n; i++) {
        if (s[i] == '-') {
            return -1;
        }
    }
    return ans;
}

int main() {
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for (int z = 0; z < t; z++) {
        string s;
        int k;
        cin >> s >> k;
        int ans = solve(s, k);
        cout << "Case #" << z + 1 << ": ";
        if (ans == -1) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << ans << '\n';
        }
    }
    return 0;
}