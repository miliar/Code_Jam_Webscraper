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

int a[100];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		int n, K;
		scanf("%d%d", &n, &K);
		fill_n(a, K, 0);
		for (int x, i = 0; i < n; ++i){
			scanf("%d", &x);
			++a[x % K];
		}

		int ans = 0;
		if (K == 2){
			ans += a[0];
			int t = a[1] / 2;
			ans += t, a[1] -= 2 * t;
			if (a[1])
				++ans;
		}
		else if (K == 3){
			ans += a[0];
			int t = min(a[1], a[2]);
			ans += t, a[1] -= t, a[2] -= t;
			t = a[1] + a[2];
			ans += t / 3, t %= 3;
			if (t % 3)
				++ans;		
		}
		else{
			ans += a[0];
			int t = a[2] / 2;
			ans += t, a[2] -= 2 * t;
			t = min(a[1], a[3]);
			ans += t, a[1] -= t, a[3] -= t;
			t = a[1] + a[3];
			ans += t / 4, t %= 4;
			if (t || a[2])
				++ans;
			if (t == 3 && a[2])
				++ans;
		}

		printf("%d\n", ans);
	}
	return 0;
}
