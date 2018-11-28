#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstdlib>
#include <ctime>
#include <deque>
using namespace std;
int n, a[210][210], xxx[210][210], yyy[210][210];
int ans;
int b[210][210];
int Link[210], go[210][210];
bool used[210];

bool check(int x, int y) {
	if (a[x][y] && a[x][y] != 1) {
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				if ((i == x || j == y) && (i != x || j != y) && a[i][j] && a[i][j] != 1)
					return false;
	}
	if (a[x][y] && a[x][y] != 2) {
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				if ((i + j == x + y || i - j == x - y) && (i != x || j != y) && a[i][j] && a[i][j] != 2)
					return false;
	}
	return true;
}

bool fi(int k, int m) {
	for (int j = 1; j <= m; j++)
		if (go[k][j] && !used[j]) {
			used[j] = true;
			if (!Link[j] || fi(Link[j], m)) {
				Link[j] = k;
				return true;
			}
		}
	return false;
}

void doit() {
	memset(a, 0, sizeof a);
	int k;
	scanf("%d%d", &n, &k);
	
	for (int i = 1; i <= k; i++) {
		char c;
		for (c = getchar(); c <= 32; c = getchar());
		int x, y;
		scanf("%d%d", &x, &y);
		if (c == 'o')
			a[x][y] = 3;
		else if (c == 'x')
			a[x][y] = 2;
		else a[x][y] = 1;
	}
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++) {
			go[i][j] = 1;
			for (int p = 1; p <= n; p++)
				if ((a[i][p] & 2) || (a[p][j] & 2))
					go[i][j] = 0;
		}
	for (int i = 1; i <= n; i++)
		Link[i] = 0;
	for (int i = 1; i <= n; i++) {
		memset(used, false, sizeof used);
		fi(i, n);
	}
	memset(b, 0, sizeof b);
	for (int i = 1; i <= n; i++)
		if (Link[i])
			b[Link[i]][i] |= 2;

	memset(go, 0, sizeof go);
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++) {
			xxx[i + j][i - j + n] = i;
			yyy[i + j][i - j + n] = j;
			go[i + j][i - j + n] = 1;
			for (int p = 1; p <= n; p++)
				for (int q = 1; q <= n; q++)
					if ((p + q == i + j || p - q == i - j) && (a[p][q] & 1))
						go[i + j][i - j + n] = 0;
			
		}
	for (int i = 1; i <= 2 * n; i++)
		Link[i] = 0;
	for (int i = 1; i <= 2 * n; i++) {
		memset(used, false, sizeof used);
		fi(i, 2 * n);
	}
	for (int i = 1; i <= 2 * n; i++)
		if (Link[i])
			b[xxx[Link[i]][i]][yyy[Link[i]][i]] |= 1;
	
	int ans = 0, cnt = 0;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++) {
			a[i][j] |= b[i][j];
			if (a[i][j] & 1)
				ans += 1;
			if (a[i][j] & 2)
				ans += 1;
			if (b[i][j])
				cnt += 1;
		}
	printf("%d %d\n", ans, cnt);
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			if (b[i][j]) {
				if (a[i][j] == 3)
					printf("o ");
				if (a[i][j] == 2)
					printf("x ");
				if (a[i][j] == 1)
					printf("+ ");
				
				printf("%d %d\n", i, j);
			}
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        doit();
    }
}