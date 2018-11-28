#include<bits/stdc++.h>
#define ALL(X)        X.begin(),X.end()
#define FOR(I,A,B)    for(int (I) = (A); (I) <= (B); (I)++)
#define FORW(I,A,B)   for(int (I) = (A); (I) < (B);  (I)++)
#define FORD(I,A,B)   for(int (I) = (A); (I) >= (B); (I)--)
#define CLEAR(X)      memset(X,0,sizeof(X))
#define SIZE(X)       int(X.size())
#define CONTAINS(A,X) (A.find(X) != A.end())
#define PB            push_back
#define MP            make_pair
#define X             first
#define Y             second
using namespace std;
template<typename T, typename U> ostream& operator << (ostream& os, const pair<T, U> &_p) { return os << "(" << _p.X << "," << _p.Y << ")"; }
template<typename T> ostream& operator << (ostream &os, const vector<T>& _V) { bool f = true; os << "["; for(auto v: _V) { os << (f ? "" : ",") << v; f = false; } return os << "]"; }
template<typename T> ostream& operator << (ostream &os, const set<T>& _S) { bool f = true; os << "("; for(auto s: _S) { os << (f ? "" : ",") << s; f = false; } return os << ")"; }
template<typename T, typename U> ostream& operator << (ostream &os, const map<T, U>& _M) { return os << set<pair<T, U>>(ALL(_M)); }
typedef signed long long slong;
typedef long double ldouble;
typedef pair<int,int> pii;
const slong INF = 1000000100;
const ldouble EPS = 1e-9;

template<class TH> void _dbg(const char *sdbg, TH h){cerr<<sdbg<<"="<<h<<"\n";}
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while(*sdbg!=',')cerr<<*sdbg++;cerr<<"="<<h<<","; _dbg(sdbg+1, a...);
}

#ifdef LOCAL
  #define DBG(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
  #define DBG(...) ;
  #define cerr if(0)cout
#endif

void solve(int num)
{
    int N, C, M;
    cin >> N >> C >> M;
    vector<vector<int> > tickets(C+1);
    vector<int> sold(N+1,0);
    int min_rides = 0;
    FOR(i,1,M) {
        int b, p;
        cin >> p >> b;
        tickets[b].PB(p);
        sold[p]++;
    }
    FOR(i,1,C) {
        min_rides = max(min_rides, SIZE(tickets[i]));
    }

    pii ans = {M+1,0};

    FOR(r,min_rides,M) {
        int cost = 0;
        int pref = 0;
        int fail = 0;
        FOR(i,1,N) {
            pref += sold[i];
            if(pref > i * r) fail = 1;
            cost += max(0,sold[i]-r);
        }
        if(!fail) {
            ans = MP(r,cost);
            break;
        }
    }

    cout << "Case #" << num << ": " << ans.X << " " << ans.Y << "\n";

}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for(int i=1; i <= t; i++)
    {
        solve(i);
    }
}
