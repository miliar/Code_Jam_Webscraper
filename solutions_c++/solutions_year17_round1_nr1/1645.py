#include <bits/stdc++.h>
using namespace std;

typedef vector<int> veci;
typedef pair<int,int> pii;
typedef vector<pii> vecii;
typedef long long ll;
typedef vector<ll> vecl;
typedef pair<ll,ll> pll;
typedef vector<pll> vecll;
#define EPS (1e-9)
#define MOD (int(1e9+7))
#define INF (int(1e9+9))
#define fi first
#define se second

int main()
{
    ios::sync_with_stdio(false);
    int tcases;
    cin >> tcases;
    for (int tc=1; tc<=tcases; ++tc)
{
    int r, c;
    cin >> r >> c;

    vector<string> res;
    res.resize(r);
    int px, py;
    for (int i=0; i<r; ++i) {
        cin >> res[i];
        py=-1,px=-1;
        for (int j=0; j<c; ++j) {
            if (res[i][j]=='?') {
                if (px>=0 && py>=0) {
                    res[i][j] = res[py][px];
                }
            } else {
                py = i;
                px = j;
            }
        }
    }

    for (int i=r-1; i>=0; --i) {
        py=-1,px=-1;
        for (int j=c-1; j>=0; --j) {
            if (res[i][j]=='?') {
                if (px>=0 && py>=0) {
                    res[i][j] = res[py][px];
                }
            } else {
                py = i;
                px = j;
            }
        }
    }

    for (int j=0; j<c; ++j) {
        py=-1,px=-1;
        for (int i=0; i<r; ++i) {
            if (res[i][j]=='?') {
                if (px>=0 && py>=0) {
                    res[i][j] = res[py][px];
                }
            } else {
                py = i;
                px = j;
            }
        }
    }
    for (int j=c-1; j>=0; --j) {
        py=-1,px=-1;
        for (int i=r-1; i>=0; --i) {
            if (res[i][j]=='?') {
                if (px>=0 && py>=0) {
                    res[i][j] = res[py][px];
                }
            } else {
                py = i;
                px = j;
            }
        }
    }

    cout << "Case #" << tc << ": " << endl;
    for (int i=0; i<r; ++i) {
        for (int j=0; j<c; ++j) {
            cout << res[i][j];
        }
        cout << endl;
    }
}
    return 0;
}
