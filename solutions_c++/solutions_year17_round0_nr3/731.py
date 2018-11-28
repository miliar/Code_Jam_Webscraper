#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cstring>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <utility>
#include <algorithm>
#include <map>
#include <set>
#include <complex>
#include <cmath>
#include <limits>
#include <cfloat>
#include <climits>
#include <ctime>
#include <cassert>
using namespace std;

#define rep(i,a,n) for(int (i)=(a); (i)<(n); (i)++)
#define repq(i,a,n) for(int (i)=(a); (i)<=(n); (i)++)
#define repr(i,a,n) for(int (i)=(a); (i)>=(n); (i)--)
#define all(v) begin(v), end(v)
#define pb(a) push_back(a)
#define fr first
#define sc second
#define INF 2000000000
#define int long long int

#define X real()
#define Y imag()
#define EPS (1e-10)
#define EQ(a,b) (abs((a) - (b)) < EPS)
#define EQV(a,b) ( EQ((a).X, (b).X) && EQ((a).Y, (b).Y) )
#define LE(n, m) ((n) < (m) + EPS)
#define LEQ(n, m) ((n) <= (m) + EPS)
#define GE(n, m) ((n) + EPS > (m))
#define GEQ(n, m) ((n) + EPS >= (m))

typedef vector<int> VI;
typedef vector<VI> MAT;
typedef pair<int, int> pii;
typedef long long ll;

typedef complex<double> P;
typedef pair<P, P> L;
typedef pair<P, double> C;

int dx[]={1, -1, 0, 0};
int dy[]={0, 0, 1, -1};
int const MOD = 1000000007;
ll mod_pow(ll x, ll n) {return (!n)?1:(mod_pow((x*x)%MOD,n/2)*((n&1)?x:1))%MOD;}
int madd(int a, int b) {return (a + b) % MOD;}
int msub(int a, int b) {return (a - b + MOD) % MOD;}
int mmul(int a, int b) {return (a * b) % MOD;}
int minv(int a) {return mod_pow(a, MOD-2);}
int mdiv(int a, int b) {return mmul(a, minv(b));}

namespace std {
    bool operator<(const P& a, const P& b) {
        return a.X != b.X ? a.X < b.X : a.Y < b.Y;
    }
}

int t;

pii solve(int n, int k) {
    int base = 1;
    k -= 1;
    while(1) {
        if(k - base < 0) break;
        k -= base;
        n -= base;
        base *= 2;
    }

    int len = 0;
    int mo = n % base;
    int div = n / base;
    if(k < mo) len = div + 1;
    else len = div;

    int mi = (len - 1) / 2;
    int ma = len / 2;
    return pii(ma, mi);
}

signed main() {
    cin >> t;
    rep(i,0,t) {
        int n, k; cin >> n >> k;
        pii ans = solve(n, k);
        printf("Case #%lld: %lld %lld\n", i+1, ans.first, ans.second);
    }
    return 0;
}