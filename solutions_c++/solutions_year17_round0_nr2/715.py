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

int dp[20][10][2];

int solve(string s) {
    memset(dp, -1, sizeof(dp));
    int len = (int)s.length();
    int init = s[0] - '0';
    rep(i,0,init) dp[0][i][1] = i;
    dp[0][init][0] = init;

    rep(i,1,len) {
        rep(j,0,10) {
            int prev = s[i-1] - '0';
            int cur  = s[i]   - '0';

            // k = 0 => j is same as cur
            if(j == cur) {
                if(prev <= cur) {
                    if(dp[i-1][prev][0] != -1)
                        dp[i][j][0] = dp[i-1][prev][0] * 10 + j;
                }
                else {
                    dp[i][j][0] = -1;
                }
            }

            // k = 1 => j is might not same as cur
            if(j < cur) {
                if(prev <= j) {
                    if(dp[i-1][prev][0] != -1)
                        dp[i][j][1] = max(dp[i][j][1], dp[i-1][prev][0] * 10 + j);
                }
            }

            rep(x,0,10) {
                if(x <= j) {
                    if(dp[i-1][x][1] != -1)
                        dp[i][j][1] = max(dp[i][j][1], dp[i-1][x][1] * 10 + j);
                }
            }

            // printf("dp[%lld][%lld][0] = %lld, dp[%lld][%lld][1] = %lld\n", i, j, dp[i][j][0], i, j, dp[i][j][1]);
        }
    }

    int ret = 0;
    rep(i,0,10) rep(j,0,2) {
        // printf("i = %lld, j = %lld, dp = %lld\n", i, j, dp[len-1][i][j]);
        ret = max(ret, dp[len-1][i][j]);
    }
    return ret;
}

signed main() {
    int t; cin >> t;
    rep(i,0,t) {
        string n; cin >> n;
        int ans = solve(n);
        printf("Case #%lld: %lld\n", i+1, ans);
    }
    return 0;
}