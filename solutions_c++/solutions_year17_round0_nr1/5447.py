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
    int tc, testcase=1;
    R(tc);
    while (tc--) {
        string s;
        int k, ans = 0;
        R(s,k);
        rep(i,0,sz(s)-k) {
            if (s[i] == '-') {
                ans++;
                rep(j,i,i+k-1) {
                    s[j] = s[j] == '-' ? '+' : '-';
                }
            }
        }
        bool p = true;
        rep(i,0,sz(s)-1) if (s[i] == '-') p = false;
        if (!p) printf("Case #%d: IMPOSSIBLE\n", testcase++);
        else printf("Case #%d: %d\n", testcase++, ans);
    }
    return 0;
}