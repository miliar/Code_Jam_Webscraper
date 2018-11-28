#include <cstdio>
#include <climits>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		int D, N;
		scanf("%d%d", &D, &N);
		
		double highTime = 0.0;
		for(int i = 0; i < N; i++)
		{
			int K, S;
			scanf("%d%d", &K, &S);
			highTime = max(highTime, (double)(D - K) / (double)S);
		}
		
		printf("Case #%d: %.6f\n", t, (double)D / highTime);
	}
}
