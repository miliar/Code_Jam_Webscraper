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

bool ch(int i)
{
	int q = 10;
	while (i)
	{
		int n = i % 10;
		if (n > q)
			return false;
		q = n;
		i /= 10;
	}
	return true;

}

int sol(string s)
{
	int n = 0;
	while (s.size())
	{
		n *= 10;
		n += s[0] - '0';
		s=s.substr(1);
	}
	for (int i = n; i >= 0; i--)
	{
		if (ch(i))
			return i;
	}



}

ll solve()
{
	string s;
	cin >> s;
	int n = s.size();
	int sm = n;
	for (int i = n - 1; i >= 1; i--)
	{
		if (s[i - 1] <= s[i])
			continue;
		else
		{
			sm = i;
			s[i - 1]--;
		}
	}
	for (int i = sm; i < n; i++)
		s[i] = '9';
	int q = 0;
	for (int i = 0; i < n;i++)
		if (s[i] != '0')
		{
			q = i; break;
		}
	s = s.substr(q);
	cout << s << endl;
	



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