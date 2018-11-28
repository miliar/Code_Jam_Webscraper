#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t;
	string s;

	cin >> t;

	for (int i = 1; i <= t; ++i)
	{
		cin >> s;
		int k;
		cin >> k;
		int c = 0;

		for (int j = 0; j <= s.size()-k; ++j)
		{
			if (s[j] == '-')
			{
				c++;

				for (int l = j; l < j+k; ++l)
				{
					if (s[l] == '-')
					{
						s[l] = '+';
					}
					else
					{
						s[l] = '-';
					}
				}
			}
		}

		for (int j = 0; j < s.size(); ++j)
		{
			if (s[j] != '+')
			{
				c = -1;
			}
		}

		cout << "Case #" << i << ": ";

		if (c>=0)
		{
			cout << c << endl;
		}
		else
		{
			cout << "IMPOSSIBLE" << endl;
		}
	}
}