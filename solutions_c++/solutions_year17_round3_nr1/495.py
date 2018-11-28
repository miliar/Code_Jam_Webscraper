#define _USE_MATH_DEFINES
#include<bits/stdc++.h>
#define MOD 1000000007
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3f
#define EPS (1e-10)
#define rep(i,n)for(int i=0;i<(n);i++)
using namespace std;
typedef long long ll;
typedef pair<int, int>P;

ll r[1000], h[1000];
int main() {
	int T; scanf("%d", &T);
	for (int cnt = 1; cnt <= T; cnt++) {
		int n, k; scanf("%d%d", &n, &k);
		rep(i, n)scanf("%lld%lld", &r[i], &h[i]);
		ll Max = 0;
		rep(i, n) {
			vector<ll>v;
			rep(j, n) {
				if (i == j)continue;
				v.push_back(r[j] * 2 * h[j]);
			}
			sort(v.begin(), v.end(), greater<>());
			ll sum = r[i] * r[i] + r[i] * 2 * h[i];
			rep(j, k - 1) {
				sum += v[j];
			}
			Max = max(Max, sum);
		}
		printf("Case #%d: %.12lf\n", cnt, Max*M_PI);
	}
}