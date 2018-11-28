#include<bits/stdc++.h>
#define two(a) (1<<(a))
#define LINF (1ll<<61)
#define EPS (1e-14)
#define Lshift(a,b) (a<<b)
#define Rshift(a,b) (a>>b)
#define rep(a,b) for(a=0 ; a<b ; a++)
#define xrep(a,b,c) for(a=b ; a<c ; a++)
#define INF (1<<29)
#define swap(a,b) ( (a^=b) , (b^=a) , (a^=b) )
#define GET(x) (mark[x>>5]>>(x&31)&1)
#define SET(x) (mark[x>>5]|=1<<(x&31))
#define maxL (10000000>>5)+1
#define mod 1000000007
typedef long long ll;
using namespace std;

int in[7]; // _, r, o, y, g, b, v


void solve(int t) {
    int i;
    vector<pair<int, string> > cols;
    rep(i, 7) cin >> in[i];
    int r(in[1]), y(in[3]), b(in[5]);
    auto limit = in[0] / 2;
    if (r > limit || y > limit || b > limit) {
        cout << "Case #" << t << ": ";
        cout << "IMPOSSIBLE" << endl;
    }
    else {
        cols.push_back({r, "R"});
        cols.push_back({y, "Y"});
        cols.push_back({b, "B"});
        sort(cols.begin(), cols.end());
        // for (int i = 0; i < cols.size(); i++) {
        //     cout << cols[i].first << ' ' << cols[i].second << endl;
        // }
        cout << "Case #" << t << ": ";
        for (int i = 0; i < cols[2].first; i++) {
            cout << cols[2].second;
            if (i < cols[1].first) {
                cout << cols[1].second;
            }
            if (cols[2].first - i <= cols[0].first) {
                cout << cols[0].second;
            }
        }
        cout << endl;
    }
}

int main() {
    int t, tt;
    cin >> tt;
    xrep(t, 1, tt+1) {
        solve(t);
    }
}
