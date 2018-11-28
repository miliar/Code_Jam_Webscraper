/*
Hanit Banga
*/

#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define fast_cin() ios_base::sync_with_stdio(false)

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int N = 1e5 + 5;

string solve(string s, char x = '0');

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		string s;
		cin >> s;
		string ans = solve(s, '0');
		if (ans[0] == '0')
			ans = ans.substr(1, ans.length() - 1);

		cout << ans << endl;
	}	
}

string solve(string s, char x)
{
	if (s == "")
		return "";

	int n = s.length();
	if (s[0] < x)
		return "x";

	string t = solve(s.substr(1, n - 1), max(s[0], '1'));
	if (t != "x")
		return s.substr(0, 1) + t;

	if (s[0] - 1 < x)
		return "x";

	string ans = s;
	--ans[0];
	for (int i = 1; i < n; ++i)
		ans[i] = '9';

	return ans;
}