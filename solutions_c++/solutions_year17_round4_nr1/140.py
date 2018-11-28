#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int MAX = 1e2 + 5;
int memo[MAX][MAX][MAX][MAX];
int mark[MAX][MAX][MAX][MAX];
int pass = 1;
int n, p;
int app[4];

int roll(int a, int b, int c, int d) {
	if(a == 0 && b == 0 && c == 0 && d == 0) {
		return 0;
	}
	int &ans = memo[a][b][c][d];
	if(mark[a][b][c][d] == pass) {
		return ans;
	}
	mark[a][b][c][d] = pass;
	int r = (app[0] - a) * 0 + (app[1] - b) * 1 + (app[2] - c) * 2 + (p == 4 ? (app[3] - d) * 3 : 0);
	ans = 0;
	if(a > 0) {
		ans = max(ans, roll(a - 1, b, c, d));
	}
	if(b > 0) {
		ans = max(ans, roll(a, b - 1, c, d));
	}
	if(c > 0) {
		ans = max(ans, roll(a, b, c - 1, d));
	}
	if(d > 0) {
		ans = max(ans, roll(a, b, c, d - 1));
	}
	ans += ((r % p) == 0);
	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	int kase = 1;
	while(t--) {
		memset(app, 0, sizeof app);
		scanf("%d %d", &n, &p);
		fori(i, 1, n + 1) {
			int cur;
			scanf("%d", &cur);
			app[cur % p]++;
		}
		int ans = roll(app[0], app[1], app[2], app[3]);
		printf("Case #%d: %d\n", kase++, ans);
		pass++;
	}

	return 0;
}

