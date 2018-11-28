#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define fst first
#define snd second
#define sz(a) int((a).size())
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef long double ld;
const int INF = 1000 * 1000 * 1000;
const ll LLINF = 1ll << 53;
const double PI = acos(-1);
template<class T> void relaxmax(T& r, T v) { r = max(r, v); }
template<class T> void relaxmin(T& r, T v) { r = min(r, v); }

const int MAXN = 1000;
char s[MAXN + 1];

void flip(char& c) {
	c = c == '-' ? '+' : '-';
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int K;
		scanf(" %s%d", s, &K); 
		int n = (int)strlen(s);
		printf("Case #%d: ", t);
		int ans = 0;
		for (int i = 0; i <= n - K; ++i)
			if (s[i] == '-') {
				++ans;
				for (int d = 0; d < K; ++d)
					flip(s[i + d]);	
			}
		bool ok = true;
		for (int i = 0; i < n; ++i)
			if (s[i] == '-')
				ok = false;
		if (ok)
			printf("%d\n", ans);
		else
			puts("IMPOSSIBLE");
	}
	return 0;
}
