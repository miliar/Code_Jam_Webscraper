#include <iostream>
#include <cstring>
#include <string>

using namespace std;

string s, ans;
int len;

bool check()
{
	for (int i = 0; i < len; i++)
	{
		if (s[i] != ans[i])
			return ans[i] < s[i];
	}
	return true;
}

void solve(int number)
{
	cin >> s;
	len = s.length();
	ans = s;
	for (int i = 0; i < len; i++)
	{
		ans[i] = '1';
	}
	cout << "Case #" << number << ": ";
	if (!check())
	{
		for (int i = 1; i < len; i++)
			cout << '9';
		cout << endl;
		return;
	}
	for (int i = 0; i < len; i++)
	{
		while (true)
		{
			if (ans[i] == '9')
				break;
			for (int j = i; j < len; j++)
				ans[j]++;
			if (!check())
			{
				for (int j = i; j < len; j++)
					ans[j]--;
				break;
			}
		}
	}
	for (int i = 0; i < len; i++)
		cout << ans[i];
	cout << endl;
	return;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		solve(i);
	}
	return 0;
}