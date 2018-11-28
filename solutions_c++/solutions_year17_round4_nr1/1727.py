#include <bits/stdc++.h>
using namespace std;
#define ULL unsigned long long
#define LL long long
#define rep(i,n) for(int i = 0; i < n; ++i)
#define Rep(i,n) for(int i = 1; i <= n; ++i)

const int INF = 0x3f3f3f3f;

int cnt[4];

int main()
{
	int t, cas = 0;
	cin >> t;
	while(cas++ < t) {
		int n, p;
		cin >> n >> p;
		int x;
		memset(cnt, 0, sizeof cnt);
		rep(i, n) cin >> x, ++cnt[x%p];
		int ans = cnt[0];
		if(p == 2) ans += (cnt[1]+1)/2;
		else if(p == 3) {
			int _ = min(cnt[1], cnt[2]);
			ans += _;
			cnt[1] -= _; cnt[2] -= _;
			ans += (cnt[1] + cnt[2] + 2) / 3;
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}

