#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>

using namespace std;

const int MAXN = 30;

char grid[MAXN][MAXN];

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;t++) {
		int R, C;
		cin >> R >> C;
		bool bad = false;
		for (int i=0;i<R;i++) for (int j=0;j<C;j++) cin>>grid[i][j];
		for (int i=0;i<R;i++) {
			int tot = 0;
			for (int j=0;j<C;j++) {
				if (grid[i][j] != '?') tot++;
			}
			if (tot > 0) {
				for (int j=1;j<C;j++) if (grid[i][j] == '?') grid[i][j] = grid[i][j-1];
				for (int j=C-2;j>=0;j--) if(grid[i][j] == '?') grid[i][j] = grid[i][j+1];
			}
			else {
				if (i == 0) bad = true;
				else {
					for (int j=0;j<C;j++) grid[i][j] = grid[i-1][j];
				}
			}
		}
		for (int i=R-2;i>=0;i--) {
			int tot = 0;
			for (int j=0;j<C;j++) {
				if (grid[i][j] == '?') tot++;
			}
			if (tot > 0) {
				for (int j=0;j<C;j++) grid[i][j] = grid[i+1][j];
			}
		}
		printf("Case #%d:\n", t);
		for (int i=0;i<R;i++) {
			for (int j=0;j<C;j++) printf("%c", grid[i][j]);
			printf("\n");
		}
	}
}