
#include <stdio.h>
#include <string.h>

int K;

int solve(char *a, int start, int end)
{
	int count = 0;
	int orig_start = start;
	int orig_end  = end;
	while(start <= end)
	{
		for (int i = start; i <= end; i++)
		{
			if (a[i] == '-')
			{
				if (i+K-1 <= end)
				{
					for (int j = i; j <=i+K-1; j++)
					{
						a[j] = (a[j] == '+')?'-':'+';
					}
					start = i+1;
					count++;
					break;
				}
			}
			start = i+1;
		}
	}

	for (int i = orig_start; i<=orig_end; i++)
	{
		if (a[i] != '+')
		{
			return -1;
		}
	}
	return count;
}

int solve_invalid(char *a, int start, int end)
{
	int count = 0;
	while(start <= end)
	{
		for(int i = start; i <= end; i++)
		{
			if ((a[i] != a[i+1]) && (i+1) <= end)
			{
				if (i+1+K-1 <= end)
				{
					for (int j = i+1; j < i+1+K; j++)
					{
						a[j] = (a[j] == '+')?'-':'+';
					}
					start = i+1;
					count++;
					break;
				}
				else
				{
					return -1;
				}
			}
		}
	}

	return count;	
}

int main()
{
	char a[1110] = {'0',};
	int T = 0;
	scanf("%d", &T);
	int len = 0;
	for (int k = 0; k < T; k++)
	{
		scanf("%s", a);
		scanf("%d", &K);
		printf("Case #%d: ", k+1);
		int res = solve(a, 0, strlen(a)-1);
		if (res == -1)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n", res);
		}
	}
}
