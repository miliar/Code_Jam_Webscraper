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

const int N = 110;

int e[N], v[N];
long long d[N][N];
int can[N][N];
double t[N][N];

int main() {
	int T;
	scanf("%d", &T);
	for(int cc = 1; cc <= T; ++cc) {
		int n, q;
		scanf("%d%d", &n, &q);
		for(int i = 0; i < n; ++i) {
			scanf("%d%d", e + i, v + i);
		}
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < n; ++j) {
				int x;
				scanf("%d", &x);
				d[i][j] = x;
			}
			d[i][i] = 0;
		}
		for(int k = 0; k < n; ++k) {
			for(int i = 0; i < n; ++i) {
				for(int j = 0; j < n; ++j) {
					if(d[i][k] != -1 && d[k][j] != -1) {
						long long tmp = d[i][k] + d[k][j];
						if(d[i][j] == -1) d[i][j] = tmp;
						else d[i][j] = min(d[i][j], tmp);
					}
				}
			}
		}
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < n; ++j) {
				if(d[i][j] != -1 && d[i][j] <= e[i]) {
					can[i][j] = 1;
					t[i][j] = ((double)d[i][j]) / v[i];
				} else can[i][j] = 0;
			}
		}
		for(int k = 0; k < n; ++k) {
			for(int i = 0; i < n; ++i) {
				for(int j = 0; j < n; ++j) {
					if(can[i][k] && can[k][j]) {
						double tmp = t[i][k] + t[k][j];
						if (can[i][j] == 0) {
							can[i][j] = 1;
							t[i][j] = tmp;
						} else {
							t[i][j] = min(tmp, t[i][j]);
						}
					}
				}
			}
		}
		printf("Case #%d:", cc);
		for(int i = 0; i < q; ++i){
			int x, y;
			scanf("%d%d", &x, &y);
			x--;
			y--;
			printf(" %.10f", t[x][y]);
		}
		printf("\n");
	}
	return 0;
}

