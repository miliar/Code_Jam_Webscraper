#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <string>
using namespace std;

int n, m;
char mp[30][30];

bool doit(int x, int y, char c) {
	if (mp[x][y] != '?') {
		return false;
	}
	bool found = false;
	for (int i = 0; i < n; i ++) {
		for (int j = 0; j < m; j ++)
			if (mp[i][j] == c) {
				found = true;
			}
	}
	if (!found) {
		return false;
	}
	int minx = x;
	int miny = y;
	int maxx = x;
	int maxy = y;
	for (int i = 0; i < n; i ++)
		for (int j = 0; j < m; j ++) {
			if (mp[i][j] == c) {
				minx = min(minx, i);
				maxx = max(maxx, i);
				miny = min(miny, j);
				maxy = max(maxy, j);
			}
		}	
	for (int i = minx; i <= maxx; i ++) 
		for (int j = miny; j <= maxy; j ++) 
			if (mp[i][j] != c && mp[i][j] != '?') {
				return false;
			}
	for (int i = minx; i <= maxx; i ++) 
		for (int j = miny; j <= maxy; j ++) 
			mp[i][j] = c;
	return true;
}

void solve(int testcase) {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i ++) {
		scanf("%s", mp[i]);
	}
	for (int i = 0; i < n; i ++)
		for (int j = 0; j < m; j ++) {
			if (mp[i][j] != '?') doit(i, j, mp[i][j]);
			else {
				for (char c = 'A'; c <= 'Z'; c ++) {
					doit(i, j, c);
				}
			}
		}
	printf("Case #%d:\n", testcase);
	for (int i = 0; i < n; i ++) {
		for (int j = 0; j < m;j ++) printf("%c", mp[i][j]);
		printf("\n");
	}
}

int main() {
	int tst;
	scanf("%d", &tst);
	for (int t = 1; t <= tst; t ++) {
		solve(t);
	}
	return 0;
}
