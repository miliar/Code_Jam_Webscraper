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
#ifdef LOCAL
    #define D(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
    #define D(...) ;
    #define cerr if(0)cout
#endif
using namespace std;
template<typename T, typename U> ostream& operator << (ostream& os, const pair<T, U> &_p) { return os << "(" << _p.X << "," << _p.Y << ")"; }
template<typename T> ostream& operator << (ostream &os, const vector<T>& _V) { bool f = true; os << "["; for(auto v: _V) { os << (f ? "" : ",") << v; f = false; } return os << "]"; }
template<typename T> ostream& operator << (ostream &os, const set<T>& _S) { bool f = true; os << "("; for(auto s: _S) { os << (f ? "" : ",") << s; f = false; } return os << ")"; }
template<typename T, typename U> ostream& operator << (ostream &os, const map<T, U>& _M) { return os << set<pair<T, U>>(ALL(_M)); }
template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) { while(*sdbg!=',')cerr<<*sdbg++;cerr<<'='<<h<<", "; _dbg(sdbg+1, a...); }

typedef signed long long slong;
typedef long double ldouble;
const slong INF = 1000000100;
const ldouble EPS = 1e-9;

const int MAXN = 1000101;
slong N, K;

void read_data() {
    scanf("%lld %lld\n", &N, &K);
}

void solve() {
    map<slong, slong> M;
    M[N]++;
    slong last_size = -1;
    while(K > 0) {
        slong size, cnt;
        tie(size, cnt) = *M.rbegin();
        M.erase(M.rbegin()->X);
        slong new_cnt = min(K, cnt);
        last_size = size;
        K -= new_cnt;
        M[(size-1)/2] += new_cnt;
        M[size/2] += new_cnt;
    }
    printf("%lld %lld", (last_size)/2, (last_size-1)/2);
}

int main() {
    int z;
    scanf("%d", &z);
    FOR(_,1,z) {
        printf("Case #%d: ", _);
        read_data();
        solve();
        printf("\n");
    }
}
