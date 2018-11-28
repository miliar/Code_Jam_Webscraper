
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main(void)
{
	int t, k;
	string s;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i)
	{
		cin >> s >> k;  // read n and then m.
		int ret = 0;
		int n = s.size();
		while (n > 0)
		{
			if (s[n - 1] == '+')
			{
				--n;
				continue;
			}
			if (n < k)
			{
				break;
			}
			++ret;
			for (int j = 0; j < k; ++j)
			{
				if (s[n - 1 - j] == '-')
				{
					s[n - 1 - j] = '+';
				}
				else
				{
					s[n - 1 - j] = '-';
				}
			}
		}

		cout << "Case #" << i << ": ";
		if (n != 0)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << ret << endl;
		}
	}
}