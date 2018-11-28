#include <iostream>
#include <vector>
#include <set>
#include <sstream>
#include <cmath>
#include <map>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <algorithm>
#include <list>

using namespace std;

const int MAXN = 1005;
char s[MAXN];

void solve() {
    int n, k;
    cin >> s >> k;
    n = (int) strlen(s);
    int ans = 0;
    for (int i = 0; i <= n - k; i++) {
        if (s[i] == '-') {
            for (int j = i; j < i + k; j++) {
                s[j] ^= '+' ^ '-';
            }
            ans++;
        }
    }
    for (int i = 0; i < n; i++) {
        if (s[i] == '-') {
            cout << "IMPOSSIBLE\n";
            return;
        }
    }
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    
    
    return 0;
}
