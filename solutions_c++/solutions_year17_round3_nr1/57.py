#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mkp make_pair
#define fi first
#define se second
#define ll long long
#define M 1000000007
#define all(a) a.begin(), a.end()

const long double pi = acos(-1.0);
int n, k;
int r[1010], h[1010], w[1010];
ll s[1010];

bool cmp(const int &i, const int &j){
	return s[i] > s[j];
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("x.out", "w", stdout);
	int T, ca = 0;
	scanf("%d", &T);
	while(T--){
		scanf("%d%d", &n, &k);
		for(int i = 1; i <= n; ++i){
			scanf("%d%d", r + i, h + i);
			s[i] = (ll)r[i] * h[i];
			w[i] = i;
		}
		sort(w + 1, w + n + 1, cmp);
		ll sum = 0, maxr = 0;
		for(int i = 1; i <= k - 1; ++i){
			sum += s[w[i]];
			maxr = max(maxr, (ll)r[w[i]]);
		}
		ll ans = 0;
		for(int i = k; i <= n; ++i){
			ll tmp = sum + s[w[i]];
			ans = max(ans, 2 * tmp + max(maxr, (ll)r[w[i]]) * max(maxr, (ll)r[w[i]]));
		}
		printf("Case #%d: %.10f\n", ++ca, double(ans * pi));
	}
	return 0;
}
