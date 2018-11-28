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

const int MAXN = 103;
const int INF = 1e9;
const int TIME = 60 * 24;

enum {
	F, M
};

int dp[2][TIME + 100][TIME + 100][2];
bool free_now[2][TIME + 100];

void smin(int &a, int b) {
	a = min(a, b);
}

int main() {
  ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; tc++) {
		cout << "Case #" << tc << ": ";
		fill(&dp[0][0][0][0], &dp[0][0][0][0] + (sizeof dp/sizeof (int)), INF);
		for(int i = 0; i < TIME + 100; i++) {
			free_now[0][i] = free_now[1][i] = true;
		}
		int acts[2], a, b;
		cin >> acts[0] >> acts[1];
		for(int j = 0; j < 2; j++) {
			for(int i = 0; i < acts[j]; i++) {
				cin >> a >> b;
				b--;
				for(int x = a; x <= b; x++) {
					assert(free_now[j][x]);
					free_now[j][x] = false;
				}
			}
		}
		for(int st = 0; st < 2; st++) {
			for(int i = 0; i < TIME; i++) {
				int upper = min(i + 1, TIME/2);
				for(int t0 = 0; t0 <= upper; t0++) {
					if(i == 0) {
						if(st == 0 && free_now[0][0]) {
							dp[st][0][1][0] = 0;
						} else if(st == 1 && free_now[1][0]) {
							dp[st][0][0][1] = 0;
						}
					} else {
						if(free_now[0][i] && t0 > 0) {
							int add = 0;
							if(i == TIME - 1 && st != 0) add = 1;
							smin(dp[st][i][t0][0], dp[st][i-1][t0 - 1][0] + add);
							smin(dp[st][i][t0][0], dp[st][i-1][t0 - 1][1] + 1 + add);
						}
						if(free_now[1][i]) {
							int add = 0;
							if(i == TIME - 1 && st != 1) add = 1;
							smin(dp[st][i][t0][1], dp[st][i-1][t0][1] + add);
							smin(dp[st][i][t0][1], dp[st][i-1][t0][0] + 1 + add);
						}
					}
				}
			}
		}
		int ans = INF;
		for(int i = 0; i < 2; i++) {
			for(int j = 0; j < 2; j++) {
				ans = min(ans, dp[i][TIME-1][TIME/2][j]);
			}
		}
		assert(ans < INF);
		cout << ans << '\n';
	}
  return 0;
}
