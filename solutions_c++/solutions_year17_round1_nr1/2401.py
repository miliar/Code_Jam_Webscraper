#include<stdio.h>

char M[100][100];
int T,R,C;

void printM()
{
	for (int i=0;i<R;i++) {
		for (int j=0;j<C;j++) {
			printf("%c", M[i][j]);
		}
		printf("\n");
	}
}

int solveRow(int r)
{
	char* row = M[r];

	int k=0;
	int i=0;
	int j=0;
	for (i=0;i<C;i++) {
		if (row[i]!='?') {
			break;
		}
	}
	k = i;
	if (k>=C) return -1;

	while (k<C) {
		for (i=j;i<k;i++) {
			M[r][i]=row[k];
		}

		for (i=k+1;i<C;i++) {
			if (row[i]!='?') {
				break;
			} else {
				M[r][i]=row[k];
			}
		}
		j=k+1;
		k=i;
	}
	return 0;
}

int copyRow(int r)
{
	if (r>0) {
		for (int i=0;i<C;i++) {
			M[r][i]=M[r-1][i];
		}
	}
}

int copyRow2(int r)
{
	if (M[r][0]=='?') {
		for (int i=0;i<C;i++) {
			M[r][i]=M[r+1][i];
		}
	}
}
int solve()
{
	for (int i=0;i<R;i++)
		if (solveRow(i)<0)
			copyRow(i);

	for (int i=R-2;i>=0;i--)
		copyRow2(i);
	printM();
}

int main()
{

	scanf("%d", &T);
	for (int i=0;i<T;i++) {
		char line[100];
		scanf("%d %d", &R, &C);


		for (int j=0;j<R;j++){
			scanf("%s", line);
			for (int k=0;k<C;k++)
				M[j][k]=line[k];
		}

		//printM();

		printf("Case #%d:\n", i+1);

		solve();
	}
}
