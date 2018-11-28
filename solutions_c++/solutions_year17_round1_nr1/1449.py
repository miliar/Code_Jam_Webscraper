#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int chs = 26;

int casei, cases, n, m;
int coor[33][2];
char board[33][33];

void split(int up, int down, int left, int right) {
	int ch1 = -1, ch2 = -1;
	for (int i = 0; i < chs; ++i) 
		if (coor[i][0] >= up && coor[i][0] < down && coor[i][1] >= left && coor[i][1] < right) {
			if (ch1 == -1) {
				ch1 = i;
			}
			else {
				ch2 = i;
				break;
			}
		}
	
	if (ch2 == -1) {
		ch1 += 'A';
		for (int i = up; i < down; ++i)
			for (int j = left; j < right; ++j) board[i][j] = (char)ch1;
		return;
	}
	
	if (coor[ch1][0] != coor[ch2][0]) {
		int line = min(coor[ch1][0], coor[ch2][0]) + 1;
		split(up, line, left, right);
		split(line, down, left, right);
	}
	else {
		int line = min(coor[ch1][1], coor[ch2][1]) + 1;
		split(up, down, left, line);
		split(up, down, line, right);
	}
}

int main() {
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) scanf(" %s", board[i]);
		memset(coor, 255, sizeof(coor));
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j) if (board[i][j] != '?') {
				int ch = board[i][j] - 'A';
				coor[ch][0] = i;
				coor[ch][1] = j;
			}
		
		split(0, n, 0, m);
		
		printf("Case #%d:\n", casei);
		for (int i = 0; i < n; ++i) printf("%s\n", board[i]);
	}
	return 0;
}
