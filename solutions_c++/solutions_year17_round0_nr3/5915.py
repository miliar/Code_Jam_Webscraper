#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

#define _CRT_SECURE_NO_WARNINGS

vector <long long> V;

int main()
{
	long long num;
	long long n;
	long long N;
	FILE *fp, *fpp;
	fpp = fopen("output.txt", "wt");

	fp = freopen("C-small-1-attempt1.in", "rt", stdin);
	scanf("%lld", &n);

	for(int T = 1; T <= n; T++)
	{
		V.clear();
		scanf("%lld %lld", &num, &N);
		V.push_back(num);
		N -= 1;
		while (N--)
		{
			long long st = V[V.size() - 1];
			V.pop_back();
			if (st % 2 == 0)
			{
				V.push_back(st / 2);
				V.push_back((st / 2) - 1);
			}
			else
			{
				V.push_back(st / 2);
				V.push_back(st / 2);
			}
			sort(V.begin(), V.end());
		}
		if (V[V.size() - 1] % 2 == 0)
			fprintf(fpp, "Case #%d: %lld %lld\n", T, V[V.size() - 1] / 2, (V[V.size() - 1] / 2) - 1);
		else
			fprintf(fpp, "Case #%d: %lld %lld\n", T, V[V.size() - 1] / 2, V[V.size() - 1] / 2);

	}
	fclose(fpp);
	fclose(fp);
	return 0;
}