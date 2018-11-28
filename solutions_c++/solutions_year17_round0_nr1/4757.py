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
#define itn int
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
	string s;
	int n, k;
	cin >> s >> k;
	n = s.size();
	int ans = 0;
	for (int i = 0; i <= n - k; i++)
	{
		if (s[i] == '-')
		{
			ans++;
			for (int j = 0; j < k; j++)
			{
				if (s[i + j] == '+')
					s[i + j] = '-';
				else
					s[i + j] = '+';
			}
		}
	}
	for (int i = 0; i < n;i++)
		if (s[i] == '-')
		{
			cout << "IMPOSSIBLE\n";
			return 0;
		}

	cout << ans << endl;






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
	/*
	freopen("input.txt", "w", stdout);
	int n = 2e5;
	cout << n << endl;
	for (int i = 0; i < n; i++)
		cout << 0 << ' ' << i+1 << endl;


	return 0;*/
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

	return 0;
}