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

int main() {
    int t, testcase = 1;
    R(t);
    int a, b,c,d;
    while (t--) {
        vector<ii> as,bs;
        R(a,b);
        rep(i,0,a-1) R(c,d), as.pb(ii(c,d));
        rep(i,0,b-1) R(c,d), bs.pb(ii(c,d));
        int ans;
        if (a == 1 && b == 1) {
            ans = 2;
        } else {
            vector<ii> v = (sz(as) > 0) ? as : bs;
            sort(v.begin(), v.end());
            if (v[1].se - v[0].fi <= 720) ans = 2;
            else if (v[0].se + 1440 - v[1].fi <= 720) ans = 2;
            else ans = 4;
        }
        printf("Case #%d: %d\n", testcase++, ans);
    }
    return 0;
}