#include <cstdio>
#include <algorithm>

using namespace std;

#define LLU unsigned long long int

void GetLR(LLU n, LLU k, LLU &l, LLU &r)
{
	if (k == 1)
	{
		l = n / 2 + n % 2 - 1;
		r = n/2;
		return;
	}

	k--;

	if (n % 2)
	{
		GetLR(n / 2, k / 2 + k % 2, l, r);
	}
	else
	{
		GetLR(n / 2 + k % 2 - 1, k / 2 + k % 2, l, r);
	}
}

int main(int argc, char* argv)
{
	int T, t;

	LLU N, K, L, R;

	scanf("%d", &T);

	for (t = 1; t <= T; t++)
	{
		scanf("%llu%llu", &N, &K);
		
		GetLR(N, K, L, R);

		printf("Case #%d: %llu %llu\n", t, max(L,R), min(L,R));
	}

	return 0;
}