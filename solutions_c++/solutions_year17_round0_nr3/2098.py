#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define ii pair<int,int>
#define INF 1000000000
#define INFLL 1000000000000000010ll
#define UQ(x) (x).resize(distance((x).begin(),unique(all((x)))))
#define mid(x,y) (((x)+(y))>>1)
int tc;
ll n,k;
map<ll,ll> m;
int main() {
	scanf("%d",&tc);
	for (int kk=1;kk<=tc;kk++) {
		scanf("%lld%lld",&n,&k);
		m.clear();
		m[n]=1ll;
		ll ans1=-1ll,ans2=-1ll;
		while(k>0ll) {
			auto it=(--m.end());
			ll x=it->first,c=it->second;
			if (x%2ll) {
				if (k<=c) {
					ans1=ans2=x/2ll;
					k=0ll;
				} else m[x/2ll]+=2ll*c;
			} else {
				if (k<=c) {
					ans1=x/2ll;
					ans2=x/2ll-1ll;
					k=0ll;
				} else {
					m[x/2ll]+=c;
					m[x/2ll-1ll]+=c;
				}
			}
			k-=c;
			m.erase(it);
		}
		assert(ans1!=-1ll);
		assert(ans2!=-1ll);
		printf("Case #%d: %lld %lld\n",kk,ans1,ans2);
	}
}