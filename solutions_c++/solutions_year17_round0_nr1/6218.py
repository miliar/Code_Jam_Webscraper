#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("A.out","w",stdout);
	int t;cin>>t;
	for(int o=1;o<=t;o++)
	{
		string s;int k;
		cin>>s>>k;
		int i,cnt=0;
		for(i=0;i<(int)s.size()-k+1;i++)
		{
			if(s[i]=='+')continue;
			for(int j=0;j<k;j++)
			{
				s[i+j]=s[i+j]=='+'?'-':'+';
			}
			cnt++;
		}
		int ok=1;
		for(;i<s.size();i++)if(s[i]=='-')ok=0;
		if(ok)printf("Case #%d: %d\n",o,cnt);
		else printf("Case #%d: %s\n",o,"IMPOSSIBLE");
	}
	return 0;
}
