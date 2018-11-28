#include<cstdio>

char grid[26][26];

void fill(int x0, int y0,int x1,int y1) {
	char i;

	for (int x = x0; x <= x1; x++)
		for (int y = y0; y <= y1; y++)
			if (grid[x][y] != '?')
				i = grid[x][y];

	for (int x = x0; x <= x1; x++)
		for (int y = y0; y <= y1; y++)
			grid[x][y] = i;
}

int qnt(int x0, int y0,int x1,int y1) {
	int counter = 0;
	for (int x = x0; x <= x1; x++)
		for (int y = y0; y <= y1; y++)
			if (grid[x][y] != '?')
				counter++;
	return counter;
}

void solve(int x0, int y0,int x1,int y1) {
	int q = qnt(x0, y0, x1, y1);
	if (q == 1)
		fill(x0, y0, x1, y1);
	for (int x = x0; x < x1; x++)
		if (qnt(x0, y0, x, y1) > 0 && qnt(x+1, y0, x1, y1) > 0) {
			solve(x0, y0, x, y1);
			solve(x+1, y0, x1, y1);
			return;
		}
	
	for (int y = y0; y < y1; y++)
		if (qnt(x0, y0, x1, y) > 0 && qnt(x0, y+1, x1, y1) > 0) {
			solve(x0, y0, x1, y);
			solve(x0, y+1, x1, y1);
			return;
		}
}

int main(){
	int t, r, c;
	scanf("%d", &t);

	for (int t_ = 1; t_ <= t; t_++) {
		scanf("%d %d", &r, &c);
		for (int r_ = 0 ; r_ < r; r_++)
			scanf("%s\n", grid[r_]);
		solve(0,0,r-1,c-1);
		printf("Case #%d:\n", t_);
		for (int r_ = 0 ; r_ < r; r_++)
			printf("%s\n", grid[r_]);
	}
}
