#include <bits/stdc++.h>
#define SZ(v) ((int)(v).size())
#define PI 3.141592653589793238

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<int, ll> pil;

pii rh[1000003];
ll dp[1003];
ll cpy[1003];

bool cmp(pii &p1, pii &p2){
	return p1.first > p2.first;
}

int main(){
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++){
		int n, k;
		scanf("%d%d", &n, &k);
		double ans = 0;
		for (int i=0; i<n; i++){
			scanf("%d%d", &rh[i].first, &rh[i].second);
		}
		sort(rh, rh+n, cmp);
		for (int i=0; i<=n-k+1; i++){
			for (int j=i; j<n; j++){
				cpy[j-i] = (ll)rh[j].first * rh[j].second;
			}
			sort(cpy, cpy+n-i, greater<ll>());
			dp[i] = 0;
			for (int j=0; j<k-1; j++){
				dp[i] += cpy[j];
			}
		}
		double mx = 0;
		for (int i=0; i<n-k+1; i++){
			ans = (double)rh[i].first*rh[i].first*PI
				  + (double)rh[i].first*rh[i].second*2*PI
				  + (double)dp[i+1] * 2 * PI;
			mx = max(mx, ans);
		}
		printf("Case #%d: %.9lf\n", t, mx);
	}
	return 0;
}