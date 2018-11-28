#include<bits/stdc++.h>
#define mod 1000000007
#define pp pair<ll,ll>
#define mp make_pair
#define ll long long
#define pb push_back
#define ff first
#define ss second
using namespace std;

ll tc,n,k;
double ans,u,p[1000];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios::sync_with_stdio(0);
	
	cin>>tc;
	for(ll t=1;t<=tc;t++){
		cin>>n>>k;
		cin>>u;
		for(ll i=0;i<n;i++)	
			cin>>p[i];
		sort(p,p+n);
		ll i=0;
		while(i < n){
			while(i < n-1 && p[i] == p[i+1])
				i++;
			i++;
			if(i == n){
				double temp = (u*1.0)/n;
				u = 0;
				for(ll j=0;j<n;j++)
					p[j] += temp;
			}
			else{
				double temp = (p[i]-p[i-1]*1.0)*i;
				if(temp <= u){
					u-=temp;
					for(ll j=0;j<i;j++)
						p[j] = p[i];
				}
				else{
					temp = (u*1.0)/i;
					for(ll j=0;j<i;j++)
						p[j] += temp;
					u = 0;
				}
			}
		}
		double add = u/n;
		double ans = 1.0;
		for(ll i=0;i<n;i++){
			p[i] += add;
			ans = 1.0*ans*p[i];
		}
		ans = min(1.0,ans);
		cout<<"Case #"<<t<<": "<<fixed<<ans<<"\n";
	}
	return 0;
}

