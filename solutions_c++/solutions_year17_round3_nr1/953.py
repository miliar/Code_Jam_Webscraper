#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

const double PI = acos(-1);
pair<long long, long long> pan[1010];
vector<int> v;

int main() {
	int t;
	scanf("%d", &t);
	for (int _ = 1; _ <= t; _++) {
		int n, k;
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i++) {
			scanf("%lld%lld", &pan[i].first, &pan[i].second);
		}
		long long ans = 0;
		for (int i = 0; i < n; i++) {
			v.clear();
			long long now = pan[i].first * pan[i].first + 2 * pan[i].first * pan[i].second;
			for (int j = 0; j < n; j++) {
				if (i != j && pan[j].first <= pan[i].first) {
					v.push_back(j);
				}
			}
			if (v.size() < k - 1) continue;
			sort(v.begin(), v.end(), [](int a, int b) {
					return pan[a].first * pan[a].second > pan[b].first * pan[b].second;});
			for (int j = 0; j < k - 1; j++) {
				now += 2 * pan[v[j]].first * pan[v[j]].second;
			}
			ans = max(ans, now);
		}
		printf("Case #%d: %.10lf\n", _, 1.0 * ans * PI);
	}
}
