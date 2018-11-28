#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
int t;
ll n;
string s;
int dp[20][10][2];
int path[20][10][2];

int solve(int curr, int l, int f)
{
	if (curr == s.size())
	{
		return 1;
	}
	
	int & ret = dp[curr][l][f];
	if (ret != -1)
		return ret;
		
	ret = 0;
	int digit = s[curr] - '0';
	if (f)
	{
		if (digit >= l)
		{
			ret = solve(curr + 1, digit, f);
			if (ret)
			{
				path[curr][l][f] = digit;
				return ret;
			}
		}
		for (int i = digit - 1; i >= l; --i)
		{
			ret = solve(curr + 1, i, 0);
			
			if (ret)
			{
				path[curr][l][f] = i;
				return ret;
			}
		}
	}
	else
	{
		for (int i = 9; i >= l; --i)
		{
			ret = solve(curr + 1, i, 0);
			if (ret)
			{
				path[curr][l][f] = i;
				return ret;
			}
		}
	}
	return ret;
}

void getPath(int curr, int l, int f, string &ans)
{
	if (curr == s.size())
		return;
	int ff = f;
	if (f and path[curr][l][f] < s[curr] - '0')
		ff = 0;
	ans += path[curr][l][f] + '0';
	getPath(curr + 1, path[curr][l][f], ff, ans);
}

int main(void)
{
	ios :: sync_with_stdio(false);
	cin >> t;
	
	for (int i = 1; i <= t; ++i)
	{
		s.clear();
		cin >> n;
		while (n)
		{
			s += n%10 + '0';
			n /= 10;
		}
		reverse(s.begin(), s.end());
		memset(dp, -1, sizeof dp);
		memset(path, -1, sizeof path);
		string ans;
		solve(0, 0, 1);
		getPath(0, 0, 1, ans);
		ll ansn = 0;
		for (int j = 0; j < ans.size(); ++j)
		{
			ansn *= 10LL;
			ansn += ans[j] - '0';
		}
		cout << "Case #" << i << ": " << ansn << "\n";
	}
	return 0;
}
