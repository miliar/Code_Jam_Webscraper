#include<stdio.h>
#include<map>
using namespace std;
map<long long, long long> M;
void solve() {
	long long n, k, x,c;
	scanf("%lld%lld", &n, &k);
	M.clear();
	M[n]++;
	while (k > 0) {
		auto it = M.end(); it--;
		x = it->first-1, c = it->second;
		M.erase(it);
		k -= c;
		M[x / 2]+=c;
		M[(x + 1) / 2]+=c;
	}
	printf("%lld %lld\n", (x+1) / 2, x / 2);
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		solve();
	}
	return 0;
}