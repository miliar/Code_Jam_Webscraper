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

/* #define LOCAL */
#ifdef LOCAL
#define DBG(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define DBG(...) ;
#define cerr if(0)cout
#endif

typedef long double R;

const int N = 1000, K = 1000;

int n, k;
pair<int, int> pancakes[N + 1];


R sar(pair<int, int> p){ return 2.0 * M_PI * p.ft * p.sd;}

void solve(){
    cin >> n >> k;
    rep(i, 0, n){
        int r, h; cin >> r >> h;
        pancakes[i] = {r, h};
    }
    sort(pancakes, pancakes + n);
    R ans = 0.0;
    rep(i, 0, n){
        if(i >= k - 1){
            R res = M_PI * pancakes[i].ft * pancakes[i].ft + sar(pancakes[i]);
            DBG(i, res);
            sort(pancakes, pancakes + i, [&](auto& p1, auto& p2){ return sar(p1) < sar(p2);});
            rep(j, i - k + 1, i){
                res += sar(pancakes[j]);
            }
            DBG(res);
            ans = max(ans, res);
        }
    }
    cout << setprecision(15) << fixed << ans;
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
