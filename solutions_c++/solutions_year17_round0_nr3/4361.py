#include <cstdio>
long long n, k, num1, num2, sum1, sum2;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		scanf("%I64d%I64d", &n, &k);
		printf("Case #%d: ", tt);
		if (k == 1)
		{
			printf("%I64d %I64d\n", n >> 1 , n - 1 >> 1);
			continue;
		}
		num1 = n >> 1;
		num2 = n - 1 >> 1;
		sum1 = sum2 = 1;
		k--;
		while (k > sum1 + sum2)
		{
			//printf("%I64d %I64d\n", num1, num2);
			k -= sum1 + sum2;
			if (num1 == num2)
			{
				long long xnum1 = num1 >> 1, xnum2 = num1 - 1 >> 1;
				long long xsum1 = sum1 + sum2, xsum2 = sum1 + sum2;
				num1 = xnum1;
				num2 = xnum2;
				sum1 = xsum1;
				sum2 = xsum2;
			}
			else
			{
				if (num1 & 1)
				{
					long long tmp = num1; num1 = num2; num2 = tmp;
					tmp = sum1; sum1 = sum2; sum2 = tmp;
				}
				long long xnum1 = num1 >> 1, xnum2 = num1 - 1 >> 1;
				long long xsum1 = sum1, xsum2 = sum1;
				if ((num2 >> 1) == xnum1)
					xsum1 += sum2;
				else
					xsum2 += sum2;
				if ((num2 - 1 >> 1) == xnum1)
					xsum1 += sum2;
				else
					xsum2 += sum2;
				num1 = xnum1;
				num2 = xnum2;
				sum1 = xsum1;
				sum2 = xsum2;
			}
		}
		if (num1 < num2)
		{
			long long tmp = num1; num1 = num2; num2 = tmp;
			tmp = sum1; sum1 = sum2; sum2 = tmp;
		}
		if (k <= sum1)
			printf("%I64d %I64d\n", num1 >> 1, num1 - 1 >> 1);
		else
			printf("%I64d %I64d\n", num2 >> 1, num2 - 1 >> 1);
	}
	return 0;
}
