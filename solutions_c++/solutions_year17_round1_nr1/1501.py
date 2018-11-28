#include <bits/stdc++.h>
using namespace std;

const int N = 30;

char cell[N][N];

int r, c;

void floodfill(int x, int y, char val, int idx){
	cell[x][y] = val;

	// printf("%d %d %c %d\n", x, y, val, idx);

	if(y > 0 && cell[x][y-1] == '?' && idx == 1)
		floodfill(x, y-1, val, idx);
	if(y < c-1 && cell[x][y+1] == '?' && idx == 1)
		floodfill(x, y+1, val, idx);

	if(x > 0 && cell[x-1][y] == '?' && idx == 2)
		floodfill(x-1, y, val, idx);
	if(x < r-1 && cell[x+1][y] == '?' && idx == 2)
		floodfill(x+1, y, val, idx);

	return;
}

int main(){
	int t, tt = 0;
	scanf("%d", &t);

	while(t--){
		scanf("%d %d", &r, &c);

		for(int i=0; i<r; i++)
			scanf("%s", cell[i]);

		for(int i=0; i<r; i++)
			for(int j=0; j<c; j++){
				if(cell[i][j] != '?'){
					floodfill(i, j, cell[i][j], 1);
				}
			}

		for(int i=0; i<r; i++)
			for(int j=0; j<c; j++){
				if(cell[i][j] != '?'){
					floodfill(i, j, cell[i][j], 2);
				}
			}

		printf("Case #%d:\n", ++tt);

		for(int i=0; i<r; i++){
			for(int j=0; j<c; j++)
				printf("%c", cell[i][j]);
			puts("");
		}
	}
}