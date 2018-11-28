#include <bits/stdc++.h>

using namespace std;

const int N = 30;

char v[N][N], r[N][N];
int f[N][N][N][N];

char check(int y, int x, int n, int m)
{
    char c = '?';
    for (int i = y; i < n; ++i)
	for (int j = x; j < m; ++j)
	    if (v[i][j] != '?')
		if (c == '?')
		    c = v[i][j];
		else
		    return 'X';
    return c;
}

int fill(int y, int x, int n, int m)
{
    if (f[y][x][n][m] == 0) {
	char c = check(y, x, n, m);
	if (c == '?')
	    f[y][x][n][m] = -1;
	else if (c != 'X') {
	    for (int i = y ; i < n; ++i)
		for (int j = x; j < m; ++j)
		    r[i][j] = c;
	    f[y][x][n][m] = 1;
	}
	else {
	    for (int i = y + 1; i < n; ++i)
		if (fill(y, x, i, m) == 1 && fill(i, x, n, m) == 1) {
		    f[y][x][n][m] = 1;
		    goto lbl;
		}
	    for (int j = x + 1; j < m; ++j)
		if (fill(y, x, n, j) == 1 && fill(y, j, n, m) == 1) {
		    f[y][x][n][m] = 1;
		    goto lbl;
		}
	    f[y][x][n][m] = -1;
	lbl:
	    ;
	}
	
	    
	/*cout << "[" << y << ", " << x << "] -> (" << n << ", " << m << "): " << f[y][x][n][m] << endl;
	for (int i = y; i < n; ++i) {
	    for (int j = x; j < m; ++j)
		cout << v[i][j];
	    cout << endl;
	    }*/
    }
    return f[y][x][n][m];
}

int main()
{
    int __; cin >> __;
    for (int _ = 0; _ < __; ++_) {
	int n, m; cin >> n >> m;
	memset(f, 0, sizeof(f));
	for (int i = 0; i < n; ++i)
	    for (int j = 0; j < m; ++j)
		cin >> v[i][j];
	assert(fill(0, 0, n, m) == 1);
	cout << "Case #" << (_ + 1) << ":" << endl;
	for (int i = 0; i < n; ++i) {
	    for (int j = 0; j < m; ++j)
		cout << r[i][j];
	    cout << endl;
	}
    }
    return 0;
}
