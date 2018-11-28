#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
int main()
{
	ios::sync_with_stdio(0);
	int T;
	cin>>T;
	int tx = 1;
	while (T--)
	{
		string s;
		cin>>s;
		int cp = -1;
		for (int i = 0; i < s.length() - 1; ++i)
		{
			if (s[i] > s[i+1])
			{
				cp = i;
				break;
			}
		}
		cout<<"Case #"<<tx++<<": ";
		if (cp == -1)
		{
			cout<<s<<'\n';
			continue;
		}
		for (int i = cp+1; i < s.length(); ++i)
		{
			s[i] = '9';
		}
		s[cp]--;
		for (int i = cp; i > 0; --i)
		{
			if (s[i-1] > s[i])
			{
				s[i-1]--;
				s[i] = '9';
			}
			else
				break;
		}
		if (s[0] == '0')
			s = s.substr(1, s.length()-1);
		cout<<s<<'\n';
	}

}