#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
FILE *fi = freopen("A-large.in", "r", stdin);
FILE *fo = freopen("ALout.txt", "w", stdout);
string str[40];
int test,row, col;
void go(int y, int x, char ch)
{
	int tmpy = y, tmpx = x;
	--y;
	while (y >= 0) {
		if (str[y][x] != '?')break;
		str[y][x] = ch; 
		--y;
	}
	y = tmpy;
	++y;
	while (y < row) {
		if (str[y][x] != '?')break;
		str[y][x] = ch;
		++y;
	}
}
char whats(int y, int x)
{
	int tmpx = x;
	while(x<col) {
		if (str[y][x] != '?')return str[y][x];
		++x;
	}
	x = tmpx;
	while (x >= 0) {
		if (str[y][x] != '?')return str[y][x];
		--x;
	}
	return '!';
}
int main() {
	scanf("%d", &test); int lev = 0;
	while (test--) {
		++lev;
		scanf("%d %d", &row, &col);
		for (int i = 0; i < row; i++)cin >> str[i];
		for (int j = 0; j < col; j++) {
			for (int i = 0; i < row; i++) {
				if (str[i][j] != '?') {
					go(i, j, str[i][j]);
				}
			}
		}
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				if (str[i][j] == '?') {
					str[i][j] = whats(i, j);
				}
			}
		}
		printf("Case #%d:\n", lev);
		for (int i = 0; i < row; i++)cout << str[i] << endl;
	}
}