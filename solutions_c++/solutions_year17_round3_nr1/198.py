#include <bits/stdc++.h>
#define LL long long
#define FOR(i,c) for(__typeof(c.begin()) i = c.begin(); i != c.end(); i++)
#define F first
#define S second
using namespace std;

const LL mod = 1e9 + 7;

template<typename T> T gcd(T a, T b) { return b == 0?a: gcd(b, a % b); }
template<typename T> T LCM(T a, T b) { return a*(b/gcd(a, b)); }
template<typename T> T expo(T base, T e, T mod) { T res = 1;
  while(e > 0) { if(e&1) res = res * base % mod; base = base * base % mod; e >>= 1; }
  return res;
}
template<typename T, typename S> T expo(T b, S e){if(e <= 1)return e == 0?1: b;\
	return (e&1) == 0?expo((b*b), e>>1): (b*expo((b*b), e>>1));}
template<typename T, typename S> T modinv(T a, S mod) { return expo(a, mod-2, mod); }
template<class T, class S> std::ostream& operator<<(std::ostream &os, const std::pair<T, S> &t) {
	os<<"("<<t.first<<", "<<t.second<<")";
	return os;
}
template<class T> std::ostream& operator<<(std::ostream &os, const std::vector<T> &t) {
	os<<"["; FOR(it,t) { if(it != t.begin()) os<<", "; os<<*it; } os<<"]";
	return os;
}
#define gc getchar_unlocked
template <typename T> void in(T &x) {
	T c = gc(); while(((c < 48) || (c > 57)) && (c!='-')) c = gc();
	bool neg = false; if(c == '-') neg = true; x = 0; for(;c < 48 || c > 57;c=gc());
	for(;c > 47 && c < 58;c=gc())	x = (x*10) + (c - 48); if(neg)	x = -x;
}

const int MAXN = 1e3 + 10;
const double PI = acos(-1.0);
const double INF = 1e18;
double dp[MAXN][MAXN];
int n, k;

struct pan {
	double r, h;
	bool operator<(const pan &other) const {
		return r > other.r;
	}
} arr[MAXN];

int main() {
	int t;
	in(t);
	for(int tc = 1; tc <= t; tc++) {
		for(int i = 0; i < MAXN; i++) {
			for(int j = 0; j < MAXN; j++) dp[i][j] = -INF;
		}
		in(n), in(k);
		int a, b;
		for(int i = 1; i <= n; i++) {
			in(a), in(b);
			arr[i].r = a, arr[i].h = b;
		}
		sort(arr + 1, arr + 1 + n);
		for(int i = 1; i <= n; i++) {
			int upper = min(k, i);
			dp[i][1] = max(dp[i-1][1], PI * arr[i].r * arr[i].r + 2 * PI * arr[i].r * arr[i].h);
			for(int j = 2; j <= upper; j++) {
				if(dp[i-1][j-1] >= 0.0) {
					dp[i][j] = dp[i-1][j-1] + 2.0l * PI * arr[i].r * arr[i].h;
				}
				if(dp[i-1][j] >= 0.0) {
					dp[i][j] = max(dp[i][j], dp[i-1][j]);
				}
			}
		}
		assert(dp[n][k] >= 0.0);
		printf("Case #%d: %.9lf\n", tc, dp[n][k]);
	}
  return 0;
}
