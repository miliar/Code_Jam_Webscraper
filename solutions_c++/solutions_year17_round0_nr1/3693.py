#include<stdio.h>

char A[1111];
int N, K, T, Ret;

int main(void)
{
	int l0, l1, l2;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%s %d", A, &K);
		for(N = 0; A[N]; N++);
		
		Ret = 0;
		for(l1 = 0; l1+K <= N; l1++)
		{
			if(A[l1] == '-')
			{
				Ret++;
				for(l2 = 0; l2 < K; l2++)
				{
					if(A[l1+l2] == '-') A[l1+l2] = '+';
					else A[l1+l2] = '-';
				}
			}
		}
		for(l1 = 0; l1 < N; l1++) if(A[l1] == '-') Ret = -1;
		
		if(Ret == -1)
			printf("Case #%d: IMPOSSIBLE\n", l0);
		else
			printf("Case #%d: %d\n", l0, Ret);
	}

	return 0;
}
