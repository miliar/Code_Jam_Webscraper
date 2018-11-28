#include<bits/stdc++.h>
using namespace std;

typedef long long lld;

int check(string s)
{
	for(lld i=0;i<s.size();i++)
	{
		if(s[i]=='-')
		return 0;
	}
	return 1;
}
int main()
{
	
   freopen("in.txt", "r", stdin);
   freopen("out.txt", "w", stdout);
	
	lld t;
	cin>>t;
	
	for(lld tc=1;tc<=t;tc++)
	{
		lld K;
		string s;
		cin>>s>>K;
		
		lld l=s.size();
		lld ans=0;
		for(lld i=0;i<l;i++)
		{
			if(s[i]=='-' && i+K<=l)
			{
				for(lld j=i; j<i+K ; j++)
				{
					if(s[j]=='-')
					s[j]='+';
					else
					s[j]='-';
				}
				ans++;
			}
		}
		
		if(check(s)==1)
		{
			cout<<"Case #"<<tc<<": "<<ans<<"\n";
		}
		else
		{
			cout<<"Case #"<<tc<<": IMPOSSIBLE"<<"\n";
		}
	
	}
	
}
