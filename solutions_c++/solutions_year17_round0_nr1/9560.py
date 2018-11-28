#include <bits/stdc++.h>
#define ALL(x) (x).begin(), (x).end()
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

string s;

void solve() {
    int k;
    cin >> s >> k;
    for(int i = 0; i < (int)s.size(); ++i) {
        if ( s[i] == '+' ) s[i] = 1;
        else s[i] = 0;
    }
    int res = 0;
    for(int i = 0, n = s.size(); i <= n - k; ++i) {
        if ( !s[i] ) {
            res++;
            for(int j = i; j < i + k; ++j) {
                s[j] ^= 1;
            }
        }
    }
    for(int i = 0; i < (int)s.size(); ++i) {
        if ( !s[i] ) {
            cout << "IMPOSSIBLE\n";
            return;
        }
    }
    cout << res << endl;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }


    return 0;
}
