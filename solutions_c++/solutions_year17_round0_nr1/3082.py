#include <iostream>
#include <cstring>
#include <string>

using namespace std;

void solve(int number)
{
	string s;
	cin >> s;
	int k;
	cin >> k;
	int answer = 0;
	for (int i = 0; i <= s.length() - k; i++)
	{
		if (s[i] == '-')
		{
			answer++;
			for (int j = i; j < i + k; j++)
			{
				if (s[j] == '-')
					s[j] = '+';
				else
					s[j] = '-';
			}
		}
	}
	cout << "Case #" << number << ": ";
	for (int i = 0; i < s.length(); i++)
	{
		if (s[i] == '-')
		{
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << answer << endl;
	return;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		solve(i);
	}
	return 0;
}