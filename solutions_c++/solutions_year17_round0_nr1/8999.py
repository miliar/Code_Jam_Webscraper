/* Sachin Chandani */

#include<bits/stdc++.h>
using namespace std;
#define INF INT_MAX
#define PB push_back
#define SET(a,b) memset(a,b,sizeof(a))
#define rep(i,a,b) for(i=a;i<=b;i++)
#define rev(i,a,b) for(i=b;i>=a;i--)


int main()
{
	ios::sync_with_stdio(false);	
	cin.tie(NULL);
	string s;
	int a[1005];
	int t,k;
	cin>>t;
	for(int one=1;one<=t;one++)
	{
		int ans=0,check=0;
		cin>>s>>k;
		int l=s.length();
		cout<<"Case #"<<one<<": ";
		for(int i=0;i<l;i++)
		{
			if(s[i]=='+') a[i]=1;
			else a[i]=0;	
		}
		for(int i=0;i<l;i++)
		{
			if(a[i]==0 && i<=l-k)
			{
				ans++;
				for(int j=i;j<i+k && j<l;j++)
				{
					if(a[j]==1)
						a[j]=0;
					else a[j]=1;

				}
			}	
		}
		for(int i=0;i<l;i++)
		{
			if(a[i]!=1) check=1;
		}
		if(check==1)  cout<<"IMPOSSIBLE"<<'\n';
		else
			cout<<ans<<'\n';		
	}
	
	return 0;
}

