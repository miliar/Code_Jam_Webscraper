#include <bits/stdc++.h>
using namespace std;
char enl = '\n';
#define rep(i, from, to) for (int i = from; i < (to); ++i)
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<pair<int, int>> vii;

void solve() {

    int n, p;
    cin >> n >> p;

    vi modcount(p);

    rep(i,0,n) {
        int g;
        cin >> g;
        modcount[(g%p)] += 1;
    }

    int ans = 0;

    if (p == 3) {


        ans = modcount[0];

        ans += min(modcount[1], modcount[2]);

        int x = max(modcount[1], modcount[2]) - min(modcount[1], modcount[2]);
        if (x > 0)
            ans += (x - 1) / 3 + 1;

    } else if (p == 2) {
        
        ans = modcount[0];
        if (modcount[1] > 0) {
            ans += (modcount[1] - 1) / 2 + 1;
        }

    } else if (p == 4) {

        ans = modcount[0];

        int t = min(modcount[1], modcount[3]);
        int s = max(modcount[1], modcount[3]);

        ans += t;

        ans += modcount[2] / 2;

        int left = s - t;

        if (modcount[2] % 2 == 1) {
            if (left >= 2) {
                ans += 1;
                left -= 2;
            } else {
                ans += 1;
                cout << ans << endl;
                return;
            }
        }

        if (left > 0)
            ans += (left - 1) / 4 + 1;

    }


    cout << ans << endl;

}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin.exceptions(cin.failbit);

    int t;
    cin >> t;
    rep(i,0,t) {
        cout << "Case #" << (i+1) << ":" << " ";
        solve();
    }

    return 0;
}
