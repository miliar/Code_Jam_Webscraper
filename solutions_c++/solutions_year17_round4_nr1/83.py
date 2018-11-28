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
const int MAXP = 4;

int dp[MAXN][MAXN][MAXN][MAXP];

void solve(int num)
{
    FORW(i,0,MAXN) FORW(j,0,MAXN) FORW(k,0,MAXN) FORW(r,0,MAXP) dp[i][j][k][r] = -1000000;

    int N, P;
    cin >> N >> P;
    int ans = 0;
    vector<int> v(MAXP,0);
    FORW(i,0,N) {
        int g;
        cin >> g;
        v[g%P]++;
    }
    ans += v[0];

    dp[v[1]][v[2]][v[3]][0] = 0;
    int s = v[1]+v[2]+v[3];
    FORD(ss,s,1) {
        FOR(i,0,ss) FOR(j,0,ss-i) {
            int k = ss - i - j;
            vector<int> w = {0,i,j,k};
            FORW(r,0,MAXP) {
                FORW(q,1,4) if(w[q]) {
                    int tmp = dp[i][j][k][r] + (r==0);
                    int nr = (r+q)%P;
                    w[q]--;
                    dp[w[1]][w[2]][w[3]][nr] = max(dp[w[1]][w[2]][w[3]][nr],tmp);
                    w[q]++;
                }
            }
        }
    }
    int rem = 0;
    FORW(i,0,P) rem = max(rem, dp[0][0][0][i]);
    ans += rem;

    cout << "Case #" << num << ": " << ans << "\n";

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
