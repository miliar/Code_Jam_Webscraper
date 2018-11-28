#include <bits/stdc++.h>
using namespace std;

long long N;
char str[20];
int size;

long long expo(int p)
{
	long long mul = 1;
	for(int i = 0; i < p ; i++)
	    mul *= 10;
	return mul;
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test, tc, i;
	scanf("%d", &test);
	for(tc = 1; tc <= test; tc++)
	{
		scanf("%lld", &N);
		sprintf(str, "%lld", N);
		size = log10(N);
		//printf("%lld --> %d\n", N, size);
		for(i = size; i > 0; i--)
		{
			if(str[i] < str[i - 1]) {
				N -= (N % expo(size - i + 1) + 1);
				sprintf(str, "%lld", N);
				//printf("%s\n", str);
			}
		}
		printf("Case #%d: %lld\n", tc, N);
	}
	return 0;
}
