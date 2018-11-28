#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define RI(i,n) FOR(i,1,(n))
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (int) w.size()
#define getin(i,n,tab) REP(i,n) { cin >> tab[i]; }
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pii;
typedef pair<string, int> para;
const int inf = 1e9 + 7;
const int MAXN = 26;

char tab[MAXN][MAXN];
bool was[MAXN][MAXN];

int maxr, maxc;
const pair<int, int> term(-1, -1);

pair<int, int> next_f(pair<int, int> p, int level) {
	if (p.st == maxr - 1 && p.nd == maxc - 1) {
		return term;
	}
	
	if (p.st == maxr - 1) {
		return make_pair(level, p.nd + 1);
	}
	
	return make_pair(p.st + 1, p.nd);
}

int main() {
	ios_base::sync_with_stdio(0);
	
	int t;
	cin >> t;
	
	bool assigned;
	pair<int, int> p;
	
	RI(q, t) {
		cin >> maxr >> maxc;
		REP(i, maxr) {
			getin(j, maxc, tab[i]);
		}
		
		REP(i, maxr) {
			REP(j, maxc) {
				was[i][j] = false;
			}
		}
		
		REP(i, maxr) {
			REP(j, maxc) {
				if (tab[i][j] == '?') {
					assigned = false;
					
					p = make_pair(i, j);
					while (p != term && tab[p.st][p.nd] == '?') {
						p = next_f(p, i);
					}
					
					if (p != term && !was[p.st][p.nd]) {
						FOR(x, i, p.st) {
							FOR(y, j, p.nd) {
// 								cout << x << ", " << y << endl;
								tab[x][y] = tab[p.st][p.nd];
								was[x][y] = true;
							}
						}
					}
				}
			}
		}
		
		REP(j, maxc) {
			REP(i, maxr) {
				if (!was[i][j] && tab[i][j] == '?') {
					if (maxc > 1 && tab[0][j] != '?' && tab[0][j] != tab[0][j - 1]) {
						tab[i][j] = tab[i - 1][j];
					} else if (maxc == 1) {
						tab[i][j] = tab[i - 1][j];
					} else {
						tab[i][j] = tab[i][j - 1];
					}
				}
			}
		}
		
		cout << "Case #" << q << ":" << endl;
		REP(i, maxr) {
			REP(j, maxc) {
				cout << tab[i][j];
			}
			cout << endl;
		}
	}
}