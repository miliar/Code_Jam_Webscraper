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

const int MAXN = 1E4 + 10;

int n, m;
int a[MAXN], b[MAXN];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		scanf("%d%d", &m, &n);
		double t = 0;
		for (int i = 0; i < n; ++i){
			scanf("%d%d", a + i, b + i);
			t = max(t, (m - a[i]) * 1.0 / b[i]);
		}
		printf("%.12f\n", m / t);
	}
	return 0;
}
