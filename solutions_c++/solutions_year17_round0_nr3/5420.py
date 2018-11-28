// ConsoleApplication3.cpp : Defines the entry point for the console application.
//

#include <time.h>
#include <stdio.h>
#include <cstdio>
#include <algorithm>
#include <map>

using namespace std;

void print(long long n)
{
	long long x = n / 2;
	long long y = n - x;
	if (x < y) swap(x, y);
	printf("%I64d %I64d\n", x, y);
}

void cal(long long n1, long long m1, long long n2, long long m2, long long k)
{
	--n1, --n2;
	k -= m1;
	if (k <= 0) {
		print(n1);
		return;
	}
	k -= m2;
	if (k <= 0) {
		print(n2);
		return;
	}
	if (n1 % 2 == 0)
		cal(n1 / 2, m1 * 2 + m2, n2 / 2, m2, k);
	else
		cal(n1 / 2 + 1, m1, n2 / 2, m1 + m2 * 2, k);
}

void work()
{
	long long n, k;
	scanf("%I64d%I64d", &n, &k);
	cal(n + 1, 0, n, 1, k);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		work();
	}
    return 0;
}

