
#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef set<int> SI;
typedef pair<int, int> PII;
typedef vector<pair<int, int> > VPII;

const int INF = 1000000001;
const int EPS = 1e-9;
const int MOD = 1000000007;
const LL LLINF = 1000000000000000001;

//813437586

#define FOR(i, b, e) for(int i = b; i <= e; i++)
#define FORD(i, b, e) for(int i = b; i >= e; i--)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define VAR(v, n) auto v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)

#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define GGL(x) "Case #" << x << ": "


/*************************** END OF TEMPLATE ***************************/


const int daym = 1442;

int main()
{
	ios_base::sync_with_stdio(false);
	int W;
	cin >> W;
	FOR(cc, 1, W)
	{
		int fr[daym];
		FOR(i, 0, daym-1)
			fr[i] = 2;

		int c, j;
		cin >> c >> j;

		FOR(i, 1, c)
		{
			int b, e;
			cin >> b >> e;
			FOR(j, b, e-1)
				fr[j] = 1;
		}
		FOR(i, 1, j)
		{
			int b, e;
			cin >> b >> e;
			FOR(j, b, e-1)
				fr[j] = 0;
		}
		int ans = INF;
		/*
		cout << endl;
		FOR(i, 0, 1439)
			cout << fr[i];
		cout << endl;
		*/

		if(fr[0] != 0)
		{
			int dp[daym][daym][3];
			dp[0][1][0] = 0;
			dp[0][0][0] = INF;
			FOR(i, 2, 720)
				dp[0][i][0] = INF;
			FOR(i, 0, 720)
				dp[0][i][1] = INF;

			FOR(i, 1, 1439)
			{
				if(fr[i] == 0)
				{
					FOR(j, 0, 720)
						dp[i][j][0] = INF;
				}
				else
				{
					dp[i][0][0] = INF;
					FOR(j, 1, 720)
						dp[i][j][0] = min(dp[i-1][j-1][0], dp[i-1][j-1][1] + 1);
				}
				if(fr[i] == 1)
				{
					FOR(j, 0, 720)
						dp[i][j][1] = INF;
				}
				else
				{
					FOR(j, 0, 720)
						dp[i][j][1] = min(dp[i-1][j][1], dp[i-1][j][0] + 1);
				}
			}
			ans = min(ans, dp[1439][720][0]);
			ans = min(ans, dp[1439][720][1] + 1);
		}
		if(fr[0] != 1)
		{
			int dp[daym][daym][3];
			dp[0][0][1] = 0;
			FOR(i, 0, 720)
				dp[0][i][0] = INF;
			FOR(i, 1, 720)
				dp[0][i][1] = INF;

			FOR(i, 1, 1439)
			{
				if(fr[i] == 0)
				{
					FOR(j, 0, 720)
						dp[i][j][0] = INF;
				}
				else
				{
					dp[i][0][0] = INF;
					FOR(j, 1, 720)
						dp[i][j][0] = min(dp[i-1][j-1][0], dp[i-1][j-1][1] + 1);
				}
				if(fr[i] == 1)
				{
					FOR(j, 0, 720)
						dp[i][j][1] = INF;
				}
				else
				{
					FOR(j, 0, 720)
						dp[i][j][1] = min(dp[i-1][j][1], dp[i-1][j][0] + 1);
				}
			}
			//cout << dp[1439][720][0] << endl;
			ans = min(ans, dp[1439][720][0] + 1);
			ans = min(ans, dp[1439][720][1]);
		}

		cout << GGL(cc) << ans << endl;

	}


}