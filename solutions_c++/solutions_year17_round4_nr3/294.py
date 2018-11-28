#include <cstdio>
#include <algorithm>

using namespace std;

#define pii pair<int, int>
#define piii pair<int, pii>
#define piiii pair<int, piii>

const int N = 60;

int n,m;
char s[N][N];
int d[N][N];

inline void cvt (int i, int j, int t) {
	if (t == 1) {
		for (int k = j + 1;k < m and s[i][k] != '#';k ++) {
			if (s[i][k] == '.') {
				s[i][k] = 'x';
			}
		}
		for (int k = j - 1;k >= 0 and s[i][k] != '#';k --) {
			if (s[i][k] == '.') {
				s[i][k] = 'x';
			}
		}
	} else {
		for (int k = i + 1;k < n and s[k][j] != '#';k ++) {
			if (s[k][j] == '.') {
				s[k][j] = 'x';
			}
		}
		for (int k = i - 1;k >= 0 and s[k][j] != '#';k --) {
			if (s[k][j] == '.') {
				s[k][j] = 'x';
			}
		}
	}
}

inline piiii findOne (int i, int j) {
	int sum = 0;
	pii p;
	int t;
	for (int k = i + 1;k < n and s[k][j] != '#';k ++) {
		if (s[k][j] == '-' or s[k][j] == '|') {
			if (d[k][j] == 0) {
				sum ++;
				p = pii (k, j);
				t = 2;
			}
		}
	}
	for (int k = i - 1;k >= 0 and s[k][j] != '#';k --) {
		if (s[k][j] == '-' or s[k][j] == '|') {
			if (d[k][j] == 0) {
				sum ++;
				p = pii (k, j);
				t = 2;
			}
		}
	}
	for (int k = j + 1;k < m and s[i][k] != '#';k ++) {
		if (s[i][k] == '-' or s[i][k] == '|') {
			if (d[i][k] == 0) {
				sum ++;
				p = pii (i, k);
				t = 1;
			}
		}
	}
	for (int k = j - 1;k >= 0 and s[i][k] != '#';k --) {
		if (s[i][k] == '-' or s[i][k] == '|') {
			if (d[i][k] == 0) {
				sum ++;
				p = pii (i, k);
				t = 1;
			}
		}
	}
	return piiii (sum, piii (t, p));
}

inline bool go () {
	for (int i = 0;i < n;i ++) {
		for (int j = 0;j < m;j ++) {
			if (s[i][j] == '-' or s[i][j] == '|') {
				for (int k = i + 1;k < n and s[k][j] != '#';k ++) {
					if (s[k][j] == '-' or s[k][j] == '|') {
						if (d[i][j] == 2 or d[k][j] == 2) {
							return false;
						}
						s[i][j] = s[k][j] = '-';
						d[i][j] = d[k][j] = 1;
						cvt (i, j, 1);
						cvt (k, j, 1);
					}
				}
				for (int k = i - 1;k >= 0 and s[k][j] != '#';k --) {
					if (s[k][j] == '-' or s[k][j] == '|') {
						if (d[i][j] == 2 or d[k][j] == 2) {
							return false;
						}
						s[i][j] = s[k][j] = '-';
						d[i][j] = d[k][j] = 1;
						cvt (i, j, 1);
						cvt (k, j, 1);
					}
				}
				for (int k = j + 1;k < m and s[i][k] != '#';k ++) {
					if (s[i][k] == '-' or s[i][k] == '|') {
						if (d[i][j] == 1 or d[i][k] == 1) {
							return false;
						}
						s[i][j] = s[i][k] = '|';
						d[i][j] = d[i][k] = 2;
						cvt (i, j, 2);
						cvt (i, k, 2);
					}
				}
				for (int k = j - 1;k >= 0 and s[i][k] != '#';k --) {
					if (s[i][k] == '-' or s[i][k] == '|') {
						if (d[i][j] == 1 or d[i][k] == 1) {
							return false;
						}
						s[i][j] = s[i][k] = '|';
						d[i][j] = d[i][k] = 2;
						cvt (i, j, 2);
						cvt (i, k, 2);
					}
				}
			}
		}
	}
	bool out = true;
	int noi = 1;
	while (out) {
		out = false;
		int nxt = -1u/2;
		for (int i = 0;i < n;i ++) {
			for (int j = 0;j < m;j ++) {
				if (s[i][j] == '.') {
					out = true;
					piiii p = findOne (i, j);
					if (p.first == 0) {
						return false;
					}
					nxt = min (nxt, p.first);
					if (p.first <= noi) {
						int x = p.second.second.first,y = p.second.second.second;
						int t = p.second.first;
						d[x][y] = t;
						if (t == 1) {
							s[x][y] = '-';
						} else {
							s[x][y] = '|';
						}
						cvt (x, y, t);
					}
				}
			}
		}
		noi = nxt;
	}
	return true;
}

inline void solve () {
	scanf ("%d %d", &n, &m);
	for (int i = 0;i < n;i ++) {
		scanf ("%s", s[i]);
	}

	for (int i = 0;i < n;i ++) {
		for (int j = 0;j < m;j ++) {
			d[i][j] = 0;
		}
	}

	if (go ()) {
		printf ("POSSIBLE\n");
		for (int i = 0;i < n;i ++) {
			for (int j = 0;j < m;j ++) {
				if (s[i][j] == 'x') {
					s[i][j] = '.';
				}
			}
			printf ("%s\n", s[i]);
		}
	} else {
		printf ("IMPOSSIBLE\n");
	}
}

int main () {
	int t;
	scanf ("%d", &t);

	for (int i = 1;i <= t;i ++) {
		printf ("Case #%d: ", i);
		solve ();
	}
}