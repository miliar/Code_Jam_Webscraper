#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

#include <stdio.h>
#include <string.h>

#define ll long long

#pragma warning(disable:4996)

using namespace std;

int D, N;

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d %d", &D, &N);
		double time = 0;
		int k,s;
		for (int i = 0; i < N; i++)
		{
			scanf("%d %d", &k, &s);
			time = max(time, ((double)(D - k)) / s);
		}
		printf("Case #%d: %lf\n", t, ((double)D) / time);
	}
	return 0;
}