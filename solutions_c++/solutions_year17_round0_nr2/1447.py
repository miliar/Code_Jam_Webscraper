#include <bits/stdc++.h>
#define ll long long
#define mk make_pair
using namespace std;

const int N = 1e5 + 5;

ll n;
int a[N], b[N], t;

bool dfs(int x, int limit) {
	if (x > t) return 1;
	if (limit) {
		b[x] = a[x];
		if (a[x] >= b[x - 1] && dfs(x + 1, 1)) 
			return 1;
		for (int i = a[x] - 1; i >= b[x - 1]; i--) {
			b[x] = i;	
			if (dfs(x + 1, 0)) return 1;
		}
	} else {
		for (int i = 9; i >= b[x - 1]; i--) {
			b[x] = i;	
			if (dfs(x + 1, 0)) return 1;
		}
	}
	return 0;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		cin >> n;
		t = 0;
		while (n) {
			a[++t] = n % 10;
			n /= 10;
		}
		reverse(a + 1, a + 1 + t);
		printf("Case #%d: ", ++cas);
		dfs(1, 1);
		ll ans = 0;
		for (int i = 1; i <= t; i++) ans *= 10, ans += b[i]; 
		printf("%lld\n", ans);
	}
}


