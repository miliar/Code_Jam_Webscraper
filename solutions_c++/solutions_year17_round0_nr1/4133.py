#include <iostream>
#include <vector>
#include <string>

using namespace std;
string s;
int n, k;
long long res, ans;

void change(int left)
{
	for (int i = left; i < left + k; i++)
	{
		if (s[i] == '+')
			s[i] = '-';
		else
			s[i] = '+';
	}
}

bool check()
{
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] != '+')
			return false;
	}
	return true;
}

int main()
{
	ios::sync_with_stdio(false);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		ans = 0;
		cin >> s >> k;
		int ind = 0;
		while (ind + k <= s.size())
		{
			if (s[ind] == '+')
			{
				ind++;
				continue;
			}
			else
			{
				change(ind);
				ans++;
				ind++;
			}
		}

		cout << "Case #" << i + 1 << ": ";
		if (check())
		{
			cout << ans << endl;
		}
		else
		{
			cout << "IMPOSSIBLE" << endl;
		}

	}
}