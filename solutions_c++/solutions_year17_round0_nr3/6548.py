#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

priority_queue<long long int> q;

int main()
{
	int T;
	long long int n, k, tmp, L, R;
	FILE *pf_r, *pf_w;

	pf_r = fopen("C-small-1-attempt0.in", "r");
	pf_w = fopen("C-small-1-attempt0.out", "w+");
	
	fscanf(pf_r,"%d", &T);

	for (int i = 0; i < T; i++)
	{
		fscanf(pf_r,"%lld%lld", &n, &k);
		q.push(n);
		for (int j = 0; j < k; j++)
		{
			tmp = q.top();
			q.pop();
			L = (tmp - 1) >> 1;
			R = tmp >> 1;
			if (L == 0 && R == 0)
				break;
			q.push(L);
			q.push(R);
		}
		while (!q.empty())q.pop();
		fprintf(pf_w,"Case #%d: %lld %lld\n", i + 1, max(L, R), min(L,R));
	}
	return 0;
}