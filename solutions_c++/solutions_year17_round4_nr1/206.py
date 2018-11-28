
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
    }
    return (T)ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

int dp4[101][101][101][101][4];
int go4(int c0, int c1, int c2, int c3, int v){
    if(c0+c1+c2+c3 == 0) return 0;
    int &ret = dp4[c0][c1][c2][c3][v];
    if(ret != -1) return ret;
    ret = 0;
    int val = (v == 0);
    if(c0)ret = max(ret, val + go4(c0 - 1, c1, c2, c3, v));
    if(c1)ret = max(ret, val + go4(c0, c1 - 1, c2, c3, (v+1)%4));
    if(c2)ret = max(ret, val + go4(c0, c1, c2 - 1, c3, (v+2)%4));
    if(c3)ret = max(ret, val + go4(c0, c1, c2, c3 - 1, (v+3)%4));

    return ret;
}
int dp3[101][101][101][3];
int go3(int c0, int c1, int c2, int v){
    if(c0+c1+c2 == 0) return 0;
    int &ret = dp3[c0][c1][c2][v];
    if(ret != -1) return ret;
    ret = 0;
    int val = (v == 0);
    if(c0)ret = max(ret, val + go3(c0 - 1, c1, c2, v));
    if(c1)ret = max(ret, val + go3(c0, c1 - 1, c2, (v+1)%3));
    if(c2)ret = max(ret, val + go3(c0, c1, c2 - 1, (v+2)%3));

    return ret;
}

int dp2[101][101][3];
int go2(int c0, int c1, int v){
    if(c0+c1 == 0) return 0;
    int &ret = dp2[c0][c1][v];
    if(ret != -1) return ret;
    ret = 0;
    int val = (v == 0);
    if(c0)ret = max(ret, val + go2(c0 - 1, c1, v));
    if(c1)ret = max(ret, val + go2(c0, c1 - 1, (v+1)%2));

    return ret;
}

int main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    memset(dp2, -1, sizeof dp2);
    memset(dp3, -1, sizeof dp3);
    memset(dp4, -1, sizeof dp4);
    int T; cin >> T;
    FOR(ts, 1, T+1){
        int n, p; cin >> n >> p;
        int tmp[4] = {0};
        REP(i, n){
            int x; cin >> x;
            tmp[x % p]++;
        }
        cout << "Case #" << ts << ": ";
        if(p == 2) cout << go2(tmp[0], tmp[1], 0) << endl;
        if(p == 3) cout << go3(tmp[0], tmp[1], tmp[2], 0) << endl;
        if(p == 4) cout << go4(tmp[0], tmp[1], tmp[2], tmp[3], 0) << endl;
    }
}

