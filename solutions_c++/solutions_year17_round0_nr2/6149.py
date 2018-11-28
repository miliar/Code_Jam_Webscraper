
#include<bits/stdc++.h>
using namespace std;
#define ll long long
main()
{
	freopen("B-large.in","r",stdin);
	freopen("outlarge.txt","w",stdout);
	int tt;
	cin>>tt;
	for(int p=1;p<=tt;p++)
	{
	ll N;
	cin>>N;
	vector<int>v;
	ll R=N;
	while(R>0)
	{
	int x=R%10;
	R=R/10;
	v.push_back(x);
	}
	reverse(v.begin(),v.end());
	int len=v.size();
	for(int t=0;t<18;t++)
	{
	for(int i=0;i<(len-1);i++)
	{
	if(v[i]<=v[i+1])
	continue;
	else
	{
	if(v[i+1]==0)
	{
	for(int j=i+1;j<=(len-1);j++)
	v[j]=9;
	while(v[i]==0)
	{
	v[i]=9;
	i--;
	}
	v[i]=v[i]-1;
	}
	else
	{
       for(int j=i+1;j<=(len-1);j++)
	v[j]=9;
	v[i]=v[i]-1;
	}

	}
	}
}
	//string s;
	ll ans=0;
	for(int i=0;i<len;i++)
	{
		//int y=v[i];
		ans=ans*10+v[i];
	
	}
	cout<<"Case #"<<p<<": "<<ans<<'\n';
	}
}