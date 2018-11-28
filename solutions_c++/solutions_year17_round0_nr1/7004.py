#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,tc=1;
	cin>>t;
	for(tc=1;tc<=t;tc++)
	{
		string s;
		cin>>s;
		int n=s.size();
		int k,i,j,ans=0;
		cin>>k;
		bool req;
		for(i=0;i<n-k+1;i++)
		{
			if(s[i]=='+')
			 continue;
			req=false;
			for(j=i;j<i+k;j++)
			{
				
				if(s[j]=='-')
				{
					req=true;
					break;
				}
			}
			if(req)
			{
				for(j=i;j<i+k;j++)
				{
					if(s[j]=='-')
					  s[j]='+';
					else
					  s[j]='-';
				}
				ans++;
			}
		//	 cout<<s<<"  "<<ans<<endl;
		}
		req=true;
		for(i=0;i<n;i++)
		{
			if(s[i]=='-')
			{
				req=false;
				break;
			}
		}
		cout<<"Case #"<<tc<<": ";
		if(req)
		 cout<<ans<<"\n";
		else 
		 cout<<"IMPOSSIBLE\n";
	}
}
