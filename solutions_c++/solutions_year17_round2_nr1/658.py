#include <bits/stdc++.h>

#define rep(i,n) for(i=0; i<n; i++)
#define repl(i,n) for(i=1; i<=n; i++)

#define sz(x) (int) x.size()
#define pb push_back
#define all(x) x.begin(),x.end()
#define uu first
#define vv second
#define mem(x, y) memset(x, y, sizeof(x))
#define un(x) x.erase(unique(all(x)), x.end())

#define sdi(x) scanf("%d", &x)
#define sdii(x, y) scanf("%d %d", &x, &y)
#define sdiii(x, y, z) scanf("%d %d %d", &x, &y, &z)
#define sdl(x) scanf("%lld", &x)
#define sdll(x, y) scanf("%lld %lld", &x, &y)
#define sdlll(x, y, z) scanf("%lld %lld %lld", &x, &y, &z)
#define sds(x) scanf("%s", x)
#define pfi(x) printf("%d\n", x)
#define pfii(x, y) printf("%d %d\n", x, y)
#define pfiii(x, y, z) printf("%d %d %d\n", x, y, z)
#define pfl(x) printf("%lld\n", x)
#define pfll(x, y) printf("%lld %lld\n", x, y)
#define pflll(x, y, z) printf("%lld %lld %lld\n", x, y, z)

#define eps 1e-9
#define OK cerr << "ok\n"
#define DB(x) cerr << #x << " = " << x << endl

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair <int, int> pii;

inline int setBit(int N, int pos) { return N=N | (1<<pos); }
inline int resetBit(int N, int pos) { return N= N & ~(1<<pos); }
inline bool checkBit(int N, int pos) { return (bool)(N & (1<<pos)); }

//int kx[] = {+2, +1, -1, -2, -2, -1, +1, +2};
//int ky[] = {+1, +2, +2, +1, -1, -2, -2, -1}; //Knight Direction
//int fx[] = {+0, +0, +1, -1, -1, +1, -1, +1};
//int fy[] = {-1, +1, +0, +0, +1, +1, -1, -1}; //Four & Eight Direction


const int MAX = 1005;
int n;
double start[MAX], speed[MAX], len;

inline bool check(double x) {
    int i;
    rep(i, n) {
        double a = len*speed[i];
        double b = (len-start[i])*x;
//        cerr << a << " " << b << endl;
        if(a < b) return false;
    }
    return true;
}

inline double bs() {
    double low = 0.0, high=1e18, mid, ret=low;
    int cnt = 300;
    while(cnt--) {
        mid = (low+high) / 2.0;
        if(check(mid)) {
            ret = max(ret, mid);
            low = mid;
        }
        else high = mid;
    }
    return ret;
}

int main() {
//    assert(freopen("in.txt","r",stdin));
//    assert(freopen("out.txt","w",stdout));
    assert(freopen("A-large.in","r",stdin));
    assert(freopen("A-large.out","w",stdout));

    int test, kase=1, i;

    sdi(test);
    while(test--) {
        cerr << kase << endl;
        scanf("%lf %d", &len, &n);
        rep(i, n) {
            scanf("%lf %lf", &start[i], &speed[i]);
        }
        printf("Case #%d: %.10f\n", kase++, bs());
    }

    return 0;
}
