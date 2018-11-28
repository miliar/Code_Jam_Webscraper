#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
vector<pll> V;
int u, t=1, n, k, i, cnt, j;
ll r, h, area, mx;
int main(){
	for(cin>>u; t<=u; t++){
		V.clear();
		mx=0;
		cin>>n>>k;
		for(i=0; i<n; i++)
			cin>>r>>h, V.push_back({2*r*h, r});
		sort(V.begin(), V.end(), greater<pll>());
		for(i=0; i<n; i++){
			r=V[i].second, area=V[i].first+r*r;
			cnt=1;
			for(j=0; j<n&&cnt<k; j++){
				if(i==j)	continue;
				if(V[j].second<=r)
					cnt++, area+=V[j].first;
			}
			if(cnt==k)
				mx=max(mx, area);
		}
		printf("Case #%d: %.8Lf\n", t, (long double)M_PI*mx);
	}
	return 0;
}
