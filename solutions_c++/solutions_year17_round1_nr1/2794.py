#include <bits/stdc++.h>
using namespace std;
#define SQUARE(x)   ((x)*(x))
#define X           first
#define Y           second
#define EPS         (1e-8)
#define INF         (int)INFINITY
#define MOD         (1000000007)
#define PI          (acos(-1.0))
#ifdef DEBUGs
#include "debug.cpp"
// #include "testlib.h"
#else
#define deb(...)
#endif
// ----------

#define MAXR 25 + 10
#define MAXC 25 + 10

int R, C;
char gnd[MAXR][MAXC], ans[MAXR][MAXC];
vector<pair<int, int>> initials;

bool fill(int index) {
	deb(index)
	if(index == initials.size()) {
		for(int i = 0; i < R; ++i) for(int j = 0; j < C; ++j) if(gnd[i][j] == '?') return false;
		for(int i = 0; i < R; ++i) for(int j = 0; j < C; ++j) ans[i][j] = gnd[i][j];
		return true;
	}

	int x = initials[index].X;
	int y = initials[index].Y;
	char c = gnd[x][y];
	bool found = false;
	for(int i = 0; i <= x && !found; ++i) {
		for(int j = 0; j <= y && !found; ++j) {
			for(int p = x; p < R && !found; ++p) {
				for(int q = y; q < C && !found; ++q) { 
					deb(i)
					deb(j)
					deb(p)
					deb(q)
					// fill initial
					bool ok = true;
					for(int k = i; k <= p && ok; ++k) {
						for(int l = j; l <= q && ok; ++l) {
							if(gnd[k][l] == '?' || gnd[k][l] == c) gnd[k][l] = c;
							else ok = false;
						}
					}

					/*for(int i = 0; i < R; ++i) {
						for(int j = 0; j < C; ++j) {
							cout << (char)gnd[i][j];
						} cout << endl;
					}*/
			
					if(ok) found = fill(index+1);

					for(int k = i; k <= p; ++k) {
						for(int l = j; l <= q; ++l) {
							if(gnd[k][l] == c) gnd[k][l] = '?';
						}
					}
					gnd[x][y] = c;
				}
			}
		}
	}

	return found;
}

int main(int argc, char* argv[]) {
	// initialization
 	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;

	for(int tc = 1; tc <= T; ++tc) {
		//initialization
		memset(gnd, '?', sizeof gnd);
		memset(ans, '?', sizeof ans);
		initials.clear();

		// input
		cin >> R >> C;
		{
			string s;
			for(int i = 0; i < R; ++i) {
				cin >> s;
				for(int j = 0; j < C; ++j) {
					if(s[j] != '?') {
						gnd[i][j] = s[j];
						initials.push_back({i, j});
					}
				}
			}
		}

		// main program
		deb(initials)
		fill(0);

		// output
		cout << "Case #" << tc << ":" << endl;
		for(int i = 0; i < R; ++i) {
			for(int j = 0; j < C; ++j) {
				cout << (char)ans[i][j];
			} cout << endl;
		}
	}

	return 0;
}
