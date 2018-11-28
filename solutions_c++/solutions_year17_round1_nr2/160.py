
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

int ar[55], last[55];
pair < int, int > pp[55][55];

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T; cin >> T;
    FOR(ts, 1, T+1){
        int n, m; cin >> n >> m;
        REP(i, n) cin >> ar[i];
        REP(i, n){
            REP(j, m){
                int x; cin >> x;
                int v = (x / ar[i]);
                v *= ar[i];
                pp[i][j] = mp(-1, -1);
                for(int k = v; k > 0; k -= ar[i]){
                    if(x * 10 <= k * 11){
                        pp[i][j].xx = k;
                    } else break;
                }
                if(v < x) v += ar[i];
                for(LL k = v; k <= 2000000; k += ar[i]){
                    if(x * 10 >= k * 9){
                        pp[i][j].yy = k;
                    } else {
                        break;
                    }
                }
                if(pp[i][j].xx == -1 && pp[i][j].yy != -1) pp[i][j].xx = pp[i][j].yy;
                if(pp[i][j].xx != -1 && pp[i][j].yy == -1) pp[i][j].yy = pp[i][j].xx;
                swap(pp[i][j].xx, pp[i][j].yy);
                pp[i][j].xx /= ar[i];
                pp[i][j].yy /= ar[i];
            }
            sort(pp[i], pp[i] + m);
            //REP(j, m) cout << pp[i][j].xx << " " << pp[i][j].yy << endl;
        }

        int res = 0;
        set0(last);
        for(int i = 1; i <= 2000000; i++){
            int fl = 0;
            REP(j, n){
                while(last[j] < m && pp[j][last[j]].xx < i){
                    last[j]++;
                }
                if(last[j] == m || pp[j][last[j]].yy > i) fl = 1;
            }
            if(fl) continue;
            res++;
            REP(j, n){
                last[j]++;
            }
            i--;
        }

        cout << "Case #" << ts << ": " << res << endl;
    }
}

