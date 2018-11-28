#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

double solve()
{
	return 0.;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=0; t<T; ++t)
	{
		int D, N;
		scanf("%d%d", &D, &N);
		double m = 0;
		for (int i=0; i<N; ++i)
		{
			int K, S;
			scanf("%d%d", &K, &S);
			if (m < double(D-K)/S)
				m = double(D-K)/S;
		}
		printf("Case #%d: %lf\n", t+1, D/m);
	}
	return 0;
}