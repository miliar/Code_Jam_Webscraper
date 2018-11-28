#include <bits/stdc++.h>

#define N 1000007
#define it(i, n) for(i = 0; i < n; ++i)
#define pb push_back
#define eps 1e-9
#define all(x) x.begin(), x.end() 

using namespace std;
typedef long long ll;

char grid[100][100];
int seen[300];
int n, m;

bool column_differs(char c, int i1, int i2, int j1, int j2) {
	int i, j;
	for(i = i1; i <= i2; ++i) {
		for(j = j1; j <= j2; ++j)
			if(grid[i][j] != '?' and grid[i][j] != c) return true;
	}
	return false;
}

bool row_differs(char c, int i1, int i2, int j1, int j2) {
	int i, j;
	for(i = i1; i <= i2; ++i) {
		for(j = j1; j <= j2; ++j)
			if(grid[i][j] != '?' and grid[i][j] != c) return true;
	}
	return false;
}

void paint(int p, int q) {
	int i, j;
	int i1, i2, j1, j2;
	char c = grid[p][q];
	if(seen[c]) return;
	seen[c] = true;
	j1 = j2 = q;
	i1 = i2 = p;

	for(i = p; i >= 0 and row_differs(c, i, p, j1, j2) == false; --i);
	i1 = i+1;
	for(i = p; i < n and row_differs(c, p, i, j1, j2) == false; ++i);
	i2 = i-1;
	for(i = q; i >= 0 and column_differs(c, i1, i2, i, q) == false; --i);
	j1 = i+1;
	for(i = q; i < m and column_differs(c, i1, i2, q, i) == false; ++i);
	j2 = i-1;
	for(i = i1; i <= i2; ++i) {
		for(j = j1; j <= j2; ++j) {
			grid[i][j] = c;
		}
	}
}

void run() {
	int i, j, k, t, p, q;
	char c;

	scanf("%d %d", &n, &m);

	it(i, n) {
		it(j, m) {
			cin >> grid[i][j];
		}
	}

	for(i = 0; i < n; ++i) {
		c = '?';
		for(j = 0; j < m; ++j) {
			if(grid[i][j] == '?') grid[i][j] = c;
			c = grid[i][j];
		}
		for(j = m-1; j >= 0; --j) {
			if(grid[i][j] == '?') grid[i][j] = c;
			c = grid[i][j];
		}
	}

	for(i = 0; i < m; ++i) {
		c = '?';
		for(j = 0; j < n; ++j) {
			if(grid[j][i] == '?') grid[j][i] = c;
			c = grid[j][i];
		}
		for(j = n-1; j >= 0; --j) {
			if(grid[j][i] == '?') grid[j][i] = c;
			c = grid[j][i];
		}
	}

	it(i, n) {
		it(j, m) {
			cout << grid[i][j];
		}
		cout << endl;
	}
}

int main(int argc, char * argv[]) {
	int i, j, t;
	scanf("%d", &t);
	for(i = 0; i < t; ++i) {
		printf("Case #%d:\n", i+1);
		run();
	}
	return 0;
}