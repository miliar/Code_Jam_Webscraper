#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define pb push_back

set <ll> st;
ll n,k=0;
ll MAX = (ll)1e18 + 5;

void bfs(){
	k=0;
	queue <ll> q;
	ll ans = 0;
	for(ll i=1;i<=9;i++){
		st.insert(i);
		q.push(i);
		ans = i;
		k++;
	}
	while(!q.empty()){
		ll top = q.front();
		ans = top;
		if(top >= MAX) break;
	//		cout<<top<<" ";
		ll ld = top%10;
		for(ll i=ld;i<=9;i++){
			ll temp = (top*10) + i;
			if(temp <= MAX){
				q.push(temp);
				st.insert(temp);
				k++;
			}
			else{
				break;
			}
		}
		q.pop();
	}
}

int main()
{
	int t;
	cin>>t;
	bfs();
	int cs = 1;
	while(t--){
		cin>>n;
		ll ans;
		set<ll>::iterator it = st.upper_bound(n);
		if(*it == n) ans=n;
		else{
			if(it!=st.begin())
				it--;
			ans = *it;
		}
		cout<<"Case #"<<cs<<": "<<ans<<"\n";
		cs++;
	}
	return 0;
}