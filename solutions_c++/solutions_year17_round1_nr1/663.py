#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int main(void) {
	int T, R, C, r, c, i;
	char ar[32][32];
	int blankRow[32], blankCol[32];
	cin >> T;
	for (int t=1; t<=T; t++) {
		printf("Case #%d: ", t);
		cin >> R >> C;
		for (r=0; r<R; r++) for (c=0; c<C; c++) cin >> ar[r][c];
		
		//for (r=0; r<R; r++) { printf("\n"); for (c=0; c<C; c++) printf("%c", ar[r][c]); } printf("\n");
		
		for (r=0; r<R; r++) blankRow[r] = 0;
		for (c=0; c<C; c++) blankCol[c] = 0;
		for (r=0; r<R; r++) {
			for (c=0; c<C; c++) if (ar[r][c] != '?') break;
			if (c == C) blankRow[r] = 1;
			//printf("blankRow[%d] %d\n", r, blankRow[r]);
		}
		for (c=0; c<C; c++) {
			for (r=0; r<R; r++) if (ar[r][c] != '?') break;
			if (r == R) blankCol[c] = 1;
			//printf("blankCol[%d] %d\n", c, blankCol[c]);
		}
		
		for (r=0; r<R; r++) if (!blankRow[r]) {
			for (c=0; c<C; c++) if (!blankCol[c]) {
				for (i=c-1; i>=0; i--) {
					if (!blankCol[i]) {
						if (ar[r][i] == '?') ar[r][i] = ar[r][c];
						else break;
					}
				}
				for (i=c+1; i<C; i++) {
					if (!blankCol[i]) {
						if (ar[r][i] == '?') ar[r][i] = ar[r][c];
						else break;
					}
				}
			}
		}
		
		//for (r=0; r<R; r++) { printf("\n"); for (c=0; c<C; c++) printf("%c", ar[r][c]); } printf("\n");
		
		for (c=0; c<C; c++) if (!blankCol[c]) {
			for (i=c-1; i>=0; i--) {
				if (!blankCol[i]) break;
				for (r=0; r<R; r++) ar[r][i] = ar[r][c];
			}
			for (i=c+1; i<C; i++) {
				if (!blankCol[i]) break;
				for (r=0; r<R; r++) ar[r][i] = ar[r][c];
			}
		}
		
		//for (r=0; r<R; r++) { printf("\n"); for (c=0; c<C; c++) printf("%c", ar[r][c]); } printf("\n");
		
		for (r=0; r<R; r++) if (!blankRow[r]) {
			for (i=r-1; i>=0; i--) {
				if (!blankRow[i]) break;
				for (c=0; c<C; c++) ar[i][c] = ar[r][c];
			}
			for (i=r+1; i<R; i++) {
				if (!blankRow[i]) break;
				for (c=0; c<C; c++) ar[i][c] = ar[r][c];
			}
		}
		
		for (r=0; r<R; r++) { printf("\n"); for (c=0; c<C; c++) printf("%c", ar[r][c]); } printf("\n");
		
		//printf("\n");
	}
	
	return 0;
}