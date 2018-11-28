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

void solve(){
   ll n, k; cin >> n >> k;
   ll p2 = 1;
   while(k >= p2){
       k -= p2;
       p2 *= 2;
   }
   if(k == 0){
       cout << (n - (p2/2 - 1)) / p2 << " " << (n - (p2 - 1)) / p2;
   } else {
       cout << (n - (k - 1)) / (2 * p2) << " " << (n - (k - 1 + p2)) / (2 * p2);
   }
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
