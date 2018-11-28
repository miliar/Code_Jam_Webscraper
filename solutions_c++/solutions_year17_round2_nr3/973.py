//mohitbindal
#include <iostream>
#include <cstring>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <limits.h>
#include <vector>
#include <map>
#include <bitset>
#include <string>
#include <iterator>
#include <set>
#include <utility>
#include <queue>
#include <numeric>
#include <functional>
#include <ctype.h>	
#include <stack>
#include <algorithm>
#include <cstdlib>
#define bitcnt(x) __builtin_popcountll(x)
#define MS0(x) memset(x, 0, sizeof(x))
#define MS1(x) memset(x, -1, sizeof(x))
#define mp(x, y) make_pair(x, y)
#define inputL(x) scanf("%lld", &x)
#define input(x) scanf("%d", &x)
#define inputS(x) scanf("%s", x)
#define printL(x) printf("%lld\n", x)
#define print(x) printf("%d\n", x)
#define pi acos(-1.0)
#define ff first
#define ss second

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
const ll INF = 1e18, MAX = 105, mod = 1000000007;
ll e[MAX], s[MAX], d[MAX][MAX], dis[MAX][MAX], des, n;
long double dp[MAX][MAX], one = 1.0;

int main()
{
#ifdef LOCAL_PROJECT
    freopen("../input.txt", "r", stdin);
	freopen("../output.txt", "w", stdout);
#endif
    // ios_base::sync_with_stdio(0);	cin.tie(0);	cout.tie(0);
    int t, T, q, u, v;
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
    	cout << "Case #" << t << ": ";
    	cin >> n >> q;
    	for (int i = 0; i < n; i++)
    		cin >> e[i] >> s[i];
    	for (int i = 0; i < n; i++)
    	{
    		for (int j = 0; j < n; j++)
    		{
    			cin >> d[i][j];
    			dis[i][j] = ((d[i][j] == -1) ? INF : d[i][j]);
    		}
    		dis[i][i] = 0;
    	}
    	for (int i = 0; i < n; i++)
    	{
    		for (int j = 0; j < n; j++)
    		{
    			for (int k = 0; k < n; k++)
    			{
    				dis[j][k] = min(dis[j][k], dis[j][i] + dis[i][k]);
    			}
    		}
    	}

    	for (int i = 0; i < n; i++)
    		for (int j = 0; j < n; j++)
    		{
    			if (e[i] >= dis[i][j])
    				dp[i][j] = (dis[i][j] * one / (s[i] * one));
    			else
    				dp[i][j] = 1e18;
    		}

    	for (int i = 0; i < n; i++)
    	{
    		for (int j = 0; j < n; j++)
    		{
    			for (int k = 0; k < n; k++)
    			{
    				dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k]);
    			}
    		}
    	}

    	for (int i = 0; i < q; i++)
    	{
    		cin >> u >> v;
    		cout << fixed << setprecision(6) << dp[u - 1][v - 1] << " ";
    	}
    	cout << endl;
    }
    return 0;
}
