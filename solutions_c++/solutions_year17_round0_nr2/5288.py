#include<stdio.h>
#include<string>

int main(void) {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	char N[18 + 5];
	scanf("%d", &T);
	int i, j;
	int j2;
	int Nlen;
	for (i = 1; i <= T; i++)
	{
		scanf("%s", N);
		Nlen = strlen(N);
		for (j = 0; j < Nlen-1; j++)
		{
			if (N[j] <= N[j + 1]);
			else
			{
				//j까지는 통과
				//j+1부터가 엉망진창
				for (j2 = j + 1; j2 < Nlen; j2++)
					N[j2] = '9';
				//N[j]가 0일리는 없다
				N[j] = N[j] - 1;
				for (j2 = j; j2 >= 0; j2--) 
				{
					if (N[j2 - 1] > N[j2])
					{
						N[j2] = '9';
						N[j2 - 1] = N[j2 - 1] - 1;
					}
				}
				break;
			}
		}
		printf("Case #%d: ",i);
		for (j = 0; j < Nlen; j++) {
			if (N[j] == '0');
			else printf("%c", N[j]);
		}
		printf("\n");
	}
}