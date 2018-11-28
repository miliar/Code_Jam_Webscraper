//============================================================================
// Name        : A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <set>
#include <iostream>
#define max(x,y) ((x)>(y)?(x):(y))
#define min(x,y) ((x)<(y)?(x):(y))
#define MAXN 100050
#define LL long long
using namespace std;
char a[55][55];
char s[55][55];
//bool bo[55][1 << 6];
bool h[55][55], v[55][55];
int n, m;
bool ismir(char x) {
	return x == '-' || x == '|';
}
void vextend(int i, int j) {
	int x, y;
	x = i, y = j;
	while (x >= 0) {
		if (ismir(s[x][y])) {
			v[x][y] = true;
			break;
		}
		if (s[x][y] == '#')
			break;
		x--;
	}
	x = i, y = j;
	while (x < n) {
		if (ismir(s[x][y])) {
			v[x][y] = true;
			break;
		}
		if (s[x][y] == '#')
			break;
		x++;
	}
}
void hextend(int i, int j) {
	int x, y;
	x = i, y = j;
	while (y >= 0) {
		if (ismir(s[x][y])) {
			h[x][y] = true;
			break;
		}
		if (s[x][y] == '#')
			break;
		y--;
	}
	x = i, y = j;
	while (y < m) {
		if (ismir(s[x][y])) {
			h[x][y] = true;
			break;
		}
		if (s[x][y] == '#')
			break;
		y++;
	}
}
bool ok[55][55];
int main() {
	int tt, ri = 0;
	scanf("%d", &tt);
	while (tt--) {
		scanf("%d%d", &n, &m);
		memset(s, 0, sizeof(s));
		memset(h, 0, sizeof(h));
		memset(v, 0, sizeof(v));
		memset(ok, 0, sizeof(ok));
		for (int i = 0; i < n; ++i) {
			scanf(" %s", a[i]);
			for (int j = 0; j < m; ++j)
				if (a[i][j] != '.')
					ok[i][j] = true;
		}
//		for(int i=0;i<n;++i){
//			for(int j=0;j<m;++j)
//				s[j][i]=a[i][j];
//		}
//		swap(n,m);

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (ismir(s[i][j])) {
					for (int k = j + 1; k < m; ++k) {
						if (ismir(s[i][k])) {
							v[i][j] = true;
							v[i][k] = true;
							for (int x = j + 1; x < k; ++x) {
								vextend(i, x);
							}
							continue;
						}
					}
					for (int k = i + 1; k < n; ++k) {
						if (ismir(s[i][k])) {
							h[i][j] = true;
							h[k][j] = true;
							for (int x = i + 1; x < k; ++x) {
								hextend(x, j);
							}
							continue;
						}
					}
				}
			}
		}
		int flag = 1;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (h[i][j] && v[i][j])
					flag = 0;
				if (h[i][j]) {
					s[i][j] = '-';
					int x = i, y = j + 1;
					while (y < m && s[x][y] == '.') {
						ok[x][y] = true;
						y++;
					}
					x = i, y = j - 1;
					while (y >= 0 && s[x][y] == '.') {
						ok[x][y] = true;
						y--;
					}
				}
				if (v[i][j]) {
					s[i][j] = '|';
					int x = i + 1, y = j;
					while (x < n && s[x][y] == '.') {
						ok[x][y] = true;
						x++;
					}
					x = i - 1, y = j;
					while (x >= 0 && s[x][y] == '.') {
						ok[x][y] = true;
						x--;
					}
				}
			}
		}
		if (flag == 0) {
			printf("Case #%d: IMPOSSIBLE\n", ++ri);
			continue;
		}
		puts("--");
		flag=1;
		while (flag) {
			flag = 0;
			for (int i = 0; i < n; ++i) {
				if (flag)
					break;
				for (int j = 0; j < m; ++j) {
					if (ok[i][j])
						continue;
					int cnt = 0;
					int posx, posy, ty = -1;
					int x = i, y = j + 1;
					while (y < m && s[x][y] == '.') {
						y++;
					}
					if (y < m && !h[x][y] && !v[x][y]) {
						ty = 0;
						posx = x;
						posy = y;
						cnt++;
					}
					x = i, y = j - 1;
					while (y >= 0 && s[x][y] == '.') {
						y--;
					}
					if (y >= 0 && !h[x][y] && !v[x][y]) {
						cnt++;
						ty = 0;
						posx = x;
						posy = y;
					}

					x = i + 1, y = j;
					while (x < n && s[x][y] == '.') {
						x++;
					}
					if (x < n && !h[x][y] && !v[x][y]) {
						cnt++;
						ty = 1;
						posx = x;
						posy = y;
					}
					x = i - 1, y = j;
					while (x >= 0 && s[x][y] == '.') {
						x--;
					}
					if (x >= 0 && !h[x][y] && !v[x][y]) {
						cnt++;
						ty = 1;
						posx = x;
						posy = y;
					}
					if (cnt == 1) {
						if (ty == 0) {
							h[posx][posy] = true;
							s[posx][posy] = '-';
							int x = posx, y = posy + 1;
							while (y < m && s[x][y] == '.') {
								ok[x][y] = true;
								y++;
							}
							x = posx, y = posy - 1;
							while (y >= 0 && s[x][y] == '.') {
								ok[x][y] = true;
								y--;
							}

						} else {
							v[posx][posy] = true;
							s[posx][posy] = '|';
							int x = posx + 1, posy = j;
							while (x < n && s[x][y] == '.') {
								ok[x][y] = true;
								x++;
							}
							x = posx - 1, posy = j;
							while (x >= 0 && s[x][y] == '.') {
								ok[x][y] = true;
								x--;
							}
						}
						flag = true;
					}
				}
			}
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (!ok[i][j])
					flag = 0;
			}
		}
		if (flag == 0) {
			printf("Case #%d: IMPOSSIBLE\n", ++ri);
			continue;
		} else {
			printf("Case #%d: POSSIBLE\n", ++ri);
			for (int i = 0; i < n; ++i)
				printf("%s\n", s[i]);
		}
		return 0;
	}
}
