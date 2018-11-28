#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

int const INF = 1e9 + 10;
ll const BINF = 1e18 + 10;
int const MAXN = 1e6 + 10;
ld const EPS = 1e-6;
ld const PI = 3.141592653589793238462;

#define f first
#define sec second
#define pb push_back
#define pii pair<int, int>
#define pll pair<ll, ll>
#define mk make_pair
#define forn(i, n) for (int i = 1; i <= n; i++)
#define fore(i, n) for (int i = 0; i < n; i++)

vector <pll> Vec;
ll n, k, sum, last, max1 = -1, ts, dp[1001][1001];
ld ans;
bool t;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    srand(time(0));
    cin >> ts;
    forn(l, ts)
    {
        max1 = -1;
        Vec.clear();
        cin >> n >> k;
        Vec.resize(n);
        fore(i, n)
        {
            cin >> Vec[i].f >> Vec[i].sec;
        }
        sort(Vec.begin(), Vec.end());
        forn(i, k)
        forn(j, n)
        {
            dp[i][j] = -1;
        }

        for(int i = 1; i <= k; i++)
        for(int j = i - 1; j < n; j++)
        {
            if (i == 1)
            {
                dp[i][j] = Vec[j].f * Vec[j].f + 2 * Vec[j].f * Vec[j].sec;
                continue;
            }
            for(int j1 = j - 1; j1 >= 0; j1--)
            {
                dp[i][j] = max(dp[i][j], dp[i - 1][j1] + (Vec[j].f * Vec[j].f - Vec[j1].f * Vec[j1].f) + 2 * Vec[j].f * Vec[j].sec);
            }
        }

        fore(i, n)
        {
            max1 = max(max1, dp[k][i]);
            //cout << dp[k][i] << endl;
        }

        ans = ld(ld(max1) * PI);
        cout << "Case #" << l << ": ";
        cout << fixed << setprecision(10) << ans << endl;
    }



    return 0;
}
