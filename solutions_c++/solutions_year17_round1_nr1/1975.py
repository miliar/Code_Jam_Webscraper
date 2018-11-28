#include<stdio.h>

int main()
{
	int t;
	scanf("%d", &t);
	for(int _t = 1; _t <= t; _t++){
		char A[30][30];
		int r, c;
		scanf("%d %d", &r, &c);
		for(int i = 0; i < r; i++)
			for(int j = 0; j < c; j++)
				scanf(" %c", &A[i][j]);

		//copy top
		for(int i = 1; i < r; i++)
			for(int j = 0; j < c; j++)
				if(A[i][j] == '?'){
					if(A[i-1][j] != '?')
						A[i][j] = A[i-1][j];
				}


		//copy bottom
		for(int i = r - 2; i >= 0; i--)
			for(int j = 0; j < c; j++)
				if(A[i][j] == '?'){
					if(A[i+1][j] != '?')
						A[i][j] = A[i+1][j];
				}

		//copy left
		for(int i = 0; i < r; i++)
			for(int j = 1; j < c; j++)
				if(A[i][j] == '?'){
					if(A[i][j-1] != '?')
						A[i][j] = A[i][j-1];
				}

		//copy right
		for(int i = 0; i < r; i++)
			for(int j = c - 2; j >= 0; j--)
				if(A[i][j] == '?'){
					if(A[i][j+1] != '?')
						A[i][j] = A[i][j+1];
				}

		printf("Case #%d:\n", _t);
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++)
				printf("%c", A[i][j]);
			printf("\n");
		}
	}
}