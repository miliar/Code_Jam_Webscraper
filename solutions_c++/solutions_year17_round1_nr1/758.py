#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>
#include <cassert>
using namespace std;

#define REP(i, n) for (int i = 0; i < (int)(n); i++)

void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
#endif
}

void solve() {
	int n, m; scanf("%d %d ", &n, &m);
	vector<vector<char> > grid(n, vector<char>(m));
	REP(i, n) REP(j, m) scanf(" %c", &grid[i][j]);

	vector<int> jj;
	REP(j, m) {
		bool found = false;
		REP(i, n) {
			if (grid[i][j] != '?') {
				if (!found) {
					jj.push_back(j);
					found = true;
					for (int ii = 0; ii < i; ii++) {
						grid[ii][j] = grid[i][j];
					}
				}
			} else if (i) {
				grid[i][j] = grid[i - 1][j];
			}			
		}
	}

	REP(i, n) REP(j, m) {
		if (j && grid[i][j] == '?' && grid[i][j - 1] != '?') {
			grid[i][j] = grid[i][j - 1];
		}
	}

	for (int i = n - 1; i >= 0; i--) for (int j = m - 2; j >= 0; j--) {
		if (grid[i][j] == '?' && grid[i][j + 1] != '?') {
			grid[i][j] = grid[i][j + 1];
		}
	}

	printf("\n");
	REP(i, n) {
		REP(j, m) printf("%c", grid[i][j]);
		printf("\n");
	}
}

int main() {
    openFiles();
    int n; scanf("%d ", &n);
    for (int i = 0; i < n; i++) {
            printf("Case #%d: ", i + 1);
            solve();
    }
    return 0;
}
