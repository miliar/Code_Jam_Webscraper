#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t, i, k, l, j, flag;
	string s;
	cin >> t;
	int count[t];
	for(i = 0; i < t; i++)
		count[i] = 0;
	for(i = 0; i < t; i++)
	{
		cin >> s;
		cin >> k;
		for(j = 0; j <= s.length() - k; j++)
		{
			if(s[j] == '+') continue;
			else if(s[j] == '-')
			{
				count[i]++;
				for(l = j; l < j + k; l++)
				{
					if(s[l] == '+') s[l] = '-';
					else if(s[l] == '-') s[l] = '+';
				} 
			}
		}
		for(j = s.length() - k + 1; j < s.length(); j++)
		{
			if(s[j] == '-')
			{
				count[i] = -1;
				break;
			}
		}
	}
	for(i = 0; i < t; i++)
	{
		if(count[i] == -1)
		{
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << "Case #" << i + 1 << ": " << count[i] << endl;
		}
	}
	return 0;
}