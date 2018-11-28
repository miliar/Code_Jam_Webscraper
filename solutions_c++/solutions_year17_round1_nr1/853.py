#include <stdio.h>
#include <string.h>

#include <map>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

int INT(){int x;scanf("%d",&x);return x;}

char grid[33][33];
int R, C;

int main() {
	int T=INT();
	for (int t=1;t<=T;++t) {
		R=INT();C=INT();
		for (int r=0;r<R;++r)scanf("%s",grid[r]);

		for (int c=0;c<C;++c) {
			for (int r = 0; r < R;++r) {
				if (grid[r][c] == '?') {
					if (r-1 >= 0 && grid[r-1][c]!='?') {
						grid[r][c]=grid[r-1][c];
					}
				}
			}
			for (int r = R-1; r >= 0;--r) {
				if (grid[r][c] == '?') {
					if (r+1 < R && grid[r+1][c]!='?') {
						grid[r][c]=grid[r+1][c];
					}
				}
			}
		}

		for (int c = 0; c < C; ++c) {
			for (int r = 0; r < R; ++r) {
				if (grid[r][c]=='?') {
					if (c-1 >= 0 && grid[r][c-1]!='?') {
						grid[r][c] = grid[r][c-1];
					}
				}
			}
		}
		for (int c = C-1; c >= 0; --c) {
			for (int r = 0; r < R; ++r) {
				if (grid[r][c]=='?') {
					if (c+1 < C && grid[r][c+1]!='?') {
						grid[r][c] = grid[r][c+1];
					}
				}
			}
		}

		printf("Case #%d:\n", t);
		for (int r=0;r<R;++r)printf("%s\n",grid[r]);
	}
	return 0;
}
