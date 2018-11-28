#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <limits.h>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <memory.h>
#include <string.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <functional>
#include <cassert>
#include <map>
#include <set>
#include <list>

using namespace std;
typedef long long lli;
typedef vector<int> vi;
typedef vector<lli> vli;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef long double ld;

const int INF = 0x3f3f3f3f;
const lli LINF = 0x3f3f3f3f3f3f3f3f;

//#define _LOCAL_DEBUG_
#ifdef _LOCAL_DEBUG_
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...) 
#endif

const int MAX = 30;
int R, C;
char a[MAX][MAX];
int r[MAX];

void clear() {
	memset(r, 0, sizeof(r));
}

void read() {
	scanf("%d%d", &R, &C);
	for (int i = 0; i < R; i++)
		scanf("%s", a[i]);
}

void solve(int t) {
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++)
			if (a[i][j] != '?') r[i]++;
	int firstRow = 0;
	for (firstRow = 0; firstRow < R && r[firstRow] == 0; firstRow++);

	for (int ir = firstRow; ir < R; ir++) {
		if (r[ir]) {
			int firstCol = 0;
			for (firstCol = 0; firstCol < C && a[ir][firstCol] == '?'; firstCol++);
			char curColor = a[ir][firstCol];
			for (int j = 0; j < C; j++) {
				if (a[ir][j] != '?') curColor = a[ir][j];
				a[ir][j] = curColor;
			}
		}
		else
			for (int j = 0; j < C; j++) a[ir][j] = a[ir - 1][j];

		if (ir == firstRow)
			for (int i = firstRow - 1; i >= 0; i--)
				for (int j = 0; j < C; j++)
					a[i][j] = a[i + 1][j];
	}

	printf("Case #%d:\n", t);
	for (int i = 0; i < R; i++)
		printf("%s\n", a[i]);
}

int main() {
#ifdef _LOCAL_VAN
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int it = 0; it < t; it++) {
		clear();
		read();
		solve(it + 1);
	}
	return 0;
}