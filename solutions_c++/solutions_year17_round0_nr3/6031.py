#include<bits/stdc++.h>
#define ll long long int
#define pb push_back
//#define mp make_pair
#define f first
#define s second

using namespace std;
vector<ll> v;
map<ll,ll> mp;


int main()
{
	int t,i,n,k;
	cin>>t;
	
	for(i=1;i<=t;i++)
	{
		v.clear();
		mp.clear();
		ll sum=0,a,b,temp;
		cin>>n>>k;
		v.pb(n);
		mp[n]++;
		
		
		while(1)
		{
			temp=v.front();
			
			sum+=mp[temp];
			//cout<<temp<<" "<<sum<<endl;
			if(sum>=k) break;
			temp--;
			if(temp%2==0) a=b=temp/2;
			else
			{
				b=temp/2;
				a=b+1;
			}
			
			if(mp[a]==0) v.pb(a);
			mp[a]+=mp[temp+1];
			if(mp[b]==0) v.pb(b);
			mp[b]+=mp[temp+1];
			
			//cout<<a<<" "<<b<<" "<<mp[a]<<" "<<mp[b]<<endl;
			mp[temp+1]=0;
			v.erase(v.begin());
			//for(int j=0;j<v.size();j++) cout<<v[j]<<endl;
			
			
		}
		
		temp--;
		if(temp%2==0) a=b=temp/2;
		else
		{
			b=temp/2;
			a=b+1;
		}
		
		cout<<"Case #"<<i<<": "<<a<<" "<<b<<endl;
		
	}
	
}

