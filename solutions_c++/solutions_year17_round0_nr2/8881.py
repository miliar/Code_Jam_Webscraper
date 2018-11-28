//#include <bits/stdc++.h>
#include <cstdio>
#include <string.h>
using namespace std;
int t, i, j, n, k, v, L;
long long res, add, inc;
char arr[45];
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	while (t--)
	{
		v++;
		scanf("%s", arr);
		L = strlen(arr);
		for (i = 1; i < L; i++)
		{
			if (arr[i] < arr[i - 1])
				break;
		}
		if (i == L)
		{
			printf("Case #%d: ",v);
			printf("%s\n", arr);
		}
		else
		{
			printf("Case #%d: ", v);
			for (j = i; j > 0; j--)
			{
				if (arr[j] > arr[j - 1])
					break;
			}
			if (j == 0)
			{
				if (arr[0] != '1')
					printf("%c", (char)(arr[0] - 1));
				for (int x = 0; x< L - 1; x++)
						printf("9");
					puts("");
			}
			else
			{
				arr[j] = (char)(arr[j] - 1);
				for (i = 0; i <=j;i++)
					printf("%c", arr[i]);
				for (; i < L; i++)
					printf("9");
				puts("");
			}
		}
	}
}