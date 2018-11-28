#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ll;

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		string s;
		cin >> s;
		s = '0' + s;

		char last = '0';
		for(int i = 0; i < s.size(); ++i)
		{
			if(s[i] < last)
			{
				int j;
				for(j = i - 1; j >= 0; --j)
				{
					if(s[j] < last) 
					{
						++j;
						s[j] -= 1; 
						break;
					}
				}
				for(++j;j < s.size(); ++j)
					s[j] = '9';
				break;
			}
			else
			{
				last = s[i];
			}
		}

		cout << stoll(s) << "\n";

	}
}
