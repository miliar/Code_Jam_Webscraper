#include <iostream>
#include <fstream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
int t, r, c;
char map[27][27];
int txy[2][4] = { {0,0,1,-1}, {1,-1,0,0} };
char dfs(int x, int y, int dir) {
	if (x < 0 || y< 0 || x > r - 1 || y> c - 1) return '?';
	if (map[x][y] != '?') {
		if (dir == 0 || dir == 1) {
			for (int i = 2; i < 4; i++) {
				int nx = x + txy[0][i];
				int ny = y + txy[1][i];
				if (nx < 0 || ny < 0 || nx > r - 1 || ny > c - 1) continue;
				if (map[nx][ny] == map[x][y]) return '?';
			}
			return map[x][y];
		}
		if (dir == 2 || dir == 3) {
			for (int i = 0; i < 2; i++) {
				int nx = x + txy[0][i];
				int ny = y + txy[1][i];
				if (nx < 0 || ny < 0 || nx > r - 1 || ny > c - 1) continue;
				if (map[nx][ny] == map[x][y]) return '?';
			}
			return map[x][y];
		}
	}
	char a = (dfs(x + txy[0][dir], y + txy[1][dir], dir));
	map[x][y] = a;
	return a;
}
int main() {
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("out.in");
	fin >> t;
	//scanf("%d", &t);
	for (int iter = 1; iter <= t; iter++) {
		fin >> r >> c;
		//scanf("%d%d", &r, &c);
		for (int i = 0; i < r; i++) {
			fin >> map[i];
			//scanf("%s", map[i]);
			for (int j = 0; j < c; j++) {
				if (map[i][j] == '?') continue;
			}
		}
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				if (map[i][j] == '?') map[i][j] = dfs(i, j, 1);
				if (map[i][j] == '?') map[i][j] = dfs(i, j, 0);
			}
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				if (map[i][j] == '?') map[i][j] = dfs(i, j, 2);
				if (map[i][j] == '?') map[i][j] = dfs(i, j, 3);
			}
	
		for (int i = 1; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (map[i][j] == '?' && map[i - 1][j] != '?' ) strcpy(map[i], map[i - 1]);
			}
		}
		for (int i = r-2; i > -1; i--) {
			for (int j = 0; j < c; j++) {
				if (map[i][j] == '?' && map[i + 1][j] != '?') strcpy(map[i], map[i + 1]);
			}
		}
		
		fout << "Case #" << iter << ":\n";
		for (int i = 0; i < r; i++)
			fout << map[i] << '\n';
			//printf("%s\n", map[i]);

	}
	fin.close();
	fout.close();
	return 0;
}