#include<bits/stdc++.h>
#define rep(i,k,n) for(ll i= (ll) k;i< (ll) n;i++)
#define all(v) (v).begin(), (v).end()
#define SZ(v) (int)((v).size())
#define pb push_back
#define ft first
#define sd second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
const long long INF = 4e18L + 1;
const int IINF = 2e9 + 1;

using namespace std;

template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while(*sdbg!=',')cerr<<*sdbg++;cerr<<'='<<h<<','; _dbg(sdbg+1, a...);
}

#define LOCAL
#ifdef LOCAL
#define DBG(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define DBG(...) ;
#define cerr if(0)cout
#endif

const int M = 1440;

ll dp[M + 2][M + 2][2][2];
ll O[M + 2];


void solve(){
    int a_c, a_j; cin >> a_c >> a_j;
    rep(i, 0, M + 2){
        O[i] = -1;
    }
    rep(_, 0, a_c){
        ll c, d; cin >> c >> d;
        rep(i, c + 1, d + 1){
            O[i] = 0;
        }
    }
    rep(_, 0, a_j){
        ll c, d; cin >> c >> d;
        rep(i, c + 1, d + 1){
            O[i] = 1;
        }
    }
    rep(i, 0, M + 2){
        rep(j, 0, M + 2){
            rep(p, 0, 2){
                rep(p1, 0, 2){
                    dp[i][j][p][p1] = IINF;
                }
            }
        }
    }
    rep(p, 0, 2){
        dp[1][0][p][p] = 0; 
    }
    rep(i, 2, M + 2){
        rep(j, 0, i){
            rep(p, 0, 2){
                rep(p1, 0, 2){
                    if(O[i - 1] != p){
                        if(p == 0){
                            if(j > 0){
                                dp[i][j][p][p1] = min(dp[i][j][p][p1], dp[i - 1][j - 1][p][p1]);
                                dp[i][j][p][p1] = min(dp[i][j][p][p1], dp[i - 1][j - 1][p ^ 1][p1] + 1);
                            }
                        } else {
                            dp[i][j][p][p1] = min(dp[i][j][p][p1], dp[i - 1][j][p][p1]);
                            dp[i][j][p][p1] = min(dp[i][j][p][p1], dp[i - 1][j][p ^ 1][p1] + 1);
                        }
                    }
                }
            }
        }
    }
    cout << min({dp[M + 1][M / 2][0][0], dp[M + 1][M / 2][1][1], dp[M + 1][M / 2][0][1] + 1, dp[M + 1][M / 2][1][0] + 1});
}

int main()
{
#ifndef LOCAL
    ios_base::sync_with_stdio(0);
    cin.tie(0);
#endif
    int T; cin >> T;
    rep(t, 1, T + 1){
        cout << "Case #" << t << ": ";
        solve();
        cout << "\n";
    } 
    return 0;
}
