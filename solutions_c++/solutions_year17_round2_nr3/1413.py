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
const double INF = 1e18;
int n, q;
double speed[MAXN], dist[MAXN];
double D[MAXN][MAXN];
double dp[MAXN];
double mdp[MAXN];
double floyd[MAXN][MAXN];
double prefix[MAXN];

int main() {
  ios_base::sync_with_stdio(false);
  int t;
  cin >> t;
  for(int tc = 1; tc <= t; tc++) {
    cout << "Case #" << tc << ": ";
    cin >> n >> q;
    for(int i = 1; i <= n; i++) {
      cin >> dist[i] >> speed[i];
    }
    for(int i = 1; i <= n; i++) {
      for(int j = 1; j <= n; j++) {
        cin >> D[i][j];
      }
    }
    for(int i = 2; i <= n; i++) {
      prefix[i] = prefix[i-1] + D[i-1][i];
    }
    for(int i = 1; i <= n; i++) {
      dp[i] = INF;
    }
    dp[1] = 0;
    for(int i = 2; i <= n; i++) {
      for(int h = 1; h < i; h++) {
        if(dist[h] >= prefix[i] - prefix[h]) {
          dp[i] = min(dp[i], dp[h] + (prefix[i] - prefix[h])/speed[h]);
        }
      }
    }
    int u, v;
    while(q--) {
      cin >> u >> v;
      assert(dp[v] < INF - 100);
      cout << fixed << setprecision(6) << dp[v] << ' ';
    }
    cout << endl;
  }
  return 0;
}
