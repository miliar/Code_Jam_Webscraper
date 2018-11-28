#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); ++i)

int main()
{
	int t; cin>>t;
	for(int i=1; i<=t; ++i)
	{
		cout<<"Case #"<<i<<": ";
		string s; cin>>s;
		int k; cin>>k;
		int res = 0;
		for(int i=0; i+k<=s.size(); ++i)
		{
			if(s[i]=='-')
			{
				++res;
				for(int j=0; j<k; ++j)
				{
					if(s[i+j]=='-') s[i+j]='+';
					else s[i+j]='-';
				}
			}
		}
		bool poss = true;
		for(int i=0; i<s.size(); ++i) if(s[i]=='-') poss = false;
		if(poss) cout<<res<<"\n";
		else cout<<"IMPOSSIBLE\n";
	}
	return 0;
}
