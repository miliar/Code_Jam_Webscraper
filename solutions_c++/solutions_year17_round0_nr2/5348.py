#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define vll vector<ll>
#define pb push_back
ll t,n;
int main()
{	
	freopen("B-large.in","r",stdin);
	freopen("outputf.in","w",stdout);
	cin>>t;
	for(ll tt=1;tt<=t;tt++) 
	{
		cout<<"Case #"<<tt<<": ";
		cin>>n;
		vll d;
		ll i,j;
		while(n)
		{
			d.pb(n%10);
			n/=10;
		}
		for(i=d.size()-1;i>0;i--)
		{
			if(d[i]>d[i-1]) break;
		}	
		if(i==0) 
		{
			i=-1;
		}
		else
		{
			ll k=i;
			while(k<d.size()&&d[i]==d[k]) k++;
			i=k-1;
		}
		for(j=d.size()-1;j>i;j--)
		{
			cout<<d[j];
		}
		if(i==-1) {cout<<"\n";continue;}
		//cout<<"j"<<j<<endl;
		if(j==d.size()-1&&d[j]==1) j--;
		else cout<<d[j--]-1;
		for(;j>=0;j--) cout<<"9";
		cout<<"\n";
	}
}