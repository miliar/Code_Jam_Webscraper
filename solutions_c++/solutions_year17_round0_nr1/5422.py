#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		cout << "Case #" << i << ": ";
		string s;
		int k;
		cin >> s;
		cin >> k;
		int ans = 0;
		for(int j=0;j<s.size();j++)
		{
			if(s[j]=='+')
				continue;
			if((j+k)<=s.size())
			{
				ans++;
				for(int l=j;l<s.size()&&l<j+k;l++)
				{
					if(s[l]=='+')
						s[l] = '-';
					else
						s[l] = '+';
				}
			}
		}
		int flag=0;
		for(int j=0;j<s.size();j++)
		{
			if(s[j]=='-')
			{
				flag=1;
				break;
			}
		}
		if(flag)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
}