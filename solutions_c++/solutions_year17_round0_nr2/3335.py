#include <bits/stdc++.h>
#define ll long long
using namespace std;
bool lesser(string &s, int i, ll ans)
{
	ll n = 0;
	for(int j = 0; j <= i; j++)
		n = (n * 10 + s[j] - '0');
	if(ans <= n)
		return true;
	else
		return false;
}
bool tidy_number(string &s, ll &ans, int i, int m)
{
	if(i == s.length())
		return true;
	ans *= 10;
	for(int j = 9; j >= m; j--)
	{
		if(!lesser(s, i, ans + j))
			continue;
		ans += j;
		if(!tidy_number(s, ans, i + 1, j))
			ans -= j;
		else
			return true;
	}
	ans /= 10;
	return false;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	string s;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cin >> s;
		ll ans = 0;
		tidy_number(s, ans, 0, (s[0] - '0') - 1);
		cout << "Case #" << i << ": " << ans << "\n";
	}
	return 0;
}
