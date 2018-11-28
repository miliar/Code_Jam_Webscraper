/* In The Name Of God */
#include <bits/stdc++.h>

# define xx first
# define yy second
# define pb push_back
# define pp pop_back
# define eps 1e-9

using namespace std;
typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll> vll;
ll n,p,r[60],ans;
long double L[60],R[60];
vll v[60];
int main(){
	ios_base::sync_with_stdio (0);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ll T;cin>>T;
	for(ll Case=1 ; Case<=T; Case++){
		for(int i=0 ; i<60 ; i++)
			v[i].clear();
		ans = 0;
		cout<<"Case #"<<Case<<": ";
		cin>>n>>p;
		for(ll i=1 ; i<=n ; i++)
			cin>>r[i];
		for(ll i=1 ; i<=n ; i++){
			for(ll j=1 ; j<=p ; j++){
				ll x;cin>>x;
				v[i].pb(x);
			}
			sort(v[i].rbegin(),v[i].rend());
		}
		ans = 0;
		for(ll i=1 ; i<=1000000 ; i++){
			for(ll j=1 ; j<=n ; j++){
				L[j] = (r[j]*i*90.0)/100.0;
				R[j] = (r[j]*i*110.0)/100.0;
			}
			while(true){
				bool mark = true;
				for(ll j=1 ; j<=n ; j++){
					while(!v[j].empty() && v[j].back() < L[j])
						v[j].pp();
					if(v[j].empty()){
						goto hell;
					}
					if(v[j].back() > R[j])
						mark = false;
				}
				if(!mark)
					break;
				ans++;
				for(ll j=1 ; j<=n ; j++)
					v[j].pp();
			}
		}
		hell:;
		cout<<ans<<endl;
	}
	return 0;
}

