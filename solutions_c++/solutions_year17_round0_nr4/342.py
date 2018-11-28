#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const int size = 500;

bool hvused[size][size];
bool dused[size][size];
char origin[size][size];
char field[size][size];
bool hban[size], vban[size], xpyban[size], xmyban[size]; 
bool way[size][size];
bool used[size];
int lnb[size], rnb[size];

bool dfs(int n, int v) {
	if (used[v])
		return false;
	used[v] = true;
	for (int i = 0; i < n; i++)
		if (way[v][i] && (rnb[i] == -1 || dfs(n, rnb[i]))) {
			lnb[v] = i;
			rnb[i] = v;

			return true;
		}

	return false;
}

void find_maximum_matching(int n) {
	for (int i = 0; i < n; i++) {
		if (lnb[i] == -1) {
			for (int j = 0; j < n; j++)
				used[j] = false;
			dfs(n, i);
		}
	}
}

void mark_hor_and_ver(int n) {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++) {
			way[i][j] = (!hban[i] && !vban[j]);			
		}	
	for (int i = 0; i < n; i++) {
		lnb[i] = rnb[i] = -1;
		if (hban[i])
			lnb[i] = -2;
		if (vban[i])
			rnb[i] = -2;
	}

	find_maximum_matching(n);
	for (int i = 0; i < n; i++)
		if (lnb[i] >= 0) {
			hvused[i][lnb[i]] = true;
		}
}

void mark_diagonals(int n) {
	for (int i = 0; i < 2 * n; i++)
		for (int j = 0; j < 2 * n; j++)
			way[i][j] = false;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++) {
			way[i + j][i - j + n - 1] = (!xpyban[i + j] && !xmyban[i - j + n - 1]);
		}
	for (int i = 0; i < 2 * n; i++) {
		lnb[i] = rnb[i] = -1;
		if (xpyban[i])
			lnb[i] = -2;
		if (xmyban[i])
			rnb[i] = -2;
	}

	find_maximum_matching(2 * n - 1);
	for (int i = 0; i < 2 * n - 1; i++)
		if (lnb[i] >= 0) {
			dused[(i + lnb[i] - (n - 1)) / 2][(i - (lnb[i] - (n - 1))) / 2] = true;
		}
}

int main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tc;
    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
    	int n, m;
    	cin >> n >> m;
		for (int i = 0; i < n; i++) 
			for (int j = 0; j < n; j++) {
				hvused[i][j] = false;
				dused[i][j] = false;
				origin[i][j] = '.';
				field[i][j] = '.';
			}
		for (int i = 0; i < 2 * n; i++) {
			hban[i] = false;
			vban[i] = false;
			xpyban[i] = false;
			xmyban[i] = false;
		}

		for (int i = 0; i < m; i++) {
			char tp;
			int x, y;
			cin >> tp >> x >> y;
			x--, y--;
			origin[x][y] = tp;
	
			if (tp == '+' || tp == 'o') {
				dused[x][y] = true;
				xpyban[x + y] = true;
				xmyban[x - y + n - 1] = true;
			}
			if (tp == 'x' || tp == 'o') {
				hvused[x][y] = true;
				hban[x] = true;
				vban[y] = true;
			}
		}

		mark_hor_and_ver(n);
		mark_diagonals(n);

		int ans = 0;
		int cnt = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++) {
				ans += dused[i][j];
				ans += hvused[i][j];

				if (dused[i][j] && !hvused[i][j]) {
					field[i][j] = '+';
				}
				if (!dused[i][j] && hvused[i][j]) {
					field[i][j] = 'x';
				}
				if (dused[i][j] && hvused[i][j]) {
					field[i][j] = 'o';
				}

				if (field[i][j] != origin[i][j])
					cnt++;
			}

	    cout << "Case #" << tnum + 1 << ": " << ans << ' ' << cnt << endl;
	    for (int i = 0; i < n; i++) {
	    	for (int j = 0; j < n; j++) {
	    		if (field[i][j] != origin[i][j]) {
	    			cout << field[i][j] << ' ' << i + 1 << ' ' << j + 1 << endl;
	    		}
	    	}
	    }
    }

    return 0;
}