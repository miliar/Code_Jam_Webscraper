#include<stdio.h>
#include<math.h>
int main(void) {
	int T;
	long long N , tmp, res;
	int num[100] = { 0 };
	int i, j, k, n;
	FILE *f, *f2;
	f = fopen("large_output.txt", "w");
	f2 = fopen("B-large.in", "r");

	//scanf("%d", &T);
	fscanf(f2,"%d", &T);
	for (i = 0; i < T; i++) {
		//scanf("%lld", &N);
		fscanf(f2,"%lld", &N);
		tmp = N;
		n = 0;
		res = 0;
		for (j = 0; tmp > 0; j++) {
			tmp = tmp / 10;
			n++;
		}
		tmp = N;
		for (j = 0; j < n; j++) {
			num[n - j] = tmp % 10;
			tmp = tmp / 10;
		}
		for (j = n; j > 1; j--) {
			if (num[j]<num[j-1]) {
				num[j - 1]--;
				for(k=j;k<=n;k++)
					num[k] = 9;
			}
		}
		//printf("Case #%d: ", i+1);
		fprintf(f,"Case #%d: ", i + 1);
		for (j = 1; j <= n; j++) {
			if (j == 1 && num[j] == 0)
				;
			else
				//printf("%d", num[j]);
				fprintf(f,"%d", num[j]);
		}
		//printf("\n");
		fprintf(f,"\n");
	}
	//scanf("%d", &i);
}