#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;

string rever(string s, int l, int r)
{
	for (int i = l; i <= r; ++i)
	{
		if (s[i] == '+')
			s[i] = '-';
		else
			s[i] = '+';
	}
	return s;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		string s;
		cin >> s;
		int k;
		cin >> k;
		int count = 0;

		for (int i = 0; i < s.length() - k + 1; ++i)
		{
			if (s[i] == '-')
			{
				s = rever(s, i, i + k - 1);
				++count;
			}
		}

		for (int i = s.length() - 1; i >= k - 1; --i)
		{
			if (s[i] == '-')
			{
				s = rever(s, i - k + 1, i);
				++count;
			}
		}

		bool res = false;
		for (int i = 0; i < s.length(); ++i)
		{
			if (s[i] == '-')
			{
				res = true;
				break;
			}
		}

		if(!res)
			cout << "Case #" << i + 1 << ": " << count << '\n';
		else
			cout << "Case #" << i + 1 << ": IMPOSSIBLE\n";
	}
	return 0;
}