#include"bits/stdc++.h"
using namespace std;
#define ll long long int
#define mod 1000000007
#define pb push_back

int main()
{
	ll tt,w,e,ind,uu=1;
	cin>>tt;
	while(tt--)
	{
		ll n,k,i,j,l,r;
		cin>>n>>k;
		ll a[n][3],b[n][2];
		for(i=0;i<n;i++)
		{
			
			a[i][0]=-1;
			a[i][1]=n;
			a[i][2]=0;
			
		}
		for(j=1;j<=k;j++)
		{
			vector<pair<ll,pair<ll,ll> > > v;
			for(i=0;i<n;i++)
			{
				if(a[i][2]==0)
				{
					if(j!=1 && i>=l && i<=ind)
					{
						a[i][1]=ind;
					}
					if(j!=1 && i>=ind && i<=r)
					{
						a[i][0]=ind;
					}
					
					ll p=(i-a[i][0]-1);
					ll q=(a[i][1]-i-1);
					
					v.pb(make_pair(-min(p,q),make_pair(-max(p,q),i)));
				}
			}
			sort(v.begin(),v.end());
//			for(i=0;i<v.size();i++)
//			{
//				cout<<v[i].first<<" "<<v[i].second.first<<" "<<v[i].second.second<<endl;
//			}
			w=v[0].first,e=v[0].second.first,ind=v[0].second.second;
			a[ind][2]=1;
			l=a[ind][0],r=a[ind][1];
			if(l!=-1) a[l][1]=ind;
			if(r!=n) a[r][0]=ind;
			//cout<<"ok"<<ind<<endl;
			
		}
		cout<<"Case #"<<uu<<": "<<-e<<" "<<-w<<endl;
		uu++;
	}
}
