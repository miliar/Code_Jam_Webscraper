#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int t, T;
int N, M;
int input[120][120];
int rook[120][120];
int bishop[120][120];
char ansc[500];
int ansxy[500][2];

bool rowcheck[120];
bool colcheck[120];

int main() {
	scanf("%d", &T);
	for(t = 1; t <= T; t++) {
		char c[20];
		int i, j, x, y;
		int point, count;
		scanf("%d %d", &N, &M);
		for(i = 0; i <= N; i++) {
			for(j = 0; j <= N; j++) {
				input[i][j] = 0;
				rook[i][j] = 0;
				bishop[i][j] = 0;
			}
			rowcheck[i] = colcheck[i] = false;
		}
		for(i = 0; i < M; i++) {
			scanf("%s %d %d", c, &x, &y);
			if(c[0] == '+') {
				input[x-1][y-1] = 1;
				bishop[x-1][y-1] = 1; 
			} else if(c[0] == 'x') {
				input[x-1][y-1] = 2;
				rook[x-1][y-1] = 1; 
				rowcheck[x-1] = true;
				colcheck[y-1] = true;
			} else if(c[0] == 'o') {
				input[x-1][y-1] = 3;
				bishop[x-1][y-1] = 1; 
				rook[x-1][y-1] = 1; 
				rowcheck[x-1] = true;
				colcheck[y-1] = true;
			} else {
				printf("ERROR!\n");
			}
		}
		x = y = 0;
		while(rowcheck[x]) x++;
		while(colcheck[y]) y++;
		while(x < N && y < N) {
			rook[x][y] = 1;
			rowcheck[x] = colcheck[y] = true;
			while(rowcheck[x]) x++;
			while(colcheck[y]) y++;
		}
		//small
		bishop[0][0] = 1;
		bishop[0][N-1] = 1;
		for(i = 1; i < N-1; i++) {
			bishop[0][i] = 1;
			bishop[N-1][i] = 1;
		}
		count = point = 0;
		for(i = 0; i < N; i++) {
			for(j = 0; j < N; j++) {
				point = point + rook[i][j] + bishop[i][j];
				if(input[i][j] < rook[i][j] * 2 + bishop[i][j]) {
					ansxy[count][0] = i + 1;
					ansxy[count][1] = j + 1;
					if(rook[i][j] * 2 + bishop[i][j] == 1) ansc[count] = '+';
					else if(rook[i][j] * 2 + bishop[i][j] == 2) ansc[count] = 'x';
					else if(rook[i][j] * 2 + bishop[i][j] == 3) ansc[count] = 'o';
					else printf("ERROR!\n");
					count++;
				}
			}
		}

		printf("Case #%d: %d %d\n", t, point, count);
		for(i = 0; i < count; i++) {
			printf("%c %d %d\n", ansc[i], ansxy[i][0], ansxy[i][1]);
		}
	}
	return 0;
}
