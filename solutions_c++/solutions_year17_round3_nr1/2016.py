#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second
#define pb push_back
#define fil(a,b) memset((a),(b),sizeof(a))
#define sz(x) ((int)(x).size())
#define rep(i,a,b) for (int i=(a); i <= int(b); i++)
#define per(i,a,b) for (int i=(a); i >= int(b); i--)
#define foreach(it,c) for (auto it=(c).begin(); it != (c).end(); it++)

template<typename T>
void _R( T &x ) { cin>>x; }
void _R( int &x ) { scanf("%d",&x); }
void _R( long long &x ) { cin>>x; }
void _R( double &x ) { scanf("%lf",&x); }
void _R( char &x ) { scanf(" %c",&x); }
void _R( char *x ) { scanf("%s",x); }

void R() {}
template<typename T, typename... U>
void R( T& head, U&... tail ) {
    _R(head);
    R(tail...);
}

template<typename T>
void _W(const T &x) { cout << x; }
void _W(const int &x) { printf("%d", x); }
template<typename T>
void _W(const vector<T> &x) {
    for (auto i = x.cbegin(); i != x.cend(); i++) {
        if (i != x.cbegin()) putchar(' ');
        _W(*i);
    }
}

void W() {}
template<typename T, typename... U> void W(const T& head, const U&... tail) {
    _W(head);
    putchar(sizeof...(tail) ? ' ' : '\n');
    W(tail...);
}

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef double db;

const int inf = 0x3f3f3f3f;
// const ll inf = 0x3f3f3f3f3f3f3f3f;
const db pi = 3.14159265358979323846264338327950288L;
const db eps = 1e-6;
const int mo = 1e9+7;

typedef pair<double, double> dd;

int n,k;
vector<dd> rh;
map<int, map<int, map<int, double>>> memo;

double solve(int cur, int last, int kleft) {
    if (cur == n || kleft == 0) return 0;
    if (memo[cur][last][kleft] > 0) return memo[cur][last][kleft];
    double ret = 2 * pi * rh[cur].fi * rh[cur].se;
    if (last == -1) ret += pi * rh[cur].fi * rh[cur].fi;
    ret += solve(cur+1,cur,kleft-1);
    ret = max(ret, solve(cur+1,last,kleft));
    return memo[cur][last][kleft] = ret;
}

int main() {
    int t, testcase = 1;
    R(t);
    double r,h;
    while (t--) {
        memo.clear();
        rh.clear();
        R(n,k);
        rep(i,0,n-1) R(r,h), rh.pb(dd(r,h));
        sort(rh.begin(),rh.end(),greater<dd>());
        double ans = solve(0,-1,k);
        printf("Case #%d: %.10lf\n", testcase++, ans);
    }
    return 0;
}