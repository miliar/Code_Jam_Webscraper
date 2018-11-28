	//g++ -std=c++0x your_file.cpp -o your_program
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
#include <cstring>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#define fname ""
#define mp make_pair
#define F first
#define pb push_back
#define S second
#define ub upper_bound
#define lb lower_bound
#define inf 2000000000
#define INF 2000000000000000000ll
using namespace std;

const int N = 55;

char c[N][N], c2[N][N];

bool Fixed[N][N];

int n, m;

inline bool isShooter(int x, int y) {
	return (c[x][y] == '-' || c[x][y] == '|');
}

inline void proceed(int x, int y, vector <pair <int, int> > &cur, bool flag) {
	if (!isShooter(x, y)) {
		return ;
	}
	if (c[x][y] == '|') {
		for (int i = x - 1; i >= 1; i--) {
			if (c[i][y] != '.') {
				break;
			}
			if (flag) {
				cur.pb(mp(i, y));
			}
			c[i][y] = '#';
		}
		for (int i = x + 1; i <= n; i++) {
			if (c[i][y] != '.') {
				break;
			}
			if (flag) {
				cur.pb(mp(i, y));
			}
			c[i][y] = '#';
		}
	}
	else {
		for (int j = y - 1; j >= 1; j--) {
			if (c[x][j] != '.') {
				break;
			}
			if (flag) {
				cur.pb(mp(x, j));
			}
			c[x][j] = '#';
		}
		for (int j = y + 1; j <= m; j++) {
			if (c[x][j] != '.') {
				break;
			}
			if (flag) {
				cur.pb(mp(x, j));
			}
			c[x][j] = '#';
		}		
	}
}

inline bool checkKillers() {
	int x, y;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (isShooter(i, j)) {
				x = y = 0;
				for (int l = j + 1; l <= m; l++) {
					if (c[i][l] == '#') {
						break;
					}
					if (isShooter(i, l)) {
						x = 1;
					}
				}
				for (int l = j - 1; l >= 1; l--) {
					if (c[i][l] == '#') {
						break;
					}
					if (isShooter(i, l)) {
						x = 1;
					}
				}
				for (int l = i + 1; l <= n; l++) {
					if (c[l][j] == '#') {
						break;
					}
					if (isShooter(l, j)) {
						y = 1;
					}
				}
				for (int l = i - 1; l >= 1; l--) {
					if (c[l][j] == '#') {
						break;
					}
					if (isShooter(l, j)) {
						y = 1;
					}
				}
				if (x == 1 && y == 1) {
					return false;
				}
				if (x == 1) {
					c[i][j] = '|';
					Fixed[i][j] = 1;
				}
				if (y == 1) {
					c[i][j] = '-';
					Fixed[i][j] = 1;
				}
			}
		}
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (isShooter(i, j) && Fixed[i][j]) {
				if (c[i][j] == '-') {
					for (int l = j - 1; l >= 1; l--) {
						if (c[i][l] == '#') {
							break;
						}
						c[i][l] = '#';
					}
					for (int l = j + 1; l <= m; l++) {
						if (c[i][l] == '#') {
							break;
						}
						c[i][l] = '#';
					}
				}
				if (c[i][j] == '|') {
					for (int l = i - 1; l >= 1; l--) {
						if (c[l][j] == '#') {
							break;
						}
						c[l][j] = '#';
					}
					for (int l = i + 1; l <= n; l++) {
						if (c[l][j] == '#') {
							break;
						}
						c[l][j] = '#';
					}
				}
			}
		}
	}
	return true;
}

