#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
int main()
{
	ios::sync_with_stdio(0);
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		string s;
		int k;
		cin>>s>>k;
		long long val = 0;
		for (int i = 0; i <= (int)s.length()-k; ++i)
		{
			if (s[i] == '-')
			{
				++val;
				for (int j = 0; j < k; ++j)
				{
					if (s[i+j] == '-') s[i+j] = '+';
					else s[i+j] = '-';
				}
			}
		}
		bool valid = true;
		for (auto c : s)
		{
			if (c == '-')
			{
				valid = false;
				break;
			}
		}
		cout<<"Case #"<<t<<": ";
		if (valid) cout<<val<<'\n';
		else cout<<"IMPOSSIBLE\n";
	}
}