#include <bits/stdc++.h>

#define F first
#define S second
#define prev azaza
#define mp make_pair
#define pb push_back

using namespace std;
typedef long long ll;
typedef long double ld;

const int max_n = 10, inf = 1000111222;
vector<pair<int, int> > c, j;
int cntc, cntj;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    for (int I = 1; I <= T; ++I) {
        c.clear(), j.clear();
        cin >> cntc >> cntj;
        int from, to;
        for (int i = 0; i < cntc; ++i) {
            cin >> from >> to;
            c.pb(mp(from, to));
        }
        for (int i = 0; i < cntj; ++i) {
            cin >> from >> to;
            j.pb(mp(from, to));
        }
        int ans;
        if (cntc == 0 && cntj == 0 ||
            cntc == 0 && cntj == 1 ||
            cntc == 1 && cntj == 0 ||
            cntc == 1 && cntj == 1) {
            ans = 2;
        } else {
            vector<pair<int, int> > &cur = (cntc == 2 ? c : j);
            if (cur[0].F > cur[1].F) {
                swap(cur[0], cur[1]);
            }
            int d1 = cur[1].S - cur[0].F;
            int d2 = 1440 - (cur[1].F - cur[0].S);
            if (d1 <= 720 || d2 <= 720) {
                ans = 2;
            } else {
                ans = 4;
            }
        }
        cout << "Case #" << I << ": " << fixed << setprecision(10) << ans << endl;
    }
    return 0;
}


