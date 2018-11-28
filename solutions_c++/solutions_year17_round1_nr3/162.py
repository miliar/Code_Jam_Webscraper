
/*********************************************************************\
   |--\        ---       /\        |-----------| -----   /-------|    |
   |   \        |       /  \       |               |    /             |
   |    \       |      /    \      |               |   |              |
   |     \      |     /      \     |               |   |----|         |
   |      \     |    / ------ \    |-------|       |        |-----|   |
   |       \    |   /          \   |               |              |   |
   |        \   |  /            \  |               |              /   |
  ---        -------            ------           ----- |---------/    |
                                                                      |
    codeforces = nfssdq  ||  topcoder = nafis007                      |
    mail = nafis_sadique@yahoo.com || nfssdq@gmail.com                |
    IIT,Jahangirnagar University(41)                                  |
                                                                      |
**********************************************************************/

#include <bits/stdc++.h>
using namespace std;

#define xx         first
#define yy         second
#define pb         push_back
#define mp         make_pair
#define LL         long long
#define inf        INT_MAX/3
#define mod        1000000007ll
#define PI         acos(-1.0)
#define linf       (1ll<<60)-1
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ALL(A)     ((A).begin(), (A).end())
#define set0(ar)   memset(ar,0,sizeof ar)
#define vsort(v)   sort(v.begin(),v.end())
#define setinf(ar) memset(ar,126,sizeof ar)

//cout << fixed << setprecision(20) << p << endl;

template <class T> inline T bigmod(T p,T e,T M){
    LL ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

int dp[101][101][101][101], B, D, H;

int go(int hd, int ad, int hk, int ak){
    if(hk <= 0) return 0;
    if(hd <= 0) return inf;
    int &ret = dp[hd][ad][hk][ak];
    if(ret != -1) return ret;
    ret = inf;

    ret = min(ret, go(hd - ak, ad, hk - ad, ak) + 1);
    ret = min(ret, go(hd - ak, min(100, ad + B), hk, ak) + 1);
    ret = min(ret, go(H - ak, ad, hk, ak) + 1);
    ret = min(ret, go(hd - max(0, ak - D), ad, hk, max(0, ak - D)) + 1);

    return ret;
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T; cin >> T;
    FOR(ts, 1, T+1){
        int Ad, Hk, Ak; cin >> H >> Ad >> Hk >> Ak >> B >> D;
        memset(dp, -1, sizeof dp);
        int res = go(H, Ad, Hk, Ak);
        cerr << ts << " " << res << endl;
        if(res > 100000)
            cout << "Case #" << ts << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << ts << ": " << res << endl;
    }
}

