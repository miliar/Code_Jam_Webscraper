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
    int n, c, m; cin >> n >> c >> m;
    vector<int>tickets(n + 1), cust(c + 1, 0);
    rep(i, 0, m){
        int t1, t2; cin >> t1 >> t2;
        tickets[t1]++; cust[t2]++;
    }
    int min_r = *max_element(all(cust));
    int pref_sum = 0;
    rep(i, 1, n + 1){
        pref_sum += tickets[i];
        min_r = max(min_r, int((pref_sum + i - 1) / i));
    }
    int prom = 0;
    rep(i, 1, n + 1){
        prom += max(0, tickets[i] - min_r);
    }
    cout << min_r << " " << prom;
};


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
