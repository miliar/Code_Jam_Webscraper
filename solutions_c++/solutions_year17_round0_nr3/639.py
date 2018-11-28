#include <bits/stdc++.h>
#define REP(i, a, b) for (int i = a; i <= b; ++i)
#define PER(i, a, b) for (int i = a; i >= b; --i)
#define RVC(i, S) for (int i = 0; i < S.size(); ++i)
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define debug(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
 
typedef long long LL;
typedef pair<int, int> pii;
typedef vector<int> VI;
typedef unsigned long long ULL;
 
inline int read(){
    int x = 0, ch = getchar(), f = 1;
    while (!isdigit(ch)){if (ch == '-') f = -1; ch = getchar();}
    while (isdigit(ch)) x = x * 10 + ch - '0', ch = getchar();
    return x * f;
}

map<LL, LL> f;

void solve() {
	LL n, k;
	cin >> n >> k;
	f.clear(); f[n] = 1;
	while (k){
		LL len = (--f.end()) -> fi, cnt = (--f.end()) -> se;
		f.erase(--f.end());
		LL p = (len - 1) / 2, q = len - 1 - p;
		if (k <= cnt){
			cout << max(p, q) << ' ' << min(p, q) << endl;
			return;
		}
		f[p] += cnt; f[q] += cnt; k -= cnt;
	}
}

int main(){
	// freopen("d.in", "r", stdin);
	int T = read();
	REP(kas, 1, T){
		printf("Case #%d: ", kas);
		solve();
	}
	return 0;
}