#include <bits/stdc++.h>

#define debug(x) cout << #x" = " << x;

#define st first
#define nd second

using namespace std;
using namespace placeholders;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;

const int MAXN = 1E3 + 10, MAXM = 1E3 + 10;

int n, m;
vector<int> a[MAXM];
int b[MAXN];

int main(){
	int cas;
	scanf("%d", &cas);

	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		int tm;
		scanf("%d%d%d", &n, &m, &tm);
		for (int i = 1; i <= m; ++i)
			a[i].clear();
		fill_n(b + 1, n, 0);
		for (int i = 0; i < tm; ++i){
			int p, j;
			scanf("%d%d", &p, &j);
			a[j].push_back(p);
			++b[p];
		}

		int ans = 0;
		for (int i = 1; i <= m; ++i)
			ans = max<int>(ans, a[i].size());
		for (int t = 0, i = 1; i <= n; ++i){
			t += b[i];
			ans = max(ans, (t + i - 1) / i);
		}

		int cost = 0;
		for (int i = 1; i <= n; ++i)
			cost += max(0, b[i] - ans);

		printf("%d %d\n", ans, cost);
	}
	return 0;
}

