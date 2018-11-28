#include<stdio.h>

long long X;
int N;
int T;
char A[111];
char B[111];
int Flag;

void Go(int dep, int comp)
{
	int l1, l2;

	if(Flag) return;

	if(dep == N)
	{
		B[dep] = 0;
		Flag = 1;
		return;
	}

	if(comp)
	{
		B[dep] = '9';
		Go(dep+1, comp);
		if(Flag) return;
	}
	else
	{
		B[dep] = A[dep];
		for(l1 = 1; l1 <= dep; l1++)
		{
			if(B[l1] < B[l1-1])
			{
				break;
			}
		}
		if(l1 > dep)
		{
			Go(dep+1, comp);
			if(Flag) return;
		}

		if(B[dep] != '0')
		{
			B[dep]--;
			for(l1 = 1; l1 <= dep; l1++)
			{
				if(B[l1] < B[l1-1])
				{
					break;
				}
			}
			if(l1 > dep)
			{
				Go(dep+1, 1);
				if(Flag) return;
			}
		}
	}
}

int main(void)
{
	int l0, l1, l2;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%lld", &X);
		sprintf(A, "%lld", X);
		for(N = 0; A[N]; N++);

		if(N == 1)
		{
			printf("Case #%d: %lld\n", l0, X);
		}
		else
		{
			Flag = 0;
			Go(0, 0);

			if(B[0] == '0') Flag = 0;

			if(Flag == 0)
			{
				for(l1 = 0; l1 < N; l1++) B[l1] = '9';
				B[N-1] = 0;
			}
			printf("Case #%d: %s\n", l0, B);
		}
	}

	return 0;
}
