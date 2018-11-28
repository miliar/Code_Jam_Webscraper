#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

pair<ll, ll> P[1005];

pair<ll, ll> S[1005];

multiset<ll> ml;

double solve(){
	ml.clear();
	int n, k;
	scanf("%d%d", &n, &k);
	for(int i=0;i<n;i++){
		scanf("%lld%lld", &P[i].first, &P[i].second);
		P[i].first = -P[i].first;
		S[i] = make_pair(P[i].first, (2*P[i].second*P[i].first));
	}
	// sort(P, P+n);
	sort(S, S+n);
	ll ans = 0;
	for(int i=0;i<=n-k;i++){
		// find best
		ll res = S[i].first*S[i].first + -S[i].second;

		for(int j=i+1;j<i+k;j++){
			ml.insert(-S[j].second);
		}

		for(int j=i+k;j<n;j++){
			if(!ml.empty()){
				auto its = ml.begin();
				if(-S[j].second > *its){
					ml.erase(its);
					ml.insert(-S[j].second);
				}
			}
		}

		for(auto its = ml.begin();its != ml.end();its++) res += *its;

		if(res > ans) ans = res;
		ml.clear();
	}

	return (double)ans*M_PI;
}

int main(){
	int T;
	scanf("%d", &T);
	for(int t=1;t<=T;t++){
		double ans = solve();
		printf("Case #%d: ", t);
		printf("%llf", ans);
		printf("\n");
	}
}