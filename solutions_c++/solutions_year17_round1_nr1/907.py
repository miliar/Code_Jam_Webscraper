#include <bits/stdc++.h>
using namespace std;

int R, C;
vector<string> grid;

bool cands[26];
int loX[26];
int loY[26];
int hiX[26];
int hiY[26];

bool inRect(int x, int y, int lx, int ly, int hx, int hy) {
	return (lx <= x && x <= hx && ly <= y && y <= hy);
}

bool between(int z, int x, int y) {
	return (x <= z && z <= y);
}

bool canPut(int c, int lx, int ly, int hx, int hy) {
	//cout << (char)('A'+c) << endl;
	// check each pair
	for (int k = 0; k < 26; k++) {
		if (k == c || !cands[k]) {
			continue;
		}
		
		if (!(hiX[k] < lx || hx < loX[k] || hiY[k] < ly || hy < loY[k])) {
			return false;
		}
		
		//if (between(loX[k], lx, hx)) return false;
		//if (between(hiX[k], lx, hx)) return false;
		//if (between(loY[k], ly, hy)) return false;
		//if (between(hiY[k], ly, hy)) return false;
		
		//if (inRect(loX[k], loY[k], lx, ly, hx, hy)) return false;
		//if (inRect(loX[k], hiY[k], lx, ly, hx, hy)) return false;
		
		//if (inRect(lx, ly, loX[k], loY[k], hiX[k], hiY[k])) return false;
		//if (inRect(lx, hy, loX[k], loY[k], hiX[k], hiY[k])) return false;
		
		
		//if (inRect(hiX[k], loY[k], lx, ly, hx, hy)) return false;
		//if (inRect(hiX[k], hiY[k], lx, ly, hx, hy)) return false;
	}
	return true;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		grid.clear();
		cin >> R >> C;
		grid.resize(R);
		for (int i = 0; i < R; i++) {
			cin >> grid[i];
		}
		
		//cout << "Case #" << icase << ":" << endl;
		//for (int i = 0; i < R; i++) {
			//cout << grid[i] << endl;
		//}
		
		memset(cands, 0, sizeof cands);
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (grid[i][j] != '?') {
					int k = grid[i][j] - 'A';
					if (!cands[k]) {
						cands[k] = true;
						hiX[k] = loX[k] = i;
						hiY[k] = loY[k] = j;
					} else {
						loX[k] = min(loX[k], i);
						loY[k] = min(loY[k], j);
						hiX[k] = max(hiX[k], i);
						hiY[k] = max(hiY[k], j);
					}
				}
			}
		}
		
		
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (grid[i][j] == '?') {
					// find something to fill in here
					for (int k = 0; k < 26; k++) {
						int lx = min(loX[k], i);
						int ly = min(loY[k], j);
						int hx = max(hiX[k], i);
						int hy = max(hiY[k], j);
						
						if (cands[k] && canPut(k, lx, ly, hx, hy)) {
							grid[i][j] = (char)('A' + k);
							
							loX[k] = min(loX[k], i);
							loY[k] = min(loY[k], j);
							hiX[k] = max(hiX[k], i);
							hiY[k] = max(hiY[k], j);
						}
					}
				}
			}
		}
		
		cout << "Case #" << icase << ":" << endl;
		for (int i = 0; i < R; i++) {
			cout << grid[i] << endl;
		}
	}
	return 0;
}
