#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#define pb push_back
#define pf push_front
#define fi first
#define se second
#define sz size
#define PI acos(-1)
#define eps 1e-7
#define fod find_by_order
#define fastio ios::base_sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
#define ofk order_of_key
#define val(x) cout << "Value dari "<< #x << " adalah " << x  << "\n"
#define tr tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update>
typedef long long ll;
using namespace __gnu_pbds;
using namespace std;

void readf(string x){
	freopen((x+".in").c_str(),"r",stdin);
	freopen((x+".out").c_str(),"w",stdout);
}


int read()
{
	bool min = 0;
	int  result = 0;
	char ch;
	ch = getchar();
	while(1)
	{
		if(ch == '-') break;
		if(ch >='0' && ch <= '9') break;
		ch = getchar();
	}
	if(ch == '-') min = 1;else result = ch-'0';
	while(1)
	{
		ch =getchar();
		if(ch< '0' || ch>'9') break;
		result = result * 10 + (ch-'0');
	}
	if(min) return -result;
	return result;
}

#define n 1005
int main(){
	readf("AWA");
	ll TC,cs=0;
	cin >> TC;
	while(TC--){
		ll N,K;
		cin >> N >> K;
		vector<pair<long long,pair<long long,ll> > > v,h;
		long long R[n+5],H[n+5];
		for(ll i=0;i<N;i++){
			cin >> R[i] >> H[i];
		//	v.pb({R[i],{H[i],i}});
			h.pb({2*H[i]*R[i],{0,i}});
		}
		sort(h.begin(),h.end());
		reverse(h.begin(),h.end());
		long double ans = -1;
		long long sum=0;
		bool vis[n+5];
		//cout << ans << "\n";
		memset(vis,0,sizeof vis);
		for(ll j=0;j<N;j++){
			memset(vis,0,sizeof vis);
			sum = (R[j] * R[j]) + 2  * R[j]  * H[j];
			//cout << sum << "\n";
			vis[j] = 1;
			ll aw = K-1;
		//	cout << v[0].se.se << "\n";	
			for(ll i=0;i<N;i++){
				if(aw == 0) break;
				if(vis[h[i].se.se]) continue;
				sum = sum +  h[i].fi;
				vis[h[i].se.se] = 1;	
				aw--;
			}
			long double gg = sum * PI;
		//	sum = sum * PI;
	//		cout << sum<< " " << ans << "\n";
			if(gg > ans) ans = gg;
		//	ans = max(ans,sum);
		}
		cout << "Case #" << ++cs << ": ";
		cout << fixed << setprecision(9) << ans << "\n";
	}
}

