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
    int n, R, O, Y, G, B, V;
    cin >> n >> R >> O >> Y >> G >> B >> V;
    string ans(n,'a');

    cout << "Case #" << num << ": ";
    if(2*max(R,max(Y,B)) <= n) {
        vector<pair<char,int> > v = {{'R',R}, {'Y',Y}, {'B',B}};
        while(42) {
            int i = 0;
            vector<int> pos;
            for(int j=0; j<n; j+=2) pos.PB(j);
            for(int j=1; j<n; j+=2) pos.PB(j);
            FOR(k,0,2) {
                FOR(j,1,v[k].Y) {
                    ans[pos[i]] = v[k].X;
                    i++;
                }
            }
            /*FOR(j,1,v[1].Y) {
                ans[pos[i]] = v;
                i++;
            }
            FOR(j,1,B) {
                ans[pos[i]] = 'B';
                i++;
            }*/
            int fail = 0;
            FORW(i,0,n-1) if(ans[i] == ans[i+1]) fail = 1;
            if(ans[0] == ans[n-1]) fail = 1;
            if(!fail) {
                cout << ans << "\n";
                break;
            }
            if(!next_permutation(ALL(v))) {
                cout << ".....\n";
                assert(0);
                break;
            }
        }
    }
    else cout << "IMPOSSIBLE\n";
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
