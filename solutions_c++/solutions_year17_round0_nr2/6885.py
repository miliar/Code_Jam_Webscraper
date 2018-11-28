#include <cstdio>

int T,cas,n,a[100],stock,j,i,no;
long long N;

void write(int x)
{
	if (no==0 && x==0) return;
	printf("%d", x);
	++no;
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	for (cas=1; cas<=T; ++cas)
	{
		scanf("%I64d", &N);
		printf("Case #%d: ", cas);
		n = 0;
		while (N > 0)
		{
			a[++n] = N%10;
			N /= 10;
		}
		a[0] = 10;
		stock = 0;
		no = 0;
		for (i=n; i>=1; --i)
		{
			if (a[i] < a[i-1])
			{
				for (j=1; j<=stock+1; ++j) write(a[i]);
				stock = 0;
			}
			else
			if (a[i] == a[i-1])
			{
				++stock;
			}
			else
			if (a[i] > a[i-1])
			{
				write(a[i]-1);
				for (j=1; j<=i+stock-1; ++j) write(9);
				break;
			}
		}
		printf("\n");
	}
	return 0;
}
