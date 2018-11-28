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

int n,q;
double d,e[105],s[105],dist[105], memo[105][105];

double solve(int city, int horse) {
    if (city == n-1) {
        return 0;
    }
    if (memo[city][horse] > 0) return memo[city][horse];
    double ret = DBL_MAX;
    // not change
    double td = 0;
    rep(i,horse,city) td += dist[i];
    double el = e[horse] - td;
    if (el >= 0) {
        ret = min(ret, solve(city+1,horse) + dist[city] / s[horse]);
    }
    if (e[city] >= dist[city]) {
        ret = min(ret, solve(city+1,city) + dist[city] / s[city]);
    }
    return memo[city][horse] = ret;
}

int main() {
    int t, testcase = 1;
    R(t);
    while (t--) {
        R(n,q);
        rep(i,0,n-1) R(e[i],s[i]);
        rep(i,0,n-1) {
            rep(j,0,n-1) {
                R(d);
                if (i+1==j) dist[i] = d;
                memo[i][j] = -1;
            }
        }
        int u,v;
        R(u,v);
        double ans = solve(0,0);
        printf("Case #%d: %.10lf\n", testcase++, ans);
    }
    return 0;
}