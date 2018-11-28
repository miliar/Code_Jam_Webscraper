#include <bits/stdc++.h>
using namespace std;

void solve()
{
	string s; cin >> s;
	while(true)
	{
		for(int i = 0; i < s.size() - 1; ++i)
		{
			if(s[i] > s[i + 1])
			{
				if(i == 0 && s[i] == '1')
				{
					s.erase(0, 1);
					for(int j = 0; j < s.size(); ++j) s[j] = '9';
				}
				else
				{
					s[i] -= 1;
					for(int j = i + 1; j < s.size(); ++j) s[j] = '9';
				}
				goto resume;
			}
		}
		break;
		resume:;
   }
   cout << s;
}

int main()
{
	int t; cin >> t;
	for(int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
        solve();
		cout << endl;
	}
	return 0;
}
