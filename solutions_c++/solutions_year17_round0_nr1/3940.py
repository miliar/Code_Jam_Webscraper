#include <iostream>
#include <cstdlib>
#include <cmath>
#include <functional>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <list>
#include <map>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int c = 1; c <= t; c++)
	{
		cout << "Case #" << c << ": ";

		string s;
		int k;
		cin >> s >> k;
		int flips = 0;

		for (int i = 0; i < s.length() - k + 1; i++)
		{
			if (s[i] == '-')
			{
				flips++;
				for (int j = 0; j < k; j++)
				{
					if (s[i + j] == '-')
						s[i + j] = '+';
					else
						s[i + j] = '-';
				}
			}
		}

		bool possible = true;
		for (int i = 0; i < s.length(); i++)
		{
			if (s[i] != '+')
			{
				possible = false;
				break;
			}
		}
		if (!possible)
		{
			cout << "IMPOSSIBLE";
		}
		else
		{
			cout << flips;
		}
		cout << "\n";
	}
	return 0;
}