#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (ll (i)=(0);(i)<(ll)(n);++(i))
typedef pair<int, int> P;
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    rep(i, t) {
        int r, c;
        cin >> r >> c;
        string rc[30];
        rep(a, r) cin >> rc[a];

        // 十分な数繰り返す
        rep(T, 50) {
            rep(a, r) rep(b, c) {
                if (rc[a][b] == '?') {
                    if (b - 1 >= 0 && rc[a][b-1] != '?') rc[a][b] = rc[a][b-1];
                    else if (b + 1 < c && rc[a][b+1] != '?') rc[a][b] = rc[a][b+1];
                }
            }
        }

        rep(T, 50) {
            rep(a, r) rep(b, c) {
                if (rc[a][b] == '?') {
                    if (a - 1 >= 0 && rc[a-1][b] != '?') rc[a][b] = rc[a-1][b];
                    else if (a + 1 < r && rc[a+1][b] != '?') rc[a][b] = rc[a+1][b];
                }
            }
        }

        cout << "Case #" << i+1 << ": " << endl;
        rep(a, r) {
            cout << rc[a] << endl;
        }

    }
}
