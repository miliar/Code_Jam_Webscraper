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

int n, m;
char G[100][100];

void solve() {
	scanf("%d%d", &n, &m);
	rep(i, 1, n) 
		scanf("%s", G[i] + 1);
	rep(j, 1, m) {
		int last = 0;
		char cur = '?';
		rep(i, 1, n)
			if (G[i][j] != '?') {
				cur = G[i][j];
				rep(k, last + 1, i) 
					G[k][j] = cur;
				last = i;
			}
		if (last < n){
			rep(k, last + 1, n)
				G[k][j] = cur;
		}
	}
	rep(j, 2, m) {
		if (G[1][j] == '?')
			rep(i, 1, n) 
				G[i][j] = G[i][j - 1];
	}
	drep(j, m, 1) {
		if (G[1][j] == '?')
			rep(i, 1, n) 
				G[i][j] = G[i][j + 1];
	}	
	rep(i, 1, n) {
		rep(j, 1, m) putchar(G[i][j]);
		puts("");
	}
}

int main(int argc, char *argv[]) {
	int cases;
	scanf("%d", &cases);
	rep(_, 1, cases) {
		printf("Case #%d:\n", _);
		solve();
	}
	return 0;
}
