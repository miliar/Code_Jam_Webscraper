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

int n,k,l[1005],r[1005],c[1005];

int mn(int p) {
    return min(abs(l[p]-p), abs(r[p]-p));
}

int mx(int p) {
    return max(abs(l[p]-p), abs(r[p]-p));
}

ii mp(int p) {
    return ii(mn(p), mx(p));
}

int find() {
    int ans;
    rep(i,1,n) if (c[i]) {ans=i; break;}
    rep(i,1,n) if (c[i] && mp(i) > mp(ans)) ans = i;
    return ans;
}

void update(int p) {
    c[p]=0;
    rep(i,1,p-1) r[i]=min(r[i],p-1);
    rep(i,p+1,n) l[i]=max(l[i],p+1);
}

int main() {
    int tc, testcase=1;
    R(tc);
    while (tc--) {
        R(n,k);
        rep(i,1,n) l[i]=1,r[i]=n,c[i]=1;
        while (k>1) {
            update(find());
            k--;
        }
        int p = find();
        printf("Case #%d: %d %d\n", testcase++, mx(p),mn(p));
    }
    return 0;
}