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

int solve(){
    int n, p; cin >> n >> p;
    map<int, int>cnts;
    rep(_, 0, n){
        int t1; cin >> t1;
        cnts[t1 % p]++;
    }
    if(p == 2){
        return cnts[0] + (cnts[1] + 1) / 2;
    } else if(p == 3){
        if(cnts[1] > cnts[2]){
            swap(cnts[1], cnts[2]);
        }
        cnts[2] -= cnts[1];
        return cnts[0] + cnts[1] + (cnts[2] + 2) / 3;
    } else if(p == 4){
        if(cnts[1] > cnts[3]){
            swap(cnts[1], cnts[3]);
        }
        cnts[3] -= cnts[1];
        if(cnts[2] & 1){
            return cnts[0] + cnts[1] + (cnts[2] + 1) / 2 + (cnts[3] + 1) / 4;
        } else {
            return cnts[0] + cnts[1] + (cnts[2] + 1) / 2 + (cnts[3] + 3) / 4;
        }
    }
    return 0;
}

int main()
{
#ifndef LOCAL
    ios_base::sync_with_stdio(0);
    cin.tie(0);
#endif
    int T; cin >> T;
    rep(t, 1, T + 1){
        cout << "Case #" << t << ": " << solve() << "\n";
    }
    return 0;
}
