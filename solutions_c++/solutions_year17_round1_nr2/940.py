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


int r[111], L[55][55], R[55][55];

const double eps = 1e-6;
int sgn(double x) {
	return x < -eps ? -1 : eps < x;
}

int n, p;
int work() {
	int ret = 0;
	for (int k = 1000000; 0 < k; --k) {
		bool ok2 = true;
		for (int i = 1; i <= n; ++i) {
			bool ok = false;
			for (int j = 1; j <= p; ++j)
				if (L[i][j] <= k && k <= R[i][j]) {
					ok = true;
					break;
				}
			if (!ok) {
				ok2 = false;
				break;
			}
		}
		if (ok2) {
			++ret;
			for (int i = 1; i <= n; ++i) {
				for (int j = 1; j <= p; ++j)
					if (L[i][j] <= k && k <= R[i][j]) {
						L[i][j] = R[i][j] = -1;
						break;
					}
			}
			++k;
		}
	}
	return ret;
}

int main() {
#ifdef lol
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
#endif

	int T = fr();
	for (int kase = 1; kase <= T; ++kase) {
		fr(n, p);
		for (int i = 1; i <= n; ++i)
			fr(r[i]);
		memset(L, -1, sizeof L);
		memset(R, -1, sizeof R);
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= p; ++j) {
				int v = fr(), k;
				for (k = 1; k <= 1000000; ++k) {
					if (sgn(v - 0.9 * k * r[i]) >= 0 && sgn(v - 1.1 * k * r[i]) <= 0) {
						L[i][j] = k;
						break;
					}
					if (sgn(v - 0.9 * k * r[i]) < 0)
						break;
				}
				while (k <= 1000000 && sgn(0.9 * k * r[i] - v) <= 0 && sgn(1.1 * k * r[i] - v) >= 0) {
					R[i][j] = k;
					++k;
				}
			}
	//	for (int i = 1; i <= n; ++i) {
	//		for (int j = 1; j <= p; ++j)
	//			printf("(%2d %2d) ", L[i][j], R[i][j]);
	//		puts("\n");
	//	}
		int ans = 0;
		ans += work();
		printf("Case #%d: %d\n", kase, ans);
	}

	return 0;
}
