#include <bits/stdc++.h>
#define ll long long
#define int long long
#define F first
#define S second
using namespace std;

const int N = 1e5 + 10;

int t[N];
int n, k;

void solve() {
    string s;
    cin >> s >> k;
    int n = s.size();
    for(int i = 1; i <= n; i++) {
        if(s[i - 1] == '+') {
            t[i] = 1;
        } else {
            t[i] = 0;
        }
    }
    int ans = 0;
    for(int i = 1; i <= n - k + 1; i++) {
        if(t[i] == 0) {
            ans++;
            for(int j = 0; j < k; j++) {
                t[i + j] ^= 1;
            }
        }
    }
    for(int i = 1; i <= n; i++) {
        if(t[i] == 0) {
            cout << "IMPOSSIBLE\n";
            return;
        }
    }
    cout << ans << endl;
}

main() {
    ios_base::sync_with_stdio(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n;
    for(int i = 1; i <= n; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
}
