#include<stdio.h>
#include<stdlib.h>


using namespace std;


const int MAXN = 30;

int main () {
	char matrix[MAXN][MAXN];
	
	int t, count, rll, c, first_char;
	int last_row;
	scanf("%d ", &t);
	count = 0;
	
	while (t--) {
		count ++;
		scanf("%d %d", &rll, &c);
		
//printf("r = %d, c = %d \n", rll, c);		
		
		for (int i=1; i<=rll; i++) {
			for (int j=1; j<=c; j++) {
				scanf(" %c", &matrix[i][j]);
				if (matrix[i][j] != '?') last_row = i;
			}
		}

	
		for (int i=last_row; i>=1; i--) {
			first_char = '?';
			for (int j=1; j<=c; j++) {
				if (matrix[i][j] != first_char) {
					first_char = matrix[i][j];
					break;
				}
				
				 
			}
//printf("first char: %c\n", first_char);			
			if (first_char == '?') {
				for (int j=1; j<=c; j++) {
					matrix[i][j] = matrix[i+1][j];
				}
			} else {
				for (int j=1; j<=c; j++) {
					if (matrix[i][j] == '?') {
						matrix[i][j] = first_char;
					} else {
						first_char = matrix[i][j];
					}
				}
			}
			
		}
		
		for (int i=last_row+1; i<= rll; i++) {
			for (int j=1; j<=c; j++) {
				matrix[i][j] = matrix[i-1][j];
			}
		}
//printf("cheguei\n");

		printf("Case #%d: \n", count);		
		for (int i=1; i<=rll; i++) {
			for (int j=1; j<=c; j++) {
				printf("%c", matrix[i][j]);
				
			}
			printf("\n");
		}
		
	}
	
	
	return 0;
}
