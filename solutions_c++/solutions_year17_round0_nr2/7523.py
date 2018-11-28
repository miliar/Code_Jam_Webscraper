#include<bits/stdc++.h>
#define ll long long int
using namespace std;
FILE *in=freopen("in.txt","r",stdin);
FILE *out=freopen("out.txt","w",stdout);
int main()
{
	int t;
	cin>>t;
	for(int m=1;m<=t;m++)
	{
		ll n;
		cin>>n;
		ll g=n;
		ll ans=0;
		vector<int> v;
		while(n)
		{
			v.push_back(n%10);
			n/=10;
		}
		int sz=v.size();
		for(int i=0;i<sz;i++)
		{
			if(v[i]<v[i+1])
			{
			v[i+1]--;
		    for(int j=i;j>=0;j--)
		    v[j]=9;
			}
		}
		for(int i=sz-1;i>=0;i--)
		    ans=ans*10+v[i];
		    
		if(sz==1)
		cout<<"Case #"<<m<<": "<<g<<endl;
		    
		else
		cout<<"Case #"<<m<<": "<<ans<<endl;
	}
	return 0;
}
