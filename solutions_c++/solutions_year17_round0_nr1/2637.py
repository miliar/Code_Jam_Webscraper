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

string solve(){
    string inpt; cin >> inpt;
    int k; cin >> k;
    int res = 0;
    rep(i, 0, SZ(inpt)){
        if(inpt[i] == '-'){
            res++;
            if(i > SZ(inpt) - k){
                return "IMPOSSIBLE";     
            } else {
                rep(j, i, i + k){
                    if(inpt[j] == '-'){
                        inpt[j] = '+';
                    } else {
                        inpt[j] = '-';
                    }
                }
            }
        }
    }
    return to_string(res);
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
