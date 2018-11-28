#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t, it;
	cin>>t;
	for(it=1; it<=t; it++)
	{
		cout<<"Case #"<<it<<": ";
		string s;
		int ans=0, i, j, k, n;
		cin>>s>>k;
		n=s.length();
		for(i=0; i<=(n-k); i++)
		{
			if(s[i]=='-')
			{
				ans++;
				for(j=i; j<(i+k); j++)
				{
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}
			}
		}

		bool f=true;
		for(i=0; i<n; i++)
		{
			if(s[i]=='-')
			{
				f=false;
				break;
			}
		}

		if(f) cout<<ans<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
}