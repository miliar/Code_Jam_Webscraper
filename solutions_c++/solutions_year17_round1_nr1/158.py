
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


char pp[33][33];
pair < int, int > pos[26];
int col[33];

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T; cin >> T;
    FOR(ts, 1, T+1){
        int n, m; cin >> n >> m;
        REP(i, n) cin >> pp[i];

        REP(i, 26) pos[i] = mp(1000, 1000);
        REP(i, n){
            REP(j, m){
                if(pp[i][j] != '?') pos[pp[i][j]-'A'] = mp(i, j);
            }
        }

        sort(pos, pos + 26);
        memset(col, -1, sizeof col);
        REP(i, 26){
            if(pos[i].xx == 1000) break;
            int l = -1, r = -1;
            for(int x = pos[i].xx; x > col[pos[i].yy]; x--){
                int tl = -1, tr = -1;
                for(int j = pos[i].yy; j >= 0; j--){
                    if(pp[x][j] == '?' || pp[x][j] == pp[ pos[i].xx ][ pos[i].yy ]) tl = j;
                    else break;
                }
                for(int j = pos[i].yy; j < m; j++){
                    if(pp[x][j] == '?' || pp[x][j] == pp[ pos[i].xx ][ pos[i].yy ]) tr = j;
                    else break;
                }
                if(l == -1) l = tl;
                else l = max(l, tl);
                if(r == -1) r = tr;
                else r = min(r, tr);
            }

            for(int j = col[pos[i].yy] + 1; j < n; j++){
                int fl = 0;
                for(int k = l; k <= r; k++){
                    if(pp[j][k] == '?' || pp[j][k] == pp[ pos[i].xx ][ pos[i].yy ]) continue;
                    else fl = 1;
                }
                if(fl) break;
                for(int k = l; k <= r; k++){
                    pp[j][k] = pp[ pos[i].xx ][ pos[i].yy ];
                    col[k] = j;
                }
            }
        }

        cout << "Case #" << ts << ":" << endl;
        REP(i, n) cout << pp[i] << endl;
    }
}

