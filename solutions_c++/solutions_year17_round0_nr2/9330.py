#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{	ll t;
	freopen("in.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	cin>>t;
	
	for(ll k=1;k<=t;k++)
	{
			ll n;
		cin>>n;
		bool f=true;	
		vector<int> v;
		ll tmp=n;
		while(tmp)
		{
		v.push_back(tmp%10);
		tmp/=10;
		}
		reverse(v.begin(),v.end());
		/*for(auto c:v)
		cout<<c;
		cout<<"\n";*/
		for(ll i=v.size()-1;i>0;i--)
		{
			if(v[i]<v[i-1])
			{
				for(ll j=i;j<v.size();j++)
				v[j]=9;
				v[i-1]-=1;
				//cout<<"changed\n";
			}
		}
		if(v[0]==0)
		v[0]=-1;
		cout<<"Case #"<<k<<": ";
		for(auto c:v)
		if(c!=-1)
		cout<<c;
		if(k!=t)
		cout<<"\n";
	}
	
	return 0;
}
