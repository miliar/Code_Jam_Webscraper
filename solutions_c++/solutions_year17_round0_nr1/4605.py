#include<iostream>
using namespace std;
int count(string s,int k)
{
	int n=s.size();
	int ans=0;
	for(int i=0;i<=n-k;i++)
	{
		if(s[i]=='-')
		{
			ans++;
			for(int j=0;j<k;j++)s[i+j]=(s[i+j]=='-'?'+':'-');
		}
	}
	for(int i=n-k+1;i<n;i++)if(s[i]!='+')return -1;
	return ans;
}
main()
{
	string s;int k,t;cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>s>>k;
		int ans=count(s,k);
		cout<<"Case #"<<i<<": ";
		if(ans==-1)cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
}
