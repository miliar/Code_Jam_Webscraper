#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

int row[200], col[200], rc[200][200];
int sum[300], diff[400], sd[200][200];

int n;

void tryline(int s, int d) {
	if(sum[s] == 0 && diff[d] == 0) {
		sum[s] = 1;
		diff[d] = 1;
		assert((s + d - n) % 2 == 0);
		assert((s - d + n) % 2 == 0);
		sd[(s + d - n) / 2][(s - d + n) / 2] = 2;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for(int cc = 1; cc <= T; ++cc) {
		int m, x, y;
		char ch;
		memset(row, 0, sizeof(row));
		memset(col, 0, sizeof(col));
		memset(rc, 0, sizeof(rc));
		memset(sum, 0, sizeof(sum));
		memset(diff, 0, sizeof(diff));
		memset(sd, 0, sizeof(sd));
		scanf("%d%d", &n, &m);
		for(int i = 0; i < m; ++i){
			scanf(" %c %d %d", &ch, &x, &y);
			if(ch != '+') {
				row[x] = 1;
				col[y] = 1;
				rc[x][y] = 1;
			}
			if(ch != 'x') {
				sum[x + y] = 1;
				diff[n + x - y] = 1;
				sd[x][y] = 1;
			}
		}
		for(int i = 1; i <= n; ++i){
			for(int j = 1; j <= n; ++j){
				if(row[i] == 0 && col[j] == 0) {
					row[i] = col[j] = 1;
					rc[i][j] = 2;
				}
			}
		}
		for(int i = 0; i < n; ++i) {
			if(i % 2 == 0) {
				for(int j = 0; j <= i / 2; ++j) {
					tryline(2 + i, n + j * 2);
					tryline(2 + i, n - j * 2);
					tryline(n + n - i, n + j * 2);
					tryline(n + n - i, n - j * 2);
				}
			} else {
				for(int j = 0; j <= i / 2; ++j) {
					tryline(2 + i, n + j * 2 + 1);
					tryline(2 + i, n - j * 2 - 1);
					tryline(n + n - i, n + j * 2 + 1);
					tryline(n + n - i, n - j * 2 - 1);
				}
			}
		}
		int sum = 0, cnt = 0;
		for(int i = 1; i <= n; ++i) {
			for(int j = 1; j <= n; ++j){
				if(rc[i][j]) ++sum;
				if(sd[i][j]) ++sum;
				if(rc[i][j] == 2 || sd[i][j] == 2) ++cnt;
			}
		}
		printf("Case #%d: %d %d\n", cc, sum, cnt);
		for(int i = 1; i <= n; ++i) {
			for(int j = 1; j <= n; ++j){
				if(rc[i][j] == 2 || sd[i][j] == 2) {
					if(rc[i][j] == 0) {
						printf("+ %d %d\n", i, j);
					} else if (sd[i][j] == 0) {
						printf("x %d %d\n", i, j);
					} else {
						printf("o %d %d\n", i, j);
					}
				}
			}
		}
	}
	return 0;
}

