#include <bits/stdc++.h>
using namespace std;
namespace my_header {
#define pb push_back
#define mp make_pair
#define pir pair<int, int>
#define vec vector<int>
#define pc putchar
#define clr(t) memset(t, 0, sizeof t)
#define pse(t, v) memset(t, v, sizeof t)
#define bl puts("")
#define wn(x) wr(x), bl
#define ws(x) wr(x), pc(' ')
	const int INF = 0x3f3f3f3f;
	typedef long long LL;
	typedef double DB;
	inline char gchar() {
		char ret = getchar();
		for(; (ret == '\n' || ret == '\r' || ret == ' ') && ret != EOF; ret = getchar());
		return ret; }
	template<class T> inline void fr(T &ret, char c = ' ', int flg = 1) {
		for(c = getchar(); (c < '0' || '9' < c) && c != '-'; c = getchar());
		if (c == '-') { flg = -1; c = getchar(); }
		for(ret = 0; '0' <= c && c <= '9'; c = getchar())
			ret = ret * 10 + c - '0';
		ret = ret * flg; }
	inline int fr() { int t; fr(t); return t; }
	template<class T> inline void fr(T&a, T&b) { fr(a), fr(b); }
	template<class T> inline void fr(T&a, T&b, T&c) { fr(a), fr(b), fr(c); }
	template<class T> inline char wr(T a, int b = 10, bool p = 1) {
		return a < 0 ? pc('-'), wr(-a, b, 0) : (a == 0 ? (p ? pc('0') : p) : 
			(wr(a/b, b, 0), pc('0' + a % b)));
	}
	template<class T> inline void wt(T a) { wn(a); }
	template<class T> inline void wt(T a, T b) { ws(a), wn(b); }
	template<class T> inline void wt(T a, T b, T c) { ws(a), ws(b), wn(c); }
	template<class T> inline void wt(T a, T b, T c, T d) { ws(a), ws(b), ws(c), wn(d); }
	template<class T> inline T gcd(T a, T b) {
		return b == 0 ? a : gcd(b, a % b); }
	template<class T> inline T fpw(T b, T i, T _m, T r = 1) {
		for(; i; i >>= 1, b = b * b % _m)
			if(i & 1) r = r * b % _m;
		return r; }
};
using namespace my_header;

int _hd, _ad, _hk, _ak, b, d;

int calc(int A, int B) {
	int hd = _hd, hk = _hk, ad = _ad, ak = _ak;
	int ans = 0;
	do {
		++ans;
		if (hd <= 0) return INT_MAX;
		if (A > 0) {
			if (hd > ak - d) {
				ak -= d;
				hd -= ak;
				--A;
			} else {
				hd = _hd;
				hd -= ak;
			}
		} else if (B > 0) {
			if (hd > ak) {
				hd -= ak;
				ad += b;
				--B;
			} else {
				hd = _hd;
				hd -= ak;
			}
		} else {
			if (hk <= ad) {
				break;
			} else if (hd > ak) {
				hk -= ad;
				hd -= ak;
			} else {
				hd = _hd;
				hd -= ak;
			}
		}
	} while (ans <= 1000);
	return ans > 1000 ? INT_MAX : ans;
}

int work() {
	int ans = INT_MAX;
	for (int i = 0; i <= 100; ++i)
		for (int j = 0; j <= 100; ++j)
			ans = min(ans, calc(i, j));
	if (ans == INT_MAX)
		return -1;
	return ans;
}

int main() {
#ifdef lol
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
#endif

	int T = fr();
	for (int kase = 1; kase <= T; ++kase) {
		fr(_hd, _ad, _hk);
		fr(_ak, b, d);
		int ans = work();
		printf("Case #%d: ", kase);
		if (ans == -1) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n", ans);
		}
	}

	return 0;
}
