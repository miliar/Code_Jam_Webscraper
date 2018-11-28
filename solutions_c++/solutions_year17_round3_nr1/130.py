#include<bits/stdc++.h>

const double PI = acos(-1);
using std::vector;
double dy[1010];
bool chk[1010];
using node = std::pair<long long, long long>;
int main() {
	int tc;
	scanf("%d", &tc);
	int T = 0;
	while (tc--) {
		for (int i = 0; i < 1010; i++) {
			dy[i] = 0;
			chk[i] = false;
		}
		int n, k;
		scanf("%d%d", &n, &k);
		vector<node> fan;
		for (int i = 0; i < n; i++) {
			long long a, b;
			scanf("%lld%lld", &a, &b);
			fan.push_back({ a,b });
		}
		std::sort(fan.begin(), fan.end(), std::greater<node>());
		for (int i = 0; i < n; i++) {
			long long r = fan[i].first;
			long long h = fan[i].second;
			for (int j = k; j >= 2; j--) {
				if (chk[j - 1]) {
					dy[j] = std::max(dy[j], dy[j - 1] + PI*(2 * r*h));
					chk[j] = true;
				}
			}
			dy[1] = std::max(dy[1], PI*(r*r + r*h * 2));
			chk[1] = true;
		}
		T++;
		printf("Case #%d: %.10lf\n",T, dy[k]);
	}



}