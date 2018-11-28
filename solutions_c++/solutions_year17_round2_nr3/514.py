#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <string>
#define _repargs(_1,_2,_3,name,...) name
#define _rep(i,n) repi(i,0,n)
#define repi(i,a,b) for(int i=(int)(a);i<(int)(b);++i)
#define rep(...) _repargs(__VA_ARGS__,repi,_rep,)(__VA_ARGS__)
#define all(x) (x).begin(),(x).end()
#define mod 1000000007
//#define inf 2000000007
#define mp make_pair
#define pb push_back
typedef long long ll;
using namespace std;
template <typename T>
inline void output(T a, int p = 0) {
    if(p) cout << fixed << setprecision(p)  << a;
    else cout << a;
}
// end of template

const ll inf = 1LL << 60;

template <typename T> inline void voutput(T &v){
    rep(i, v.size()){
        if (i) cout << " ";
        output(v[i], 10);
    }
    cout << endl;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    // source code
    
    int T;
    cin >> T;
    rep(t, T){
        int N, Q;
        cin >> N >> Q;
        vector<pair<int, int>> H(N);
        rep(i, N) cin >> H[i].first >> H[i].second;
        vector<vector<ll>> D(N, vector<ll>(N));
        rep(i, N) rep(j, N) {
            ll d;
            cin >> d;
            if(d == -1) d = inf;
            D[i][j] = d;
        }
        vector<pair<int, int>> A(Q);
        rep(i, Q) {
            cin >> A[i].first >> A[i].second;
            A[i].first--, A[i].second--;
        }
        
        rep(i, N) D[i][i] = 0;
        
        rep(k, N){
            rep(i, N){
                rep(j, N){
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
                }
            }
        }
        vector<vector<double>> E(N, vector<double> (N, (double)inf));
        rep(i, N) E[i][i] = 0.0;
        
        rep(i, N) rep(j, N){
            if(D[i][j] <= H[i].first){
                E[i][j] = double(D[i][j]) / (double)H[i].second;
            }
        }
            
        rep(k, N){
            rep(i, N){
                rep(j, N){
                    if(D[i][k] != inf && D[k][j] != inf){
//                        cout << i << "," << k <<  "," << j << endl;
                        
                            E[i][j] = min(E[i][j], E[i][k] + E[k][j]);
//                            if(i == 2 && k == 1 && j == 0){
//                                cout << E[i][k] << "," << E[k][j] << endl;
//                            }
                        
                    }
                }
            }
        }
        
        vector<double> ans(Q);
        rep(i, Q){
            ans[i] = E[A[i].first][A[i].second];
        }
        
        
        cout << "Case #" << t + 1 << ": ";
        rep(i, ans.size()){
            if (i) cout << " ";
            output(ans[i], 10);
        }
        cout << endl;
//        output(ans);
        
    }

    
    return 0;
}
