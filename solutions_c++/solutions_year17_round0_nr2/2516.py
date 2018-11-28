#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
#define BR __int("$3");

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt)
	{
		string s;
		cin >> s;
		int n = s.length();
		int i = 1;
		while ((i < n) && (s[i] >= s[i-1])) ++i;
		if (i < n)
		{
			--i;
			--s[i];
			while ((i > 0) && (s[i] < s[i-1]))
			{
				--i;
				--s[i];
			}
			++i;
			while (i < n)
			{
				s[i] = '9';
				++i;
			}
		}
		bool b = false;
		cout << "Case #" << tt << ": ";
		for (int j = 0; j < n; ++j)
		{
			if (b || s[j] != '0')
			{
				b = true;
				cout << s[j];
			}
		}
		cout << endl;
	}
	return 0;
}
