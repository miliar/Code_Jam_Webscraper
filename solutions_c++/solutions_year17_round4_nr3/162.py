#include <iostream>
#include <bits/stdc++.h>


using namespace std;

#define re return
#define mp make_pair
#define forn(i, n) for (int i = 0; i < n; i++)
#define sz(a) int(a.size())
#define fi first
#define se second

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int n, m, dp[100][32][32];
pair<int, int> pr[100][32][32];
int we_know[5][100];
string s[5];
string prr[100][32][32];
char ss[10];


void solve() {
	int n, m;
	cin >> n >> m;
	forn (i, n) {
		cin >> s[i];
		forn (j, m) {
			if (s[i][j] == '|') 
				s[i][j] = '-';
			we_know[i][j] = 0;
		}
	}
	forn (i, n) {
		forn (j, m) {
			if (s[i][j] == '-') {
				bool ok = false, ok1 = false;;
				for (int jj = j - 1; jj >= 0; jj--)
					if (s[i][jj] == '-') {
						ok = true;
						break;
					} else
					if (s[i][jj] == '#')
						break;
				for (int jj = j + 1; jj < m; jj++)
					if (s[i][jj] == '-') {
						ok = true;
						break;
					} else
					if (s[i][jj] == '#')
						break;
				for (int ii = i - 1; ii >= 0; ii--)
					if (s[ii][j] == '-') {
						ok1 = true;
						break;
					} else
					if (s[ii][j] == '#')
						break;
				for (int ii = i + 1; ii < n; ii++)
					if (s[ii][j] == '-') {
						ok1 = true;
						break;
					} else
					if (s[ii][j] == '#')
						break;
				if (ok && ok1) {
					cout << "IMPOSSIBLE\n";
					re;
				}
				if (ok) {
					we_know[i][j] = 1;
				}
				if (ok1) {
					we_know[i][j] = 2;
				}
			}
			//cout << we_know[i][j] << " ";
		}
		//cout << "\n";
	}

	forn (i, m + 1) {
		forn (j, (1 << n))
		forn (k, (1 << n))
			dp[i][j][k] = 0;
	}
	dp[0][0][0] = 1;
	forn (i, m) {
		forn (j, (1 << n))
		forn (pk, (1 << n)) {
			if (dp[i][j][pk] == 0) continue;
			
			forn (jj, (1 << n)) {
			
				bool ok = true;
				forn (ik, n) {
					int kp = 0;
					if (jj & (1 << ik)) kp = 1;
					if (kp && (s[ik][i] == '#' || s[ik][i] == '.')) {
						ok = false;
						break;
					}
					if ((we_know[ik][i] == 1 && kp == 1) || (we_know[ik][i] == 2 && kp == 0)) {
						ok = false;
						break;
					}
					ss[ik] = '|';
					if (kp)
						ss[ik] = '-';
					if (s[ik][i] == '.' || s[ik][i] == '#')
						ss[ik] = s[ik][i];

				}
				if (!ok) continue;

				int nwh = 0, op = pk;
				forn (ik, n) {
					if (ss[ik] == '-') {
						if (op & (1 << ik))
							op -= (1 << ik);
						nwh |= (1 << ik);
					}
					if (ss[ik] == '.' && (j & (1 << ik))) {
						nwh |= (1 << ik);
						continue;
					}
					if ((ss[ik] == '#' || ss[ik] == '|') && (op & (1 << ik))) {
						ok = false;
					}
					if (ss[ik] == '.') {
						bool ok1 = false;
						for (int prk = ik; prk >= 0; prk--)
							if (ss[prk] == '|') {
								ok1 = true;
								 break;
							} else
							if (ss[prk] == '#') break;
						for (int prk = ik; prk < n; prk++)
							if (ss[prk] == '|') {
								ok1 = true;
								 break;
							} else
							if (ss[prk] == '#') break;
						if (!ok1) {
							op |= (1 << ik);
						}
					}
				}
				if (ok) {
					dp[i + 1][nwh][op] = 1;
					pr[i + 1][nwh][op] = mp(j, pk);
					prr[i + 1][nwh][op] = "";
					forn (ik, n) {
						prr[i + 1][nwh][op] += ss[ik];
					}
					//cout << i + 1 << " " << nwh << " " << prr[i + 1][nwh] << "k\n";
				}
			}
		}
	}
	forn (j, (1 << n)) {
		if (dp[m][j][0]) {
			cout << "POSSIBLE\n";
			int q = 0;
			for (int cc = m; cc; cc--) {
				forn (i, n) {
					s[i][cc - 1] = prr[cc][j][q][i];
				}
				pii a = pr[cc][j][q];
				j = a.fi;
				q = a.se;
			}
			forn (i, n) {
				cout << s[i] << "\n";
			}
			re;
		}
	}
	cout << "IMPOSSIBLE\n";
}

int main() {
	iostream::sync_with_stdio(0), cin.tie(0);
	freopen("a.out", "w", stdout);
	int t;
	cin >> t;
	forn (i, t) {
		cout << "Case #" << i + 1 <<": ";
		solve();
	}
	re 0;
}