#include<bits/stdc++.h>
using namespace std;
#define ll long long
void dis(vector<int> &v,ll t)
{
	ll i;
	cout<<"Case #"<<t<<": ";
	for(i=0;i<v.size();i++)
	{
		if(v[i]!=0)
		cout<<v[i];
	}
	cout<<endl;
}
void check(ll ind,vector<int> &v)
{
	ll n=v.size(),i;
	for(i=ind+1;i<n;i++)
	{
		if(v[i]<v[i-1])
		v[i]=v[i-1];
	}
}
int main()
{
		freopen("cdji2-1.in","r",stdin);
			freopen("cdj-1.out","w",stdout);
	ll t,i,c=1;
	cin>>t;
	while(t--)
	{
		ll n;
		cin>>n;
		vector<int> v;
		while(n>0)
		{
			v.push_back(n%10);
			n=n/10;
		}
		reverse(v.begin(),v.end());
		if(v.size()==1)
		{
			dis(v,c);
		}
		else
		{
			for(i=v.size()-1;i>=1;i--)
			{
				if(v[i]<v[i-1])
				{
					v[i]=9;
					v[i-1]--;
					check(i,v);
				}
			}
			dis(v,c);
		}
		c++;
	}
}
