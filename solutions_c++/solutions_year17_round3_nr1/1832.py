// Nguyen Cao Nhat Long
// Pikachuuuuuuuuuuuuu
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <set>
#include <queue>
#include <vector>
#include <stack>
#include <map>
#include <string>
#include <sstream>
using namespace std;

#define next oapsidfjiuunfiujfa
#define prev sdofljkauohfaodisf

#define sqr(x) ((x)*(x))
#define PI acos(-1)

#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define REP(i,a) for(int i = 0, _a = (a); i < _a; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)

#define ii pair<int,int>
#define fi first
#define se second
#define mp make_pair

#define sz(x) (int)x.size()
#define ALL(x) (x).begin(), (x).end()
#define MS(a,x) memset(a, x, sizeof(a))

#define sync ios::sync_with_stdio(false)

#define ll long long
#define vi vector<int>
#define vll vector<ll>
#define vii vector<ii>
#define pb push_back

#define inf 1000000000
#define INF 100000000000000000LL
#define mod 1000000007LL
#define maxn 1001

// End of template

#define pdd pair<long double,long double>

pdd cake[maxn];
long double dp[maxn][maxn];

int main()
{
    freopen("codejam.inp", "r", stdin);
    freopen("codejam.out", "w", stdout);

	//sync;
    //cin.tie(0); cout.tie(0);

    int nTest;
    cin >> nTest;

    FOR(test, 1, nTest)
    {
        int n, k;
        cin >> n >> k;

        REP(i, n) cin >> cake[i].fi >> cake[i].se;

        sort(cake, cake + n);
        reverse(cake, cake + n);

        REP(i, n)
            FOR(j, 1, k)
                dp[i][j] = 0;

        REP(i, n) {
            long double gg = 0;
            gg += 2 * 1.0 * PI * cake[i].fi * cake[i].se;
            gg += PI * sqr(cake[i].fi);

            dp[i][1] = gg;
            if(i > 0)
                dp[i][1] = max(dp[i][1], dp[i - 1][1]);
        }

        FOR(j, 2, k)
            FOR(i, 1, n - 1)
            {
                if(j - 1 > i) continue;

                dp[i][j] = max(dp[i - 1][j],
                               dp[i - 1][j - 1] + 2.0 * PI * cake[i].fi * cake[i].se);
            }

        printf("Case #%d: %.10lf\n", test, dp[n - 1][k]);
    }
}
