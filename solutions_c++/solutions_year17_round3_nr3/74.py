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

typedef long double R;
R eps = 1e-12;

const int N = 50;

int n, k; 


R u;
R pb[N + 1];


void solve(){
    cin >> n >> k;
    cin >> u;
    rep(i, 0, n){
        cin >> pb[i];
    }
    pb[n] = 1.0;
    sort(pb, pb + n);
    rep(i, 0, n){
        if((pb[i + 1] - pb[i]) * (i + 1) < u + eps){
            u -= (i + 1) * (pb[i + 1] - pb[i]);
            rep(j, 0, i + 1){
                pb[j] = pb[i + 1];
            }
        } else {
            rep(j, 0, i + 1){
                pb[j] += u / (i + 1);
            }
            break;
        }
    }
    R res = 1.0;
    rep(i, 0, n){
        res *= pb[i];
    }
    cout << setprecision(15) << fixed << res;
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
