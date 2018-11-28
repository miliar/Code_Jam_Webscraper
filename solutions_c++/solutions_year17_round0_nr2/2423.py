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
string A;
int N;

void read_data() {
    char buff[13123];
    scanf("%s", buff);
    A = string(buff);
    N = SIZE(A);
}

slong parse(string s) {
    slong t;
    sscanf(s.c_str(), "%lld", &t);
    return t;
}

void solve() {
    slong result = -1;
    bool bad = false;

    
    if(A[0] != '1') {
        string Q = A;
        --Q[0];
        FORW(j,1,N) Q[j] = '9';
        result = max(result, parse(Q));
    }

    FORW(i,0,N-1) {
        string S = A;
        if(S[i] < S[i+1]) {
            --S[i+1];
            FORW(j,i+2,N) S[j] = '9';
            result = parse(S);
        } else if(S[i] > S[i+1]) {
            bad = true;
            break;
        }
    }
    if(!bad) result = parse(A);
    slong t = 0;
    while(t < parse(A)) {
        t *= 10;
        t += 9;
        if(t <= parse(A)) result = max(result, t);
    }
    printf("%lld", result);
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
