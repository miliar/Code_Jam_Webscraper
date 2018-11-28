#include <cstdio>

using namespace std;

void solve(int t)
{
	printf("Case #%d: ", t);
	
	int D, N;
	scanf("%d%d", &D, &N);
	
	int Ki, Si;
	double tMax = -1.0, ti;
	for (int n = 0; n < N; n++)
	{
		scanf("%d%d", &Ki, &Si);
		ti = (D - Ki) / (double)Si;
		if (ti > tMax)
			tMax = ti;
	}
	printf("%lf\n", D / tMax);
}

int main()
{
	int T;
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++)
		solve(t);
		
	return 0;	
}
