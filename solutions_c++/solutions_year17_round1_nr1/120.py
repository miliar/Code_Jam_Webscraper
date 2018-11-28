#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define ALL(c) (c).begin(),(c).end()

int TC;
int R, C;
vi pos[26];
string s[30];
string ans[30];
vi em;

int main() {
	scanf("%d", &TC);
	rep(tc, TC) {
		cin >> R >> C;
		em.clear();

		rep(i, R) {
			cin >> s[i];
			ans[i] = s[i];

			pos[i].clear();
			rep(j, C) {
				if (s[i][j] != '?') {
					pos[i].pb(j);
				}
			}

			if (pos[i].size()) {
				int la = -1;
				for (int x : pos[i]) {
					for (int k = la + 1; k <= x; ++k) {
						ans[i][k] = s[i][x];
					}
					la = x;
				}
				for (int k = la + 1; k < C; ++k) {
					ans[i][k] = s[i][la];
				}
				em.pb(i);
			}
		}

		int la = -1;
		for (int x : em) {
			for (int k = la + 1; k <= x; ++k) {
				ans[k] = ans[x];
			}
			la = x;	
		}

		for (int k = la + 1; k < R; ++k) {
			ans[k] = ans[la];
		}

		printf("Case #%d:\n", tc + 1);
		rep(i, R) {
			cout << ans[i] << endl;
		}
	}
	return 0;
}