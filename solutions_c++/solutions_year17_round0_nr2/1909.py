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
    string sn;
    cin >> sn;

    int jank = -1;
    int n = int(sn.length());
    for (int i=0; i<n-1; ++i) {
        if (sn[i]>sn[i+1]) {
            jank = i;
            break;
        }
    }

    if (jank>=0) {
        while (jank>0 && (sn[jank]<=sn[jank-1])) {
            jank--;
        }

        for (int i=jank+1; i<n; ++i) {
            sn[i] = '9';
        }
        sn[jank] -= 1;

        if (sn[jank]=='0') {
            sn.erase(0,1);
        }
    }

    cout << "Case #" << tc << ": " << sn << endl;
}
    return 0;
}
