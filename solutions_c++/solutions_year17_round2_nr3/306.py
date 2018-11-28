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

const int MAXN = 111;
slong dst[MAXN][MAXN];
const slong inf = INF * INF;
double ans[MAXN][MAXN];

void solve(int num)
{
    int N, Q;
    cin >> N >> Q;
    vector<slong> E(N+1);
    vector<double> S(N+1);
    cout << "Case #" << num << ": ";
    FOR(i,1,N) cin >> E[i] >> S[i];
    FOR(i,1,N) FOR(j,1,N) {
        cin >> dst[i][j];
        if(dst[i][j] == -1) dst[i][j] = inf;
    }
    FOR(k,1,N) {
        FOR(i,1,N) FOR(j,1,N) {
            dst[i][j] = min(dst[i][j], dst[i][k] + dst[k][j]);
        }
    }

    FOR(i,1,N) FOR(j,1,N) {
        ans[i][j] = inf;
        if(dst[i][j] <= E[i]) {
            ans[i][j] = dst[i][j] / S[i];
        }
    }

    FOR(k,1,N) {
        FOR(i,1,N) FOR(j,1,N) {
            ans[i][j] = min(ans[i][j], ans[i][k] + ans[k][j]);
        }
    }
    FOR(i,1,Q) {
        int U, V;
        cin >> U >> V;
        cout << ans[U][V] << " ";
    }
    cout << "\n";
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    cout << setprecision(12) << fixed;
    for(int i=1; i <= t; i++)
    {
        solve(i);
    }
}
