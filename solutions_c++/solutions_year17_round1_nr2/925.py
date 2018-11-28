#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define drep(i, a, b) for (int i = (a); i >= (b); --i)
#define REP(i, a, b) for (int i = (a); i < (b); ++i)
#define pb(x) push_back(x)
#define mp(x, y) (make_pair(x, y))
#define clr(x) memset(x, 0, sizeof(x))
#define xx first
#define yy second

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
const int inf = ~0U >> 1;
const ll INF = ~0ULL >> 1;
template <class T> inline void read(T &n) {
    char c; int flag = 1;
    for (c = getchar(); !(c >= '0' && c <= '9' || c == '-'); c = getchar()); if (c == '-') flag = -1, n = 0; else n = c - '0';
    for (c = getchar(); c >= '0' && c <= '9'; c = getchar()) n = n * 10 + c - '0'; n *= flag;
}
//***************************

int N, M, cnt, ans;
int R[100], chosen[100], Q[100][100], l[100][100], r[100][100];
int vis[100][100], opt[100], h[3000];

void dfs(int t, int cur) {
	if (t == M + 1) {
		ans = max(ans, cur);
		return;
	}
	rep(i, 1, M)
		if (!chosen[i] && max(l[1][t], l[2][i]) <= min(r[1][t], r[2][i])) {
			chosen[i] = true;
			dfs(t + 1, cur + 1);
			chosen[i] = false;
		}
	dfs(t + 1, cur);
}

void solve() {
	scanf("%d%d", &N, &M);
	rep(i, 1, N) scanf("%d", &R[i]);
	rep(i, 1, N) {
		rep(j, 1, M){
			scanf("%d", &Q[i][j]);
			l[i][j] = max(1, int(Q[i][j] / (1.1 * R[i]) - 2));
			r[i][j] = Q[i][j] / (0.9 * R[i]) + 2;
			while (0.9 * R[i] * r[i][j] > Q[i][j]) --r[i][j];
			while (1.1 * R[i] * l[i][j] < Q[i][j]) ++l[i][j];
			h[++cnt] = l[i][j];
			h[++cnt] = r[i][j];
			vis[i][j] = false;
		}
	}
	sort(h + 1, h + cnt + 1);
	cnt = unique(h + 1, h + cnt + 1) - h - 1;
	ans = 0;
	rep(k, 1, cnt) {
		int flag = true;
		rep(i, 1, N) {
			opt[i] = -1;
			rep(j, 1, M) 
				if (!vis[i][j] && l[i][j] <= h[k] && r[i][j] >= h[k]) {
					if (opt[i] == -1 || r[i][j] < r[i][opt[i]])
						opt[i] = j;
				}
			if (opt[i] == -1) flag = false;
		}
		if (flag) {
			++ans;
			rep(i, 1, N)
				vis[i][opt[i]] = true;
			--k;
		}
	}
	printf("%d\n", ans);
}

int main(int argc, char *argv[]) {
	int cases;
	scanf("%d", &cases);
	rep(_, 1, cases) {
		printf("Case #%d: ", _);
		solve();
	}
	return 0;
}
