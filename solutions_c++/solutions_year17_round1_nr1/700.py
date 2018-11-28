#include <bits/stdc++.h>

using namespace std;

int T;
int h, w;
char grid[30][30];
bool used[200];
int lr[200], lc[200], hr[200], hc[200];

bool sortr(char a, char b) {
	return hr[a] - lr[a] > hr[b] - lr[b];
}
bool sortc(char a, char b) {
	return hc[a] - lc[a] > hc[b] - lc[b];
}

int main() {
	cin >> T;
	for (int C = 1; C <= T; C++) {
		for (int i = 0; i < 200; i++) used[i] = false;
		cin >> h >> w;
		for (int r = 0; r < h; r++)
		for (int c = 0; c < w; c++)
		{
			cin >> grid[r][c];
			int tmp = grid[r][c];
			if (tmp != '?') {
				if (used[tmp]) {
					lr[tmp] = min(lr[tmp], r);
					lc[tmp] = min(lc[tmp], c);
					hr[tmp] = max(hr[tmp], r);
					hc[tmp] = max(hc[tmp], c);
				} else {
					used[tmp] = true;
					lr[tmp] = r;
					lc[tmp] = c;
					hr[tmp] = r;
					hc[tmp] = c;
				}
			}
		}
		for (int i = int('A'); i <= int('Z'); i++) {
			if (!used[i]) continue;
			for (int r = lr[i]; r <= hr[i]; r++)
				for (int c = lc[i]; c <= hc[i]; c++)
					grid[r][c] = char(i);
		}

		char alph[30];
		for (int i = int('A'); i <= int('Z'); i++) {
			alph[i-int('A')] = char(i);
		}
		sort(alph, alph + 26, sortr);
		for (int j = 0; j < 26; j++) {
			int i = int(alph[j]);
			if (!used[i]) continue;
			while (lc[i] > 0) {
				bool can = true;
				for (int r = lr[i]; r <= hr[i]; r++)
					if (grid[r][lc[i]-1] != '?') {
						can = false;
						break;
					}
				if (can)
					for (int r = lr[i]; r <= hr[i]; r++)
						grid[r][lc[i]-1] = char(i);
				else break;
				lc[i]--;
			}
			while (hc[i] < w-1) {
				bool can = true;
				for (int r = lr[i]; r <= hr[i]; r++)
					if (grid[r][hc[i]+1] != '?') {
						can = false;
						break;
					}
				if (can)
					for (int r = lr[i]; r <= hr[i]; r++)
						grid[r][hc[i]+1] = char(i);
				else break;
				hc[i]++;
			}
		}
		for (int i = int('A'); i <= int('Z'); i++) {
			alph[i-int('A')] = char(i);
		}
		sort(alph, alph + 26, sortc);
		for (int j = 0; j < 26; j++) {
			int i = int(alph[j]);
			if (!used[i]) continue;
			while (lr[i] > 0) {
				bool can = true;
				for (int c = lc[i]; c <= hc[i]; c++)
					if (grid[lr[i]-1][c] != '?') {
						can = false;
						break;
					}
				if (can)
					for (int c = lc[i]; c <= hc[i]; c++)
						grid[lr[i]-1][c] = char(i);
				else break;
				lr[i]--;
			}
			while (hr[i] < h-1) {
				bool can = true;
				for (int c = lc[i]; c <= hc[i]; c++)
					if (grid[hr[i]+1][c] != '?') {
						can = false;
						break;
					}
				if (can)
					for (int c = lc[i]; c <= hc[i]; c++)
						grid[hr[i]+1][c] = char(i);
				else break;
				hr[i]++;
			}
		}

		cout << "Case #" << C << ":\n";
		for (int r = 0; r < h; r++) {
			for (int c = 0; c < w; c++) {
				cout << grid[r][c];
			}
			cout << '\n';
		}
	}
	return 0;
}

