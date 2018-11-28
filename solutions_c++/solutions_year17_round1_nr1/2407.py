#include <stdio.h>

void solve (char **cake, int R, int C) {
	int emp_cnt[R]={0};
	for (int i=0; i<R; i++) {
		for (int j=0; j<C; j++) {
			if (cake[i][j]!='?') {
				if (j>0) {
					for (int k=j-1; k>=0; k--) {
						if (cake[i][k]=='?') 
							cake[i][k]=cake[i][j];
					}
				}
				if (j<C-1) {
					for (int k=j+1; k<C; k++) {
						if (cake[i][k]!='?') break;
						if (cake[i][k]=='?')
							cake[i][k]=cake[i][j];
					}
				}
			}
			if (cake[i][j]=='?') emp_cnt[i]++;
		}
	
	}
	//for (int i=0; i<R; i++)
	//	printf("%d\n", emp_cnt[i]);
	for (int i=0; i<R; i++) {
		if(emp_cnt[i]!=C) {
			if (i>0) {
				for (int j=i-1; j>=0; j--) {
					if (emp_cnt[j]==C) {
						for (int k=0; k<C; k++) {
							cake[j][k]=cake[i][k];
						}
						emp_cnt[j]=0;
					}
				}
			}
			if (i<R-1) {
				for (int j=i+1; j<R; j++) {
					if (emp_cnt[j]!=C) break;
					if (emp_cnt[j]==C) {
						for (int k=0; k<C; k++) {
							cake[j][k]=cake[i][k];
						}
						emp_cnt[j]=0;
					}
				}
			}
		}
	}
}

int main () {
	int T, R, C;
	scanf("%d", &T);
	char **cake;
	for (int i=0; i<T; i++) {
		scanf("%d%d", &R, &C);
		cake = new char *[R];
		for (int j=0; j<R; j++)
			cake[j] = new char[C];
		char tmp[100];
		for (int j=0; j<R; j++) {
			scanf("%s", tmp);
			for (int k=0; k<C; k++) {
				cake[j][k]=tmp[k];
			}
		}
		
		printf("Case #%d:\n", i+1);
		solve(cake,R,C);
		for (int j=0; j<R; j++) {
			for (int k=0; k<C; k++) 
				printf("%c", cake[j][k]);
			printf("\n");
		}
	}
	return 0;
}
