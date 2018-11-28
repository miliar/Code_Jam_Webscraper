// coder : davidwang
#include "MyLib.hpp"
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

struct Board{
	enum{ MaxSize = 30};
	int x[MaxSize + 1][MaxSize + 1];
	Board(){
		memset(x, 0, sizeof(x));
	}
	int *operator[](const int &t){
		return x[t];
	}
	void init(){
		for (int i = 1;i <= MaxSize;i++)
			for (int j = 1;j <= MaxSize;j++)
				x[i][j] += x[i - 1][j] + x[i][j - 1] - x[i - 1][j - 1];
	}

	int get(int x0, int y0, int x1 = -1, int y1 = -1){
		if (x1 == -1 && y1 == -1){
			x1 = x0;
			y1 = y0;
		}
		return x[x1][y1] - x[x0 - 1][y1] - x[x1][y0 - 1] + x[x0 - 1][y0 - 1];
	}
}b[30];

int grid[Board::MaxSize][Board::MaxSize];
char s[100];
int tt;
void solve(int x0, int y0,int x1, int y1){
	//fprintf(stderr, "solve(%d, %d, %d, %d) in Case %d\n", x0, y0, x1, y1, tt);
	int Count = 0, lastPos = -1;
	for (int i = 0;i < 26;i++){
		if (b[i].get(x0, y0, x1, y1)){
			Count++;
			lastPos = i;
		}
	}
	// 只有一种了
	if (Count == 1){
		for (int i = x0;i <= x1;i++){
			for (int j = y0;j <= y1;j++){
				grid[i][j] = lastPos;
			}
		}
		return;
	}
	// 我们需要考虑横向分割
	for (int x = x0;x < x1;x++){
		// 分开的有一部分没有东西
		if (b[26].get(x0, y0, x, y1) == 0 || b[26].get(x+1, y0, x1, y1) == 0)
			continue;
		int flag = 1;
//		for (int j = y0;j <= y1;j++){
//			if (grid[x][j] == grid[x+1][j]){
//				flag = 0;
//				break;
//			}
//		}
		// 不能分开
		if (flag == 0) continue;
		solve(x0, y0, x, y1);
		solve(x+1, y0, x1, y1);
		return;
	}

	for (int y = y0;y < y1;y++){
		if (b[26].get(x0, y0, x1, y) == 0 || b[26].get(x0,y+1, x1, y1) == 0)
			continue;
		int flag = 1;
//		for (int i = x0;i <= x1;i++){
//			if (grid[i][y] == grid[i][y+1]){
//				flag = 0;
//				break;
//			}
//		}
		if (flag == 0) continue;
		solve(x0, y0, x1, y);
		solve(x0, y+1, x1, y1);
		return;
	}
}
int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T = read();
	for (tt = 1;tt <= T; tt++){
		printf("Case #%d:\n", tt);
		for (int i = 0;i <= 26;i++){
			memset(b[i].x, 0, sizeof(b[i].x));
		}
		int n = read(), m = read();
		for (int i = 1;i <= n;i++){
			scanf("%s", s+1);
			for (int j = 1;j <= m;j++){
				if (s[j] == '?') grid[i][j] = -1;
				else grid[i][j] = s[j] - 'A';
	//			update(i, j);
			}
		}
		for (int i = 1;i <= n;i++){
			for (int j = 1;j <= m;j++){
				if (grid[i][j] != -1){
					b[grid[i][j]][i][j] = 1;
					b[26][i][j] = 1;
				}
			}
		}
		for (int i = 0;i <= 26;i++) b[i].init();
		solve(1, 1, n, m);
		for (int i = 1;i <= n;i++){
			for (int j = 1;j <= m;j++){
				if (grid[i][j] < 0){
					fprintf(stderr, "Not compilited [%d, %d] in Case %d\n", i, j, tt);
				}else{
					putchar('A' + grid[i][j]);
				}
			}
			printf("\n");
		}
	}// End of solving one interation!
	return 0;
}
