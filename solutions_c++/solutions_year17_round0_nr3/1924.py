#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000007
#define X first
#define Y second
#define max3(a,b,c) max(a,max(b,c))
#define min3(a,b,c) min(a,min(b,c))
#define forn(n) for(ll i=0;i<n;i++)
#define forin(n1,n2) for(ll i=n1;i<n2;i++)
using namespace std;
typedef pair<int,int>pii;
FILE *ptr=freopen("in.txt","r",stdin);
FILE *ptr1=freopen("outnew.txt","w",stdout);
int main()
{
	ll tc;
	cin>>tc;
	for(int z=1;z<=tc;z++)
	{
		map<ll,ll>m;
		ll n,k;  cin>>n>>k;
		set<ll,greater<ll> > pq;
		pq.insert(n);
		m[n]=1;
		k--;
			set<ll>::iterator it=pq.begin();
		while(k)
		{
			it=pq.begin();
			ll t=*it;
//			cout<<t<<" \n";
			pq.erase(it);
			if(m[t]>k){	  pq.insert(t); k=0; continue;		}
			else {
				k-=m[t];
			if(t==1) 
			{
				m[t]=0;
				continue;
			}
			if(t==2)
			{
				pq.insert(1);
				m[1]+=m[t];
			}
			else{
			if(t%2==1)
			{
				pq.insert((t-1)/2);
				m[(t-1)/2]+=2*m[t];
//				pq.push((t-1)/2);
			}
			else
			{
				m[(t)/2]+=m[t];
				m[(t/2)-1]+=m[t];
				pq.insert((t/2)-1);
				pq.insert(t/2);
			}}
			m[t]=0;
			}
		}
		it=pq.begin();
		ll t=*it;
		if(t==1) cout<<"Case #"<<z<<": "<<0<<" "<<0<<"\n";
		else
		{
			if(t==2) cout<<"Case #"<<z<<": "<<1<<" "<<0<<"\n";
			else
			{
				if(t%2==1) cout<<"Case #"<<z<<": "<<(t-1)/2<<" "<<(t-1)/2<<"\n";
				else cout<<"Case #"<<z<<": "<<(t/2)<<" "<<((t/2)-1)<<"\n";
			}
		}
	}
	return 0;
}

