#include <bits/stdc++.h>
using namespace std;
#define ULL unsigned long long
#define LL long long
#define rep(i,n) for(int i = 0; i < n; ++i)
#define Rep(i,n) for(int i = 1; i <= n; ++i)

const int INF = 0x3f3f3f3f;

int f(const int hd, int ad, int hk, int ak, int b, int d, int n, int m) {
	int cnt = 0, o = hd;
	while(n) {
		if(o <= ak-d) o = hd - ak;
		else {
			ak = max(0, ak-d);
			o -= ak;
			--n;
		}
		++cnt;
		if(o <= 0 || cnt > 233) return INF;
	}
	while(m) {
		if(o <= ak) o = hd - ak;
		else {
			ad += b;
			o -= ak;
			--m;
		}
		++cnt;
		if(o <= 0 || cnt > 466) return INF;
	}
	while(hk > 0) {
		if(ad < hk && o <= ak) o = hd - ak;
		else {
			hk -= ad;
			if(hk > 0) o -= ak;
		}
		++cnt;
		if(o <= 0 || cnt > 666) return INF;
	}
	return cnt;
}

int main()
{
	int t, cas = 0;
	cin >> t;
	while(cas++ < t) {
		int hd, ad, hk, ak, b, d;
		cin >> hd >> ad >> hk >> ak >> b >> d;
		int ans = INF;
		rep(i, 101) rep(j, 101) {
			ans = min(ans, f(hd, ad, hk, ak, b, d, i, j));
		}
		printf("Case #%d: ", cas);
		if(ans == INF) puts("IMPOSSIBLE");
		else cout << ans << '\n';
	}
	return 0;
}

