#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for(int i=(a);i<(b);i++)
#define MOD 1000000007
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef long double ld;
#define PI ((ld)acos(-1.))
#define asdf(x...) fprintf(stderr, x)

int T, N;
char s[20];
string ans, cur;
bool seen[20][10][2];

void dfs (int i, int m, bool sm) {
	if (seen[i][m][sm]) return;
	if (i == N) {
		if (!ans.size()) ans = cur;
	} else {
		for (int d = 9; d >= m; d--) {
			if (sm || d <= int(s[i] - '0')) {
				if (d) cur += char(d + '0');
				dfs(i+1, d, sm || (d < int(s[i] - '0')));
				if (d) cur.pop_back();
			}
		}
	}
}

int main () {
	scanf("%d", &T);
	fo(t, 1, T+1) {
		//REMEMBER CLEAR DS
		fo(i, 0, 20) fo(j, 0, 10) fo(k, 0, 2) {
			seen[i][j][k] = false;
		}
		ans.clear();
		cur.clear();
		//REMEMBER CLEAR DS

		asdf("Doing case %d... ", t);
		printf("Case #%d: ", t);

		scanf(" %s", s);
		N = (int) strlen(s);

		dfs(0, 0, 0);

		printf("%s\n", ans.c_str());
		asdf("%s\n", ans.c_str());
	}
	return 0;
}
