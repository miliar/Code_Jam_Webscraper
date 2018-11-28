#include <bits/stdc++.h>
using namespace std;

int find(string s)
{
	for (int i = 1 ; i < s.length() ; i++)
		if (s[i] < s[i-1]) return i;
	return -1;
}

main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	string s;
	cin >> t;
	for (int i = 1 ; i <= t ; i++)
	{
		cin >> s;
		string ans = "";
		int p = find(s);
		if (p == -1) ans = s;
		else
		{
			int mem = 0;
			s[p] = 9;
//			if (s[p-1]-48 == 0) s[p-1] = '9';
//			else s[p-1] = char(s[p-1]-1);
			for (int j = p ; j > 0 ; j--)
			{
				if (s[j] < s[j-1])
				{
					s[j] = '9';
					s[j-1] = char(s[j-1]-1);
				}
			}
			for (int j = p+1 ; j < s.length() ; j++)
				s[j] = '9';
			ans = s;
			if (ans[0] == '0') ans.erase(0,1);
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}