inline int assignUnambigious(vector <pair <int, int> > &cur, vector <pair <int, int> > &cur2, bool flag = 0) {
	int respond = 0;
	int cnt = 0;
	int x, y, tp;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (c[i][j] == '.') {
				cnt = 0;
				for (int l = i - 1; l >= 1; l--) {
					if (c[l][j] == '#') {
						break;
					}
					if (isShooter(l, j)) {
						if (!Fixed[l][j]) {
							cnt++;
							x = l, y = j, tp = 1;
						}
						break;
					}
				}
				for (int l = i + 1; l <= n; l++) {
					if (c[l][j] == '#') {
						break;
					}
					if (isShooter(l, j)) {
						if (!Fixed[l][j]) {
							x = l, y = j, tp = 1;
							cnt++;
						}
						break;
					}
				}
				for (int l = j - 1; l >= 1; l--) {
					if (c[i][l] == '#') {
						break;
					}
					if (isShooter(i, l)) {
						if (!Fixed[i][l]) {
							x = i, y = l, tp = 2;
							cnt++;
						}
						break;
					}
				}				
				for (int l = j + 1; l <= m; l++) {
					if (c[i][l] == '#') {
						break;
					}
					if (isShooter(i, l)) {
						if (!Fixed[i][l]) {
							x = i, y = l, tp = 2;
							cnt++;
						}
						break;
					}
				}
				if (!cnt) {
//					cout << i << " " << j << endl;
					return -1;
				}	
				if (cnt == 1) {
					respond = 1;
					if (flag) {
						cur2.pb(mp(x, y));
					}
					if (tp == 1) {
						c[x][y] = '|';
						Fixed[x][y] = 1;
					}
					else {
						c[x][y] = '-';
						Fixed[x][y] = 1;
					}
					proceed(x, y, cur, flag);
				}			
			}
		}
	}
	return respond;
}

inline bool check() {
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (c[i][j] == '.') {
				return false;
			}
		}
	}
	return true;
}

inline bool run() {
	if (check()) {
		return true;
	}
	int x = -1, y;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (isShooter(i, j) && !Fixed[i][j]) {
				x = i;
				y = j;
				break;
			}
		}
		if (x != -1) {
			break;
		}
	}
	if (x == -1) {
		return 0;
	}
	Fixed[x][y] = 1;
	c[x][y] = '-';
	vector <pair <int, int> > cur, cur2;
	cur.clear();
	cur2.clear();
	proceed(x, y, cur, 1);
	int respond;
	while (1) {
		respond = assignUnambigious(cur, cur2, 1);
		if (respond <= 0) {
			break;
		}
	}
	if (respond != -1) {
		if (run()) {
			return 1;
		}
	}
	for (int i = 0; i < (int)cur.size(); i++) {
		c[cur[i].F][cur[i].S] = '.';
	}
	for (int i = 0; i < (int)cur2.size(); i++) {
		Fixed[cur2[i].F][cur2[i].S] = 0;
	}
	cur.clear();
	cur2.clear();
	c[x][y] = '|';
	proceed(x, y, cur, 1);
	while (1) {
		respond = assignUnambigious(cur, cur2, 1);
		if (respond <= 0) {
			break;
		}
	}
	if (respond != -1) {
		if (run()) {
			return 1;
		}
	}
	for (int i = 0; i < (int)cur.size(); i++) {
		c[cur[i].F][cur[i].S] = '.';
	}
	for (int i = 0; i < (int)cur2.size(); i++) {
		Fixed[cur2[i].F][cur2[i].S] = 0;
	}
	cur.clear();
	cur2.clear();
	Fixed[x][y] = 0;
	return 0;
}

inline void solve(int Case) {
	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			cin >> c[i][j];
			c2[i][j] = c[i][j];
			Fixed[i][j] = 0;
		}
	}
/*	if (Case == 52) {
		cout << n << " " << m << endl;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				cout << c[i][j];
			}
			cout << endl;
		}
		exit(0);
	}*/
	if (!checkKillers()) {
		cout << "IMPOSSIBLE\n";
		return ;
	}
/*	cout << endl;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			cout << c[i][j];
		}
		cout << endl;
	} */
	vector <pair <int, int> > tmp, tmp2;
	tmp.clear();
	tmp2.clear();
	while (1) {
		int respond = assignUnambigious(tmp, tmp2, 0);
		if (respond == -1) {
			cout << "IMPOSSIBLE\n";
			return ;
		}
		if (!respond) {
			break;
		}
	}
/*	cout << endl;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			cout << c[i][j];
		}
		cout << endl;
	}
	return ; */
	if (run()) {
		cout << "POSSIBLE\n";
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (c[i][j] == '#' && c2[i][j] == '.') {
					c[i][j] = '.';
				}
				cout << c[i][j];
			}
			cout << endl;
		}
	}
	else {
		cout << "IMPOSSIBLE\n";
	}
}

int main() {
	freopen (fname"C-small-attempt3.in.txt", "r", stdin);
	freopen (fname"out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int Case = 1; Case <= T; Case++) {
		cout << "Case #" << Case << ": ";
		solve(Case);
	}
	return 0;
}
