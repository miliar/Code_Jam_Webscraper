#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		string s;
		size_t k;
		cin >> s >> k;
		int cnt = 0;
		bool truth = false;
		for (size_t i = 0; i < s.size(); i++)
		{
			if (s[i] == '-')
			{
				if (i + k > s.size())
				{
					truth = true;
					break;
				}
				for (size_t j = i; j < i + k; j++)
				{
					if (s[j] == '+')
					{
						s[j] = '-';
					}
					else
					{
						s[j] = '+';
					}
				}
				cnt++;
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if (truth)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << cnt << endl;
		}
	}
	return 0;
}
