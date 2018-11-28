#include<stdio.h>
#define ll long long

int vet[19], vet2[19];

main()
{
	int i, j, k, T, tam;
	ll N;
	scanf("%d", &T);
	for(k = 1; k <= T; k++)
	{
		tam = 0;
		scanf("%lld", &N);
		while(N > 0)
		{
			vet2[tam++] = N % 10;
			N /= 10;
		}
		for(i = 0; i < tam; i++)
			vet[i] = vet2[tam-1-i];
		while(1)
		{
			for(i = 1; i < tam; i ++)
				if(vet[i] < vet[i-1])
				{
					j = i-1;
					vet[j]--;
					while(vet[j] < 0)
					{
						vet[j] = 9;
						vet[--j]--;
					}
					for(j = i; j < tam; j++)
						vet[j] = 9;
					break;
				}
			if(i == tam)
				break;
		}
		for(i = 0; i < tam; i++)
			N = 10*N + vet[i];
		printf("Case #%d: %lld\n", k, N);
	}
	return 0;
}
