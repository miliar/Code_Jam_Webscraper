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
typedef vector<int> vint;
map<pii,ll> mp;
int main(){
	ios_base::sync_with_stdio (0);
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	ll T;cin>>T;
	for(int Case = 1 ; Case <= T ; Case ++){
		priority_queue< pii > q;
		mp.clear();
		cout<<"Case #"<<Case<<": ";
		ll n,k;cin>>n>>k;
		q.push( pii( (n-1)/2 , n/2) ) ;
		mp[pii(  (n-1)/2 , n/2 )] = 1;
		while(k){
			pii tmp = q.top();
			q.pop();
			if(mp[tmp] >= k){
				cout<<tmp.yy<<' '<<tmp.xx<<endl;
				break;
			}
			k-= mp[tmp];
			ll X,Y;
			X = (tmp.xx-1)/2;
			Y = (tmp.xx)/2;
			if(mp.find(pii(X,Y)) == mp.end() )
				q.push(pii(X,Y));
			mp[pii(X,Y)] += mp[tmp];
			X = (tmp.yy-1)/2;
			Y = (tmp.yy)/2;
			if(mp.find(pii(X,Y)) == mp.end() )
				q.push(pii(X,Y));
			mp[pii(X,Y)] += mp[tmp];
			mp[tmp] = 0;
		}
	}
	return 0;
}

