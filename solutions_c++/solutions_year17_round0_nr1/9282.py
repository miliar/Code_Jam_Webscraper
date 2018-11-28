#include <iostream>
#include <string>

using namespace std;

int solve(string s, int k)
{
	int count = 0, current = 0;
	int n = s.length();

	for (int i = 0; i < n; ++i)
	{
		for (int j = current; j < n; ++j)
		{
			if (s[j] == '-' && j + k - 1 < n)
			{
				++count;
				current = j;

				for (int l = current; l <= j + k - 1; ++l)
				{
					if (s[l] == '-') s[l] = '+';
					else s[l] = '-';
				}

				current = j + 1;
			}
		}
	}

	for (int i = 0; i < n; ++i)
	{
		if (s[i] == '-')
		{
			return -1;
		}
	}

	return count;
}

int main()
{
	int t, k;
	string s;

	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cin >> s >> k;
		int count = solve(s, k);

		cout << "Case #" << i << ": ";
		if (count == -1)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << count << endl;
		}
	}

	return 0;
}