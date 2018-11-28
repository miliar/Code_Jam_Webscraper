#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int cs = 1; cs <= t; cs++)
	{
		int k,k2,odd;
		string s;
		cin>>s>>k;
		k2 = k/2;
		odd = k%2;
		int len = s.length();
		int res = 0, fail = 0;
		char ch;
		int oddn;
		int found = 0;
		for(int i=0;i<len;i++)
		{
			s[i] = s[i] == '+' ? 1 : 0;
		}
		for(int i=0;i<len;i++)
		{
			if(i+k<=len)
			{
				if(s[i] == 0)
				{
					for(int j=0;j<k;j++)
					{
						s[i+j] = (s[i+j] + 1) % 2;
					}
					res++;
				}
			}
			else if(s[i] == 0)
			{
				fail = 1;
				break;
			}
		}
		if(fail==1)
			cout<<"Case #"<<cs<<": IMPOSSIBLE\n";
		else
			cout<<"Case #"<<cs<<": "<<res<<'\n';
	}
	return 0;
}
