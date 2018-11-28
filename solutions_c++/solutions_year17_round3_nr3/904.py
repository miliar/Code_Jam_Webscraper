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
	int n, k;
	cin >> n >> k;
	double u;
	cin >> u;
	vd q(n);
	for (int i = 0; i < n;i++)
		cin >> q[i];
	
	sort(q.begin(), q.end());
	double ans = 0.0;
	for (int i = n - k; i < n; i++)
	{
		if (u < eps)
			break;
		double qw = 0;
		for (int j = n - k; j < i; j++)
			qw += q[i] - q[j];
		double add = min(u / (i - (n - k)), qw / (i - (n - k)));
		for (int j = n - k; j < i; j++)
		{
			q[j] += add;
			u -= add;
		}
	}
	if (u > eps)
	{
		double add = u / (k);
		for (int i = n - k; i < n; i++)
		{
			q[i] += add;
		}
	}
	vvd dp(n + 1, vd(k + 1, 0));
	dp[0][0] = 1;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j <= k; j++)
		{
			if (j != k){
				dp[i + 1][j] += dp[i][j] * (1 - q[i]);
				dp[i + 1][j + 1] += dp[i][j] * q[i];
			}
			else
			{
				dp[i + 1][j] += dp[i][j];
			}
		}
	}
	cout <<fixed << setprecision(10) << dp[n][k] << endl;


	return 0;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
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