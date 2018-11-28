#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
//libs
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <complex>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <queue>
#include <numeric>

using namespace std;
//defines
#define infll 3e18
#define inf 2e9
#define ll long long
#define itn ll
#define vi vector<int>
#define vvi vector<vi>
#define vd vector<double>
#define vvd vector<vd>
#define pii pair<itn,itn> 
#define pb  push_back
#define mp  make_pair
#define ld  double
#define sq(x)  (x)*(x)
#define all(x) x.begin(), x.end()
//constants
const double eps = 1e-7;
const ll mod = 1000000007;
const ll N = 10001;
const ll alp = 26;
//end of definition

ll solve()
{
	int n;
	cin >> n;
	int k;
	cin >> k;
	vvd dp(n+1, vd(k+1, -1));
	dp[0][0] = 0;
	vector<pii> q(n);
	for (int i = 0; i < n; i++)
		cin >> q[i].first >> q[i].second;
	sort(q.begin(), q.end());
	reverse(q.begin(), q.end());
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < k; j++)
		{
			if (dp[i][j] < 0)
				continue;
			dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);
			if (j == 0) dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (2.0*M_PI*q[i].first*q[i].second) + (M_PI*q[i].first*q[i].first));
			else dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (2.0*M_PI*q[i].first*q[i].second));
		}
	}
	double ans = 0;
	for (int i = 0; i <= n; i++)
		ans = max(ans, dp[i][k]);
	cout << fixed << setprecision(10) << ans << endl;

	return 0;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}


	return 0;
}