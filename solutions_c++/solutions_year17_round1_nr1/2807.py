#include <bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define ll long long int
#define ld long double
#define pb push_back
#define mkp make_pair
#define pii pair<int, int> 
#define pll pair<long long int, long long int>
#define sci(x) scanf("%d", &x)
#define scl(x) scanf("%lld", &x)

char str[100][100];
int n, m;
pii st[26];
pii en[26];

void make(int x, int y)
{
	int i, j, imax, jmax, imin, jmin;
	imax = jmax = -1;
	imin = jmin = MOD;
	for (i = 1; i <= n; ++i) {
		for (j = 1; j <= m; ++j) {
			if (str[i][j] == str[x][y]) {
				if (i > imax) imax = i;
				if (i < imin) imin = i;
				if (j > jmax) jmax = j;
				if (j < jmin) jmin = j;
			}
		}
	}

	for (i = imin; i <= imax; ++i) {
		for (j = jmin; j <= jmax; ++j) {
			str[i][j] = str[x][y];
		}
	}

	st[str[x][y]-'A'] = mkp(imin, jmin);
	en[str[x][y]-'A'] = mkp(imax, jmax);
}

int main()
{
	int t, i, j, k, a, b, c, tc, imin, imax, jmin, jmax;
	tc = 1;
	cin >> t;
	while (t--) {
		cout << "Case #" << tc++ << ":" << endl;
		cin >> n >> m;
		int mark[26] = {0};
		for (i = 1; i <= n; ++i) {
			scanf("%s", &str[i][1]);
		}

		for (i = 1; i <= n; ++i) {
			for (j = 1; j <= m; ++j) {
				if (str[i][j] != '?' && mark[str[i][j]-'A'] == 0) {
					mark[str[i][j]-'A'] = 1;
					make(i, j);
				}
			}
		}
/*
		for (k = 0; k < 26; ++k) {
			if (mark[k] == 0) continue;
			if (st[k].first == en[k].first) {
				while (st[k].second > 1 && str[st[k].first][st[k].second-1] == '?') {
					st[k].second--;
					str[st[k].first][st[k].second] = k + 'A';
				}
				while (en[k].second < m && str[st[k].first][en[k].second+1] == '?') {
					en[k].second++;
					str[st[k].first][en[k].second] = k + 'A';
				}
			}
			if (st[k].second == en[k].second) {
				while (st[k].first > 1 && str[st[k].first-1][st[k].second] == '?') {
					st[k].first--;
					str[st[k].first][st[k].second] = k + 'A';
				}
				while (en[k].first < n && str[en[k].first+1][st[k].second] == '?') {
					en[k].first++;
					str[en[k].first][st[k].second] = k + 'A';
				}

			}
		}
*/		
		for (k = 0; k < 26; ++k) {
			if (mark[k] == 0) continue;
			imin = st[k].first;
			jmin = st[k].second;
			imax = en[k].first;
			jmax = en[k].second;
			bool can = true;
			while (can) {
				//cout << imin << " " << jmin << " " << imax << " " << jmax << endl;
				can = false;
				if (jmin > 1) {
					for (i = imin; i <= imax; ++i) {
						if (str[i][jmin-1] != '?') break;
					}
					if (i == imax+1) {
						can = true;
						for (i = imin; i <= imax; ++i) {
							str[i][jmin-1] = k + 'A';
						}
						jmin = jmin-1;
					}
				} 
				if (imin > 1) {
					for (j = jmin; j <= jmax; ++j) {
						if (str[imin-1][j] != '?') break;
					}
					if (j == jmax+1) {
						can = true;
						for (j = jmin; j <= jmax; ++j) {
							str[imin-1][j] = k + 'A';
						}
						imin = imin-1;
					}
				} 
				if (jmax < m) {
					for (i = imin; i <= imax; ++i) {
						if (str[i][jmax+1] != '?') break;
					}
					if (i == imax+1) {
						can = true;
						for (i = imin; i <= imax; ++i) {
							str[i][jmax+1] = k + 'A';
						}
						jmax++;
					}
				} 
				if (imax < n) {
					for (j = jmin; j <= jmax; ++j) {
						if (str[imax+1][j] != '?') break;
					}
					if (j == jmax+1) {
						can = true;
						for (j = jmin; j <= jmax; ++j) {
							str[imax+1][j] = k + 'A';
						}	
						imax++;
					}
				}
			}
		}

		for (i = 1; i <= n; ++i) {
			for (j = 1; j <= m; ++j) {
				putchar(str[i][j]);
			} puts("");
		}	
	}

	return 0;
}
