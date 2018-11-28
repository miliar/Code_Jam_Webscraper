#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

#define MaxN 1010

using namespace std;

int N, M, T;
char str[MaxN][MaxN];

void search(int low_x, int low_y, int up_x, int up_y) {
	int count = 0, lastrow, lastcol, firstrow, firstcol;
	char c;
	for (int i = low_x; i < up_x; ++i) {
		for (int j = low_y; j < up_y; ++j) {
			if (str[i][j] != '?') {
				++count;
				if (count == 1) {
					firstrow = i;
					firstcol = j;
				}
				lastrow = i;
				lastcol = j;
				c = str[i][j];
			}
		}
	}
	if (count == 1) {
		for (int i = low_x; i < up_x; ++i)
			for (int j = low_y; j < up_y; ++j)
				if (str[i][j] == '?')
					str[i][j] = c;
		return ;
	}
	if (lastrow != firstrow) {
		search(low_x, low_y, lastrow, up_y);
		search(lastrow, low_y, up_x, up_y);
		return ;
	}
	search(low_x, low_y, up_x, lastcol);
	search(low_x, lastcol, up_x, up_y);
}
int main(){
	int T0 = 0;
	scanf("%d", &T);
	for ( ; T; --T) {
		scanf("%d%d", &N, &M);
		for (int i = 0; i < N; ++i)
			scanf("%s", str[i]);
		search(0, 0, N, M);
		printf("Case #%d:\n", ++T0);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < M; ++j) {
				printf("%c", str[i][j]);
			}
			puts("");
		}
	}
	return 0;
}